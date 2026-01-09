from data_loader import *
from preprocessor import *
from season_stats import *
from range_analysis import *
from stability_analysis import *

def main():
    try:
        print("--- Starting Data Processing ---")
        # Load data from CSV files
        dataframes = load_data()
        # Stop execution if no data is found to prevent crashes
        if dataframes.empty:
            print("Error: No data loaded. Please check the 'temperatures' folder.")
            return
        
        # Process data: Clean, format, and add 'Season' column
        dataframes = transform_data(dataframes)
        
        # Generate statistics and export to .txt files
        calculate_seasonal_avg(dataframes)     # Average temp per season
        find_largest_range(dataframes)     # Max temp range
        analyze_stability(dataframes)         # Standard deviation (stability)

        print("--- Success! All results have been exported. ---")  

    except FileNotFoundError:
        print("ERROR: File or directory not found. Check 'temperatures' folder.")

    except Exception as e:
          print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()