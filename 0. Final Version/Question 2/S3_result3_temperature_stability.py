from S1_data_load import load_and_combine_data
from S2_data_transform import restructure_and_transform_data

# Result 3: Temperatures Stability & Variability 
def result3_temperature_stability(long_df):
    '''
    Calculate standard deviation to identify temperature stability.
    1.1. Group data by station and Calculate standard deviation
        - Groups the data by STATION_NAME.
        - Calculates .std()) of temperatures for each station.
    1.2. Identify the minimum (most stable) and maximum (most variable) values
        - Finds the minimum and maximum standard deviation values.
    1.3. Filter stations matching the minimum and maximum stability
        - most_stable: The stations with the minimum standard deviation.
        - most_variable: The stations with the maximum standard deviation.
    1.4. Write and Return the result to file
    '''
    # 1.1. Group data by station and Calculate standard deviation
    std_by_station = long_df.groupby("STATION_NAME")["TEMP"].std()

    # 1.2. Identify the minimum (most stable) and maximum (most variable) values
    min_std = std_by_station.min()
    max_std = std_by_station.max()

    # 1.3. Filter stations matching the minimum and maximum stability
    most_stable = std_by_station[std_by_station == min_std]
    most_variable = std_by_station[std_by_station == max_std]

    # 1.4. Write and Return the result to file
    with open("3. Temperature_Stability.txt", "w", encoding="utf-8") as f:
        
        # Write the most stable stations
        f.write("Most Stable:\n")
        for station, val in most_stable.items():
            f.write(f"- {station}: StdDev {val:.1f}°C\n")

        # Write the most variable stations
        f.write("\nMost Variable:\n")
        for station, val in most_variable.items():
            f.write(f"- {station}: StdDev {val:.1f}°C\n")
    
    return {"Most Stable": most_stable, "Most Variable": most_variable}

# Independence Test
if __name__ == "__main__":
    print("Processing analysis for Result 3 - Temperatures Stability & Variability...")
    
    # Load and Transform Data
    dataframes, identifier_cols, month_cols = load_and_combine_data()
    long_df = restructure_and_transform_data(dataframes, identifier_cols, month_cols)
    
    # Calculate Result
    result = result3_temperature_stability(long_df)
    
    print("\nResult 3 - Temperatures Stability & Variability save to file '3. Temperature_Stability.txt'")
    print(result)