from S1_data_load import load_and_combine_data
from S2_data_transform import restructure_and_transform_data
from S3_result1_seasonal_average import result1_seasonal_average
from S3_result2_temperature_range import result2_temperature_range
from S3_result3_temperature_stability import result3_temperature_stability

# Step 4: Load Data and Run Program
def main():
    '''
    Load the data and run the program
    1.1. Load data from CSV files
        - Adding a checking step to stop execution if no data is found to prevent crashes
    1.2. Transforming data: 
        - Clean, format, and add "SEASON" column
    1.3. Generate statistics and export to .txt files
    '''
    try:
        print("--- Starting Data Processing ---")
        
        # 1.1. Load data from CSV files
        dataframes, identifier_cols, month_cols = load_and_combine_data()
        
        if dataframes.empty:
            print("Error: No data loaded. Please check the 'temperatures' folder.")
            return
        
        print("--- Success! Raw data loaded (Wide Format). ---")

        # 1.2. Transforming data
        long_df = restructure_and_transform_data(dataframes, identifier_cols, month_cols)
        
        # 1.3. Generate statistics and export to .txt files
        result1_seasonal_average(long_df)            # Average temp per season
        result2_temperature_range(long_df)           # Max temp range
        result3_temperature_stability(long_df)       # Standard deviation (stability)

        print("--- Success! Results exported. ---")  

    except FileNotFoundError:
        print("ERROR: File or directory not found. Check 'temperatures' folder.")

    except Exception as e:
          print(f"An unexpected error occurred: {type(e).__name__} - {e}")

if __name__ == "__main__":
    main()