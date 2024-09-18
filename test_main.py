"""
Test File
"""

from main_python import (
    read_csv_file,
    generalise_data,
    line_graph_visualisation,
    bar_graph_visualisation,
    aggregate_data,
    group_team_data,
)
import polars as pl
from io import StringIO
import matplotlib.pyplot as plt


def test_read_csv_file():
    csv_data = """col1;col2
                  10;20
                  30;40"""
    csv_file = StringIO(csv_data)

    result_df = read_csv_file(csv_file, delimiter=";")

    assert result_df.shape == (2, 2)
    assert result_df.columns == ["col1", "col2"]


def test_generalise_data():
    # Sample data with different column types
    csv_data = """A,B,C,D,E
                  xyz,4,hello,7,10.5
                  abc,5,world,8,11.5
                  lts,6,test,9,12.5"""

    df = pl.read_csv(StringIO(csv_data))
    description, median_values = generalise_data(df)

    assert (
        description.shape[0] == 9
    ), "Description should have 8 rows for each statistic."
    assert median_values["B"][0] == 5, "Expected median of column B to be 5"
    assert median_values["D"][0] == 8, "Expected median of column D to be 8"
    assert median_values["E"][0] == 11.5, "Expected median of column E to be 11.5"


def test_plot_line_graph():
    csv_data = """Pos;PTS
                  PG;25
                  SG;20
                  SF;22
                  PF;19
                  C;23"""
    test_df = pl.read_csv(StringIO(csv_data), separator=";")

    try:
        plt.figure()
        line_graph_visualisation(
            test_df,
            "Pos",
            "PTS",
            "Average Points by Position",
            "Player Position",
            "Average Points",
        )
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Plot failed: {e}")

    assert plot_success


def test_bar_graph_visualisation():
    csv_data = """Tm;PG;SG;SF;PF;C
                  TeamA;100;150;200;180;220
                  TeamB;90;120;160;170;210"""
    test_df = pl.read_csv(StringIO(csv_data), separator=";")

    pivot_df = test_df

    try:
        plt.figure()
        bar_graph_visualisation(
            pivot_df, "Test: Total Points by Team", "Team", "Total Points", "Position"
        )
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Plot failed: {e}")

    assert plot_success


def test_aggregate_data():
    data = {"Pos": ["F", "G", "F", "G", "F"], "PTS": [10, 20, 15, 25, 30]}
    df = pl.DataFrame(data)
    result = aggregate_data(df)
    assert result["Pos"].to_list() == ["F", "G"]
    assert result["Total_Points"].to_list() == [55, 45]
    assert result["Player_Count"].to_list() == [3, 2]
    assert result["avg_point_per_player"].to_list() == [55 / 3, 45 / 2]


def test_group_team_data():
    data_team = {
        "Pos": ["F", "G", "F", "G", "F"],
        "Tm": ["A", "A", "B", "B", "A"],
        "PTS": [10, 20, 15, 25, 30],
    }
    df_team = pl.DataFrame(data_team)
    result = group_team_data(df_team)

    assert result["Tm"].to_list() == ["A", "B"]
    assert result["F"].to_list() == [40, 15]
    assert result["G"].to_list() == [20, 25]


if __name__ == "__main__":
    test_read_csv_file()
    test_generalise_data()
    test_plot_line_graph()
    test_bar_graph_visualisation()
    test_aggregate_data()
    test_group_team_data()
