def find_largest_range (dataframes):
    """Find and export the station with the largest temperature range."""

    # Calculate Max, Min, and Range per station
    station_stats = dataframes.groupby('STATION_NAME')['Temp'].agg(["min","max"])

    # Calculate Range (Max - Min)
    station_stats['Range'] = station_stats['max'] - station_stats['min']

    # Identify the highest range value
    max_temp_range = station_stats['Range'].max()
    print(station_stats)

    # Export station with largest range
    with open('largest_temp_range_station.txt', 'w', encoding='utf-8') as f:
        for station_name, row in station_stats.iterrows():
            if row['Range'] == max_temp_range:
                mi = row['min']
                ma  = row['max']
                f.write(f'Station {station_name}: Range {max_temp_range:.1f}°C (Max: {ma:.1f}°C, Min: {mi:.1f}°C)\n')
