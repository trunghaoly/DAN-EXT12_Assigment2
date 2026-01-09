from Q2_s1_data_load import load_and_combine_data
from Q2_s2_data_transform import restructure_and_transform_data

# Result 1: Seasonal Average Temperature
def result1_seasonal_average():
    
    data, identifier_cols, month_cols = load_and_combine_data()
    long_df = restructure_and_transform_data(data, identifier_cols, month_cols)

    season_avg = long_df.groupby("SEASON")["TEMP"].mean().reindex(
                 ["Summer", "Autumn", "Winter", "Spring"])

    with open("1. Seasonal_Average.txt", "w", encoding="utf-8") as f:
        for season, avg in season_avg.items():
            f.write(f"{season}: {avg:.1f}°C\n")
    return season_avg

if __name__ == "__main__":
    print(f"Seasonal Average temperature result is updated in text file.")
    result1_seasonal_average()