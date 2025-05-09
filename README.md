# NBA Analysis
This repository contains an analysis of NBA players' data from every season since 1947. The dataset and analyses are organized into directories as follows. The analyses leverage the MapReduce programming model and are prepared to be used with Hadoop Streaming.

## Dataset
- **`dataset/`**: Contains the dataset with NBA players' data, including statistics for every season since 1947.

## Analyses
1. **`average_stats/`**: Analyzes the average statistics of players across seasons.
2. **`style_of_play/`**: Examines the style of play by focusing on three-point shots.
3. **`elite_players/`**: Identifies the number of elite players by analyzing their average points and assists.

## Analysis Structure
Each analysis directory contains the following files:
- **`mapper.py`**: The MapReduce mapper script.
- **`reducer.py`**: The MapReduce reducer script.
- **`output`**: The file containing the results of executing the MapReduce scripts with the dataset.
- **`graph.py`**: A Python script that uses Matplotlib to visualize the analysis results.

## How to Use
1. Clone the repository.
2. Navigate to the desired analysis directory.
3. Use the provided MapReduce scripts with Hadoop Streaming to perform the analysis.
4. Use the provided script (graph.py) to generate graphs to visualize the results.