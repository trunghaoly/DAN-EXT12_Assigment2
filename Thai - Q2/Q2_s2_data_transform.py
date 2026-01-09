import pandas as pd
from Q2_s1_data_load import load_and_combine_data

# Step 2: Restructuring Data (wide → long) + Data Transformation (Australian seasons)
def restructure_and_transform_data(data, identifier_cols, month_cols):
    
    long_df = data.melt(
        id_vars=identifier_cols,
        value_vars=month_cols,
        var_name="MONTH",                   
        value_name="TEMP"                   
        )                        

    month_to_season = {                                                             
        "December": "Summer", "January": "Summer", "February": "Summer",
        "March": "Autumn", "April": "Autumn", "May": "Autumn",
        "June": "Winter", "July": "Winter", "August": "Winter",
        "September": "Spring", "October": "Spring", "November": "Spring"}
    
    long_df["SEASON"] = long_df["MONTH"].map(month_to_season)
    return long_df   