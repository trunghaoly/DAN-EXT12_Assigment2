from S1_data_load import load_and_combine_data
from S2_data_transform import restructure_and_transform_data

# Result 2: Largest Temperature Range 
def result2_temperature_range(long_df):
    '''
    Find and export the station with the largest temperature range.
    1.1. Calculate Max, Min, and Range per station
        - Groups the data by STATION_NAME.
        - Uses .agg() to find the absolute minimum and maximum temperature at each station.
        - Calculates the temperature range (max - min).
    1.2. Identify the highest range value
        - Finds the maximum range among all stations and filters the DataFrame 
          to select only the stations that achieved this maximum range.
    1.3. Write and Return the result to file
    '''
    
    # 1.1. Calculate Max, Min, and Range per station
    station_stats = long_df.groupby("STATION_NAME")["TEMP"].agg(["min", "max"])
    station_stats["range"] = station_stats["max"] - station_stats["min"]

    # 1.2. Identify the highest range value
    max_range = station_stats["range"].max()
    winners = station_stats[station_stats["range"] == max_range]

    # 1.3. Write and Return the result to file
    with open("2. Temperature_Range.txt", "w", encoding="utf-8") as f:
        for station, row in winners.iterrows():
            f.write(
                f"{station}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")
            
    return winners

# Independence Test
if __name__ == "__main__":
    print("Processing analysis for Result 2 - Largest Temperature Range...")
    
    # Load and Transform Data
    dataframes, identifier_cols, month_cols = load_and_combine_data()
    long_df = restructure_and_transform_data(dataframes, identifier_cols, month_cols)
    
    # Calculate Result
    result = result2_temperature_range(long_df)
    
    print("\nResult 2 - Largest Temperature Range save to file '2. Temperature_Range.txt'")
    print(result)