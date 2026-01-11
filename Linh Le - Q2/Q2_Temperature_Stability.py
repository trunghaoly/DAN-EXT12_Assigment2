import os
from Q2_Export_Combine import *

def temp_sta (df):
     months = ['January','February','March','April','May','June',
     'July','August','September','October','November','December']
     df[months]=df[months].apply(pd.to_numeric, errors = 'coerce')
     df['std']=df[months].std(axis=1)
     max = df['std'].max()
     min = df['std'].min()
     idx_min = df['std'].idxmin()
     idx_max = df['std'].idxmax()
     station_min = df.loc[idx_min, 'STATION_NAME']
     station_max = df.loc[idx_max, 'STATION_NAME']
     return idx_min, idx_max, station_min, station_max, max, min

idx_min, idx_max, station_min, station_max, max, min  = temp_sta (df)

with open ('temperature_stability_stations.txt','w') as k:
     k.write(f"Most Stable: Station {station_min}: StdDev {min:.1f} °C\n")
     k.write(f"Most Variable: Station {station_max}: StdDev {max:.1f} °C\n")