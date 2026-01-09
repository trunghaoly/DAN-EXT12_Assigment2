from Q2_s1_data_load import load_and_combine_data
from Q2_s2_data_transform import restructure_and_transform_data

def result3_temperature_stability():

    data, identifier_cols, month_cols = load_and_combine_data()
    long_df = restructure_and_transform_data(data, identifier_cols, month_cols)

    std_by_station = long_df.groupby("STATION_NAME")["TEMP"].std()

    min_std = std_by_station.min()
    max_std = std_by_station.max()

    most_stable = std_by_station[std_by_station == min_std]
    most_variable = std_by_station[std_by_station == max_std]

    with open("3. Temperature_Stability.txt", "w", encoding="utf-8") as f:
        f.write("Most Stable:\n")
        for station, val in most_stable.items():
            f.write(f"- {station}: StdDev {val:.1f}°C\n")

        f.write("\nMost Variable:\n")
        for station, val in most_variable.items():
            f.write(f"- {station}: StdDev {val:.1f}°C\n")

if __name__ == "__main__":
    print(f"Temperature Stability result is updated in text file.")
    result3_temperature_stability()
