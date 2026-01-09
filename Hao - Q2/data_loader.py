import pandas as pd
from pathlib import Path
def load_data ():

    """Load and combine all temperature CSV files into one DataFrame."""

    # Setup path to the 'temperatures' folder
    base_direct = Path(__file__).resolve().parent
    data_direct = base_direct / "temperatures"

    # Get list of all matching CSV files
    file = sorted(data_direct.glob("stations_group_*.csv"))

    full_data = []
    for filename in file:
        # Read each CSV file and append to list
        data_temp = pd.read_csv(filename)
        full_data.append(data_temp)

    # Merge all data into a single DataFrame
    dataframes = pd.concat(full_data, ignore_index = True)

    return dataframes