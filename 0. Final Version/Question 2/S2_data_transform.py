import pandas as pd
import numpy as np

# Step 2: Restructuring Data (wide → long) + Data Transformation (Australian seasons)
def restructure_and_transform_data(dataframes, identifier_cols, month_cols):
    '''
    Reshape the dataframe, clean missing values, and add a 'Season' column.
    1.1. Convert month columns into rows using melt
        - Step 1 Dataframe is in a "wide" format (12 columns for months).
        - Uses the melt function to transform it into a "long" format.
        - Creates new columns: 
            + "MONTH": hold the names of the original month columns
            + "TEMP": hold the actual temperature values in the month columns.
    1.2. Ignore missing values (NaN)
    1.3. Define mapping logic
        - Create two lists contain the logic of transfering month to season
        - Create new column "SEASON" and applying the logic.
    '''
    
    # 1.1. Convert month columns into rows using melt
    long_df = dataframes.melt(
        id_vars = identifier_cols,
        value_vars = month_cols,
        var_name = "MONTH",                   
        value_name = "TEMP"                   
    )                        

    # 1.2. Ignore missing values (NaN)
    long_df = long_df.dropna()

    # 1.2. Define season mapping logic
    conditions = [
        long_df["MONTH"].isin(['December', 'January', 'February']),
        long_df["MONTH"].isin(['March','April','May']),
        long_df["MONTH"].isin(['June','July','August']),
        long_df["MONTH"].isin(['September','October','November']),
    ]
    choices = ['Summer','Autumn','Winter','Spring']

    long_df["SEASON"] = np.select(conditions,choices)
    
    return long_df   