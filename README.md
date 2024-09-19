# Vishesh_Gupta_IDS706_Week3
[![CI](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week3/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week3/actions/workflows/CI.yml)

This repository contains my work for **Week 3** of the IDS706 course, where the purpose of this project is to transform the previous project (Pandas descriptive statistics) into generating descriptive statistics on datasets using Polars.

## File Structure 
```
Vishesh_Gupta_Individual_Project_1/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   ├── workflows/CI.yml
├── .gitignore
├── Makefile
├── main_python.py             # Main Python script for data analysis
├── main_python_jp.ipynb        # Jupyter Notebook version of the analysis
├── pandas_main_python.py       # Alternative analysis using Pandas
├── test_main.py                # Test cases for validating the code
├── requirements.txt            # List of required packages for the project
├── 2023-2024 NBA Player Stats - Regular.csv  # Dataset used for analysis
├── bar_graph.png               # Bar graph visualization of NBA player stats
├── line_graph.png              # Line graph of trends in NBA player stats
```

## Project Overview

The module performs the following key tasks:

1. **Loading and Cleaning NBA Data:** The CSV file containing player stats is loaded using Polars, and basic cleaning and formatting are applied.
2. **Data Aggregation:** Player statistics are grouped by position and team, with the total points and average points per player calculated.
3. **Visualization:** The aggregated data is visualized using line and bar graphs to show the distribution of points per position and team.


## Functions Overview
1. read_csv_file: This function reads a CSV file containing NBA player stats using Polars. It supports custom encodings and delimiters.
2. generalise_data: Generates a summary of the dataset by providing descriptive statistics and the median values.
3. line_graph_visualisation: This function creates a line graph based on the selected columns.
4. bar_graph_visualisation: Creates a bar plot based on the aggregated data, showing team points broken down by player positions.
5. aggregate_data: Aggregates player data by position, calculating the total points and the average points per player.
6. group_team_data: Aggregates player data by position and team, then pivots the data to display total points scored by each team in different player positions.

## Results of make all

<img width="1125" alt="Screenshot 2024-09-19 at 12 07 08 AM" src="https://github.com/user-attachments/assets/fe7aa630-d51b-48bf-8e3e-455dc502ea9d">

## Summary stats showing the results for inputed dataset:

<img width="1091" alt="Screenshot 2024-09-19 at 12 04 39 AM" src="https://github.com/user-attachments/assets/bfbe987e-1583-4a12-b719-8623c16c16ce">


## Data Visualisation 

![Bar Graph for Data](bar_graph.png)

![Line Graph for Data](line_graph.png)

## Execution Time

The total execution time of the script is displayed at the end of the analysis, providing insights into performance for both main_python.py and pandas_main_python.py

<img width="578" alt="Screenshot 2024-09-19 at 7 45 38 AM" src="https://github.com/user-attachments/assets/887be272-fec7-4e49-ad14-79a6c91e2504">

Although Polars is generally faster than Pandas, the screenshot above shows a result that contradicts this expectation. After discussing this with Prof Gift, I I learned that benchmarking standards are not always rigid. For smaller projects, the performance results for Pandas and Polars might differ from the benchmarks due to how the code is written and executed. Therefore, we should consider that performances can vary based on specific implementation details rather than strictly adhering to general benchmarks.

