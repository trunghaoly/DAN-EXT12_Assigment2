from pathlib import Path
import pandas as pd

# Step 1: Setup and Data Loading
def load_and_combine_data():
    
    base_direct = Path(__file__).resolve().parent
    data_direct = base_direct / "temperatures"
    files = sorted(data_direct.glob("stations_group_*.csv"))

    identifier_cols = ["STATION_NAME", "STN_ID", "LAT", "LON", "YEAR"]
    month_cols = ["January","February","March","April","May","June",
                  "July","August","September","October","November","December"]

    dfs = []
    for f in files:
        df = pd.read_csv(f)
        df["YEAR"] = int(f.stem.split("_")[-1])
        df[month_cols] = df[month_cols].apply(pd.to_numeric, errors="coerce")
        dfs.append(df)
    
    data = pd.concat(dfs, ignore_index=True)
    return data, identifier_cols, month_cols