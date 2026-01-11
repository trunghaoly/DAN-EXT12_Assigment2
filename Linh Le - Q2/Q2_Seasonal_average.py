import os
from Q2_Export_Combine import *

def seasonal_average (df):
# add seasons cl

     df['Summer'] = df[['December', 'January', 'February']].sum(axis=1)
     df['Autumn'] = df[['March', 'April', 'May']].sum(axis=1)
     df['Winter'] = df[['June', 'July', 'August']].sum(axis=1)
     df['Spring'] = df[['September', 'October', 'November']].sum(axis=1)

     a= df['Summer'].mean()/3
     b= df['Spring'].mean()/3
     c= df['Autumn'].mean()/3
     d= df['Winter'].mean()/3
     
     average_temp =pd.Series({'Summer': a,'Spring':b, 'Autumn':c, 'Winter':d})
     return average_temp


average_temp = seasonal_average(df)


with open ('average_temp.txt','w') as g:
     for season, value in average_temp.items():
          g.write(f"{season}: {value:.1f} °C\n")