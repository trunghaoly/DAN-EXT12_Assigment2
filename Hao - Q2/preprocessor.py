import pandas as pd
import numpy as np

def transform_data (dataframes):
    """
        Reshape the dataframe, clean missing values, and add a 'Season' column.
    """

    # Identify ID columns and Month columns
    id_cols = dataframes.columns[0:4]
    month_cols = dataframes.columns[4:16]

    # Convert month columns into rows using melt
    dataframes = dataframes.melt(
        id_vars = id_cols,
        value_vars = month_cols,
        var_name="Month",                   
        value_name="Temp"                   
    )

    # Ignore missing values (NaN)
    dataframes["Temp"] = pd.to_numeric(dataframes["Temp"], errors="coerce")
    dataframes = dataframes.dropna()

    # Define season mapping logic
    conditions = [
                    dataframes['Month'].isin(['December', 'January', 'February']),
                    dataframes['Month'].isin(['March','April','May']),
                    dataframes['Month'].isin(['June','July','August']),
                    dataframes['Month'].isin(['September','October','November']),
    ]
    choices = ['Summer','Autumn','Winter','Spring']

    # Assign 'Season' column based on logic
    dataframes['Season'] = np.select(conditions,choices)
    
    return dataframes