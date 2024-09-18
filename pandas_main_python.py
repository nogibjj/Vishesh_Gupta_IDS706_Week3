"""
Main Python module for functionality.
"""

import pandas as pd
import matplotlib.pyplot as plt
import time


start_time = time.time()


def read_csv_file(csv):
    return pd.read_csv(csv, encoding="ISO-8859-1", delimiter=";")


def generalise_data(general_df, col):
    describe_value = general_df[[col]].describe()
    median_value = general_df[[col]].median()
    describe_value.loc["median"] = median_value
    return describe_value


def line_graph_visualisation(df, x_axis, y_axis, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    df_sorted = df.sort_values(by=x_axis)

    plt.plot(
        df_sorted[x_axis], df_sorted[y_axis], marker="o", linestyle="-", color="blue"
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def bar_graph_visualisation(df, title, xlabel, ylabel, legend):
    df.plot(kind="bar", stacked=False, colormap="Set2", figsize=(10, 6))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Show the plot
    plt.legend(title=legend)
    plt.show()


nba_data_file = read_csv_file("2023-2024 NBA Player Stats - Regular.csv")

# get all statistical information about the Age column
data_summary = generalise_data(nba_data_file, "Age")

grouped_data = nba_data_file.groupby("Pos", as_index=False).agg(
    Total_Points=("PTS", "sum"),  # Sum of points per position
    Player_Count=("Pos", "count"),  # Count of players per position
)

grouped_data["avg_point_per_player"] = (
    grouped_data["Total_Points"] / grouped_data["Player_Count"]
)

grouped_multiple_data = nba_data_file.groupby(["Pos", "Tm"], as_index=False).agg(
    Total_Points=("PTS", "sum"),  # Sum of points per position
    Player_Count=("Pos", "count"),  # Count of players per position
)

pivot_df = grouped_multiple_data.pivot(
    index="Tm", columns="Pos", values="Total_Points"
).fillna(0)

line_graph_visualisation(
    grouped_data,
    "Pos",
    "avg_point_per_player",
    "Average Points by Player Position",
    "Player Position",
    "Average Points",
)

bar_graph_visualisation(
    pivot_df, "Total Points by Team", "Team", "Total Points", "Position"
)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
