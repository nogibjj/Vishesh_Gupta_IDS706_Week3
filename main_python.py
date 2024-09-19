"""
Main Python module for functionality.
"""

import polars as pl
import matplotlib.pyplot as plt
import time

start_time = time.time()


def read_csv_file(csv_file, encoding="ISO-8859-1", delimiter=";"):
    # Reads the CSV file using Polars
    return pl.read_csv(csv_file, encoding=encoding, separator=delimiter)


def generalise_data(df):
    return df.describe(), df.median()


def line_graph_visualisation(df, x_axis, y_axis, title, xlabel, ylabel):
    # Creates a line plot using Matplotlib
    x_data = df.select(x_axis).to_numpy().flatten()
    y_data = df.select(y_axis).to_numpy().flatten()

    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker="o", linestyle="-", color="blue")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to fit everything
    plt.show()


def bar_graph_visualisation(pivot_df, title, xlabel, ylabel, legend):
    # Creates a bar plot using Matplotlib
    teams = pivot_df["Tm"].to_numpy()
    positions = pivot_df.columns[1:]  # Exclude 'Tm'
    values = pivot_df.drop("Tm").to_numpy()

    fig, ax = plt.subplots(figsize=(14, 8))
    colors = plt.get_cmap("Set2").colors

    for i, pos in enumerate(positions):
        ax.bar(teams, values[:, i], label=pos, color=colors[i % len(colors)])

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=legend)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def aggregate_data(df):
    # Aggregates player data by position.
    grouped_data = df.group_by("Pos").agg(
        pl.col("PTS").sum().alias("Total_Points"),
        pl.col("Pos").count().alias("Player_Count"),
    )

    # Calculate the average points per player
    result = grouped_data.with_columns(
        (pl.col("Total_Points") / pl.col("Player_Count")).alias("avg_point_per_player")
    )
    # Sort the result by position
    return result.sort("Pos")


def group_team_data(df):
    # Aggregates player data by position and team.
    grouped_multiple_data = df.group_by(["Pos", "Tm"]).agg(
        pl.col("PTS").sum().alias("Total_Points"),
        pl.col("Pos").count().alias("Player_Count"),
    )
    result = grouped_multiple_data.pivot(
        index="Tm", columns="Pos", values="Total_Points"
    ).fill_nan(0)

    return result.sort("Tm")


def save_to_markdown(df):
    """save summary report to markdown"""
    markdown_table1, markdown_table2 = generalise_data(df)
    markdown_table1 = str(markdown_table1)
    markdown_table2 = str(markdown_table2)
    # Write the markdown table to a file
    with open("summary_report.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("Median:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line


# use the above functions to generate results:

# Load the NBA data
nba_data_file = read_csv_file("2023-2024 NBA Player Stats - Regular.csv")

# Describe statistics for the 'Age' column
data_summary, median_table = generalise_data(nba_data_file)
print("Median")
print(median_table)
print("Summary")
print(data_summary)

grouped_data = aggregate_data(nba_data_file)

# Grouped data for team stats by position
pivot_df = group_team_data(nba_data_file)

# Visualizations
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

save_to_markdown(nba_data_file)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
