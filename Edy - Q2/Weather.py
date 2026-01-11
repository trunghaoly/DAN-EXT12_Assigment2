import os
import re
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple


class AustralianWeatherAnalyzer:
    """Analyzes temperature data from multiple Australian weather stations."""

    # Australian seasons mapping
    SEASONS = {
        'Summer': [12, 1, 2],      # Dec, Jan, Feb
        'Autumn': [3, 4, 5],       # Mar, Apr, May
        'Winter': [6, 7, 8],       # Jun, Jul, Aug
        'Spring': [9, 10, 11]      # Sep, Oct, Nov
    }

    def __init__(self, data_folder: str = 'temperatures'):
        """
        Initialize the analyzer with path to data folder.

        Args:
            data_folder: Path to folder containing CSV files
        """
        self.data_folder = data_folder
        self.all_data = None
        self.station_data = {}

    def load_data(self) -> bool:
        """
        Load all CSV files from the temperatures folder.

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        if not os.path.exists(self.data_folder):
            print(f"Error: Folder '{self.data_folder}' not found.")
            return False

        csv_files = list(Path(self.data_folder).glob('*.csv'))

        if not csv_files:
            print(f"Error: No CSV files found in '{self.data_folder}' folder.")
            return False

        print(f"Found {len(csv_files)} CSV file(s) to process...")

        dataframes = []
        for file_path in sorted(csv_files):
            try:
                df = pd.read_csv(file_path)

                # Your format:
                # STATION_NAME, STN_ID, LAT, LON, January, February, ..., December

                # Rename STATION_NAME -> station
                if 'station' not in df.columns and 'STATION_NAME' in df.columns:
                    df.rename(columns={'STATION_NAME': 'station'}, inplace=True)

                # Identify month columns
                month_cols = [
                    'January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December'
                ]
                month_cols = [m for m in month_cols if m in df.columns]

                if 'station' not in df.columns or not month_cols:
                    print(f"Warning: Skipping {file_path.name} - cannot find station or month columns")
                    continue

                # Infer year from filename, e.g. stations_group_1986.csv
                year = 2000
                year_match = re.search(r'(\d{4})', file_path.name)
                if year_match:
                    year = int(year_match.group(1))

                # Build long-format rows: station, date, temperature
                long_rows = []
                for _, row in df.iterrows():
                    station_name = row['station']
                    for month_index, month_name in enumerate(month_cols, start=1):
                        temp_val = row[month_name]
                        if pd.isna(temp_val):
                            continue
                        long_rows.append({
                            'station': station_name,
                            # 15th day of each month as dummy date
                            'date': f"{year}-{month_index:02d}-15",
                            'temperature': temp_val
                        })

                if not long_rows:
                    print(f"Warning: Skipping {file_path.name} - no temperature data after reshaping")
                    continue

                df_long = pd.DataFrame(long_rows)
                df_long['date'] = pd.to_datetime(df_long['date'], errors='coerce')
                df_long['temperature'] = pd.to_numeric(df_long['temperature'], errors='coerce')

                dataframes.append(df_long)
                print(f"  Loaded: {file_path.name}")

            except Exception as e:
                print(f"Error loading {file_path.name}: {e}")
                continue

        if not dataframes:
            print("Error: No data could be loaded from CSV files.")
            return False

        # Combine all dataframes
        self.all_data = pd.concat(dataframes, ignore_index=True)
        print(f"Total records loaded: {len(self.all_data)}")

        # Organize data by station
        self._organize_by_station()
        return True

    def _organize_by_station(self):
        """Organize data by individual stations."""
        if self.all_data is None:
            return

        self.station_data = {}
        for station in self.all_data['station'].unique():
            station_df = self.all_data[self.all_data['station'] == station].copy()
            self.station_data[station] = station_df

    def calculate_seasonal_averages(self) -> Dict[str, float]:
        """
        Calculate average temperature for each season across all stations and years.
        Ignores NaN values in calculations.

        Returns:
            dict: Season names mapped to average temperatures
        """
        seasonal_averages = {}

        for season, months in self.SEASONS.items():
            season_data = self.all_data[
                self.all_data['date'].dt.month.isin(months)
            ]['temperature']

            avg_temp = season_data.mean()  # ignores NaN
            seasonal_averages[season] = avg_temp

        return seasonal_averages

    def find_largest_temperature_range(self) -> Tuple[List[str], Dict]:
        """
        Find station(s) with the largest temperature range.

        Returns:
            tuple: (list of station names with max range, details dict)
        """
        station_ranges = {}

        for station, station_df in self.station_data.items():
            temps = station_df['temperature'].dropna()
            if len(temps) == 0:
                continue

            max_temp = temps.max()
            min_temp = temps.min()
            temp_range = max_temp - min_temp

            station_ranges[station] = {
                'range': temp_range,
                'max': max_temp,
                'min': min_temp
            }

        if not station_ranges:
            return [], {}

        max_range = max(info['range'] for info in station_ranges.values())

        stations_with_max_range = [
            station for station, info in station_ranges.items()
            if info['range'] == max_range
        ]

        return sorted(stations_with_max_range), station_ranges

    def find_temperature_stability(self) -> Tuple[List[str], List[str], Dict]:
        """
        Find station(s) with most stable (smallest std dev) and
        most variable (largest std dev) temperatures.

        Returns:
            tuple: (most_stable_stations, most_variable_stations, stability_dict)
        """
        stability_data = {}

        for station, station_df in self.station_data.items():
            temps = station_df['temperature'].dropna()
            if len(temps) == 0:
                continue

            std_dev = temps.std()
            stability_data[station] = std_dev

        if not stability_data:
            return [], [], {}

        min_std = min(stability_data.values())
        max_std = max(stability_data.values())

        most_stable = sorted([
            station for station, std in stability_data.items()
            if std == min_std
        ])

        most_variable = sorted([
            station for station, std in stability_data.items()
            if std == max_std
        ])

        return most_stable, most_variable, stability_data

    def save_seasonal_averages(self, output_file: str = 'average_temp.txt'):
        """Save seasonal average temperatures to file."""
        averages = self.calculate_seasonal_averages()

        with open(output_file, 'w') as f:
            for season in ['Summer', 'Autumn', 'Winter', 'Spring']:
                avg_temp = averages.get(season, float('nan'))
                if pd.notna(avg_temp):
                    f.write(f"{season}: {avg_temp:.1f}°C\n")
                else:
                    f.write(f"{season}: No data available\n")

        print(f"Seasonal averages saved to '{output_file}'")

    def save_largest_temperature_range(self, output_file: str = 'largest_temp_range_station.txt'):
        """Save largest temperature range information to file."""
        stations, ranges = self.find_largest_temperature_range()

        with open(output_file, 'w') as f:
            if not stations:
                f.write("No temperature data available.\n")
            else:
                for station in stations:
                    info = ranges[station]
                    f.write(
                        f"Station {station}: Range {info['range']:.1f}°C "
                        f"(Max: {info['max']:.1f}°C, Min: {info['min']:.1f}°C)\n"
                    )

        print(f"Largest temperature range saved to '{output_file}'")

    def save_temperature_stability(self, output_file: str = 'temperature_stability_stations.txt'):
        """Save temperature stability information to file."""
        most_stable, most_variable, stability_data = self.find_temperature_stability()

        with open(output_file, 'w') as f:
            if not stability_data:
                f.write("No temperature data available.\n")
            else:
                f.write("Most Stable:\n")
                if most_stable:
                    for station in most_stable:
                        std_dev = stability_data[station]
                        f.write(f"  Station {station}: StdDev {std_dev:.1f}°C\n")

                f.write("\nMost Variable:\n")
                if most_variable:
                    for station in most_variable:
                        std_dev = stability_data[station]
                        f.write(f"  Station {station}: StdDev {std_dev:.1f}°C\n")

        print(f"Temperature stability saved to '{output_file}'")

    def generate_report(self):
        """Generate complete report with all analyses."""
        print("\n" + "=" * 60)
        print("AUSTRALIAN WEATHER STATION ANALYSIS REPORT")
        print("=" * 60)

        print("\n1. SEASONAL AVERAGE TEMPERATURES")
        print("-" * 40)
        averages = self.calculate_seasonal_averages()
        for season in ['Summer', 'Autumn', 'Winter', 'Spring']:
            avg = averages.get(season, float('nan'))
            if pd.notna(avg):
                print(f"   {season}: {avg:.1f}°C")

        print("\n2. LARGEST TEMPERATURE RANGE")
        print("-" * 40)
        stations, ranges = self.find_largest_temperature_range()
        if stations:
            for station in stations:
                info = ranges[station]
                print(
                    f"   Station {station}: Range {info['range']:.1f}°C "
                    f"(Max: {info['max']:.1f}°C, Min: {info['min']:.1f}°C)"
                )
        else:
            print("   No data available")

        print("\n3. TEMPERATURE STABILITY")
        print("-" * 40)
        most_stable, most_variable, stability_data = self.find_temperature_stability()
        if stability_data:
            print("   Most Stable:")
            for station in most_stable:
                print(f"      Station {station}: StdDev {stability_data[station]:.1f}°C")

            print("   Most Variable:")
            for station in most_variable:
                print(f"      Station {station}: StdDev {stability_data[station]:.1f}°C")
        else:
            print("   No data available")

        print("\n" + "=" * 60 + "\n")


def main():
    """Main execution function."""
    # Use folder where this script lives, plus 'temperatures'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    temps_folder = os.path.join(script_dir, "temperatures")

    analyzer = AustralianWeatherAnalyzer(temps_folder)

    if not analyzer.load_data():
        return

    analyzer.generate_report()
    analyzer.save_seasonal_averages()
    analyzer.save_largest_temperature_range()
    analyzer.save_temperature_stability()

    print("Analysis complete!")


if __name__ == '__main__':
    main()
