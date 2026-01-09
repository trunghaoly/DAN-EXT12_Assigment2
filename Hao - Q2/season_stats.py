def calculate_seasonal_avg (dataframes):
    """Calculate and export average temperature for each season."""

    # Group data by season and calculate mean temperature
    grouped = dataframes.groupby("Season")["Temp"].mean().reindex(["Summer", "Autumn", "Winter", "Spring"])
    season_ave_temp = grouped.reset_index()

    # Save result
    with open ('average_temp.txt','w',encoding='utf-8') as f:
        for index,row in season_ave_temp.iterrows():
            f.write(f"{row['Season']}: {row['Temp']:.1f}°C\n")