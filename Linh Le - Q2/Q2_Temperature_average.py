import os
from Q2_Export_Combine import *


def temp_range (df):
     months = ['January','February','March','April','May','June',
     'July','August','September','October','November','December']
     df[months]=df[months].apply(pd.to_numeric, errors = 'coerce')

     df['Max'] = df[months].max(axis=1)
     df['Min'] = df[months].min(axis=1)
     max_range = df.groupby('STATION_NAME').agg(max_temp=('Max','max'),min_temp=('Min','min'))
     max_range['Range'] = max_range['max_temp']-max_range['min_temp']
     idx = max_range['Range'].idxmax()
     row = max_range.loc[idx]
     return max_range, idx, row

max_range, idx, row = temp_range(df)
with open("largest_temp_range_station.txt", "w") as f:
    f.write(
        f"Station {idx}: Range {row['Range']:.1f}°C "
        f"(Max: {row['max_temp']:.1f}°C, Min: {row['min_temp']:.1f}°C)\n"
    )
