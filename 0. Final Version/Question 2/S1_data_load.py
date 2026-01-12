from pathlib import Path
import pandas as pd

# Step 1: Setup and Data Loading
def load_and_combine_data():
    '''
    Locating, reading, and combining all the individual temperature data files.
    1.1. Define File Paths 
        - Locates the script's directory, build the path to 'temperatures' folder, 
          find and sort all 'stations_group_*.csv' files for sequential processing.
    1.2. Define Column Names
        - Group 1: identifier columns with constant values (STATION_NAME, LAT, LON, YEAR)
        - Group 2: 12 month columns with changing values (temperature)
    1.3. Creat Loop and Combine DataFrames
        - Reads the file into a DataFrame.
        - Converts the temperature value from string to numeric type
        - Appends the processed DataFrame to a list.
    1.4. Concatenates all yearly DataFrames into a single, comprehensive DataFrame.  
    '''

    # 1.1. Define File Paths:
    base_direct = Path(__file__).resolve().parent
    data_direct = base_direct / "temperatures"

    files = sorted(data_direct.glob("stations_group_*.csv"))

    # 1.2. Define Column Names:
    identifier_cols = ["STATION_NAME", "STN_ID", "LAT", "LON", "YEAR"]
    month_cols = ["January","February","March","April","May","June",
                  "July","August","September","October","November","December"]

    # 1.3. Creat Loop and Combine DataFrames:
    dfs = []
    for f in files:
        df = pd.read_csv(f)
        df[month_cols] = df[month_cols].apply(pd.to_numeric, errors="coerce")
        df["YEAR"] = int(f.stem.split("_")[-1])
        dfs.append(df)
    
    #1.4. Merges yearly DataFrames into one DataFrame
    dataframes = pd.concat(dfs, ignore_index=True)
    
    return dataframes, identifier_cols, month_cols