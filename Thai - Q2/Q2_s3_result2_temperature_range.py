from Q2_s1_data_load import load_and_combine_data
from Q2_s2_data_transform import restructure_and_transform_data

# Result 2: Station with the Largest Temperature Range 
def result2_temperature_range():

    data, identifier_cols, month_cols = load_and_combine_data()
    long_df = restructure_and_transform_data(data, identifier_cols, month_cols)

    station_stats = long_df.groupby("STATION_NAME")["TEMP"].agg(["min", "max"])
    station_stats["range"] = station_stats["max"] - station_stats["min"]

    max_range = station_stats["range"].max()
    winners = station_stats[station_stats["range"] == max_range]

    with open("2. Temperature_Range.txt", "w", encoding="utf-8") as f:
        for station, row in winners.iterrows():
            f.write(
                f"{station}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")
    return winners

if __name__ == "__main__":
    print(f"Largest Temperature Range result is updated in text file.")
    result2_temperature_range()