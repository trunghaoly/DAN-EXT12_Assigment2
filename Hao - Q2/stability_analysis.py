import pandas as pd

def analyze_stability(dataframes):
    """Calculate standard deviation to identify temperature stability."""

    # Initialize an empty DataFrame to store statistics
    station_stats = pd.DataFrame()

    # Group data by station and select the temperature column
    grouped = dataframes.groupby('STATION_NAME')['Temp']

    # Calculate standard deviation and assign to 'Stability' column
    station_stats['Stability']=grouped.std()

    # Identify the minimum (most stable) and maximum (most variable) values
    min_std = station_stats['Stability'].min()
    max_std = station_stats['Stability'].max()

    # Filter stations matching the minimum and maximum stability
    most_stable = station_stats[station_stats['Stability'] == min_std]
    most_variable = station_stats[station_stats['Stability'] == max_std]

    # Export most and least stable stations
    with open('temperature_stability_stations.txt', 'w', encoding='utf-8') as f:
        
        # Write the most stable stations
        f.write("Most Stable:\n")
        for station_name,row in most_stable.iterrows():
            f.write(f'{station_name}: StdDev {min_std:.1f}°C\n')

        # Write the most variable stations
        f.write("\nMost Variable:\n")
        for station_name,row in most_variable.iterrows():        
            f.write(f'{station_name}: StdDev {max_std:.1f}°C\n')