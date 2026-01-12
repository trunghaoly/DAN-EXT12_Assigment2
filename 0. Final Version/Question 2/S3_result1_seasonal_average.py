from S1_data_load import load_and_combine_data
from S2_data_transform import restructure_and_transform_data

# Result 1: Seasonal Average Temperature
def result1_seasonal_average(long_df):
    '''
    Calculate and export average temperature for each season.
    1.1. Group data and calculate Seasonal Average Temperature
        - Groups the data by "SEASON" column.
        - Calculates the mean() of the TEMP column for each season.
        - Reindex orders the seasons in a traditional.
        - Converts the result back into a DataFrame using reset_index()
    1.2. Write and Return the result to file
    '''
    
    # 1.1. Group data and calculate Seasonal Average Temperature
    season_avg = long_df.groupby("SEASON")["TEMP"].mean().reindex(
                 ["Summer", "Autumn", "Winter", "Spring"])
    season_ave_temp = season_avg.reset_index()

    # 1.2. Write and Return the result to file
    with open("1. Seasonal_Average.txt", "w", encoding="utf-8") as f:
        for index, row in season_ave_temp.iterrows():
            f.write(f"{row['SEASON']}: {row['TEMP']:.1f}°C\n")
            
    return season_ave_temp

# Independence Test
if __name__ == "__main__":
    print("Processing analysis for Result 1 - Seasonal Average Temperature")
    
    # Load and Transform Data
    dataframes, identifier_cols, month_cols = load_and_combine_data()
    long_df = restructure_and_transform_data(dataframes, identifier_cols, month_cols)
    
    # Calculate Result
    result = result1_seasonal_average(long_df)
    
    print("\nResult 1 - Seasonal Average Temperature save to file '1. Seasonal_Average.txt'")
    print(result)