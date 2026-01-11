file_path = '/Users/lehoangphuonglinh/Desktop/CDU/Python1/Assignment 2/temperatures/'
import pandas as pd
import glob
import os

def combine_file (file_path):
# 1. Find all csv files
     files = glob.glob(os.path.join(file_path, "*.csv"))

# 2. Read each file into a DataFrame
     dfs = [pd.read_csv(f) for f in files]

# 3. Combine them into one DataFrame
     df = pd.concat(dfs, ignore_index=True)
     return df

df = combine_file(file_path)