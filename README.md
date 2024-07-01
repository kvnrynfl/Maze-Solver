# MazeSolver

**MazeSolver** is a Python program designed to find and display all possible paths from a start point ('S') to an end point ('E') in a given maze using Depth-First Search (DFS). The program marks paths with line and corner symbols for clear visualization. It takes maze input as a 2D array, prints the results in a neat table format, and saves the output to a UTF-8 encoded file.

## Features
- **Find All Paths**: Uses DFS to explore all possible paths from start to end.
- **Clear Visualization**: Marks discovered paths with line and corner symbols for easy tracing.
- **Flexible Input**: Accepts maze input in the form of a 2D array with 'S' for the start and 'E' for the end.
- **Neat Output**: Prints results in a table format using the `tabulate` library.
- **UTF-8 Encoded Output**: Saves results to a file with UTF-8 encoding for easy access and readability.

## Requirements
- Python 3.x
- `tabulate` library

You can install the required library using pip:
```sh
pip install tabulate
```

## Input Maze Format
The maze should be provided as a 2D array in a separate file (`maze_data.py`) with 'S' marking the start point and 'E' marking the end point. Walls are marked with '#', and open paths are marked with spaces (' ').

Example:
```python
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', 'E'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['S', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]
```

## Running the Program
1. Ensure the maze is correctly formatted in the `maze_data.py` file.
2. Run the `main.py` file:
```sh
python main.py
```

## How the Program Works
1. **Reading the Maze**: The program reads the maze from `maze_data.py`.
2. **Validation**: The maze is validated to ensure it has a start ('S') and an end ('E') and that all rows are of equal length.
3. **Finding Paths**: Using DFS, the program finds all possible paths from 'S' to 'E'.
4. **Visualizing Paths**: Each path is visualized using line and corner symbols.
5. **Output**: The results are printed in a table format and saved to a `maze_output.txt` file with UTF-8 encoding.

## Example Output
Here are some examples of what the output might look like:

### Path 1:
```
Distance: 21
Coordinates: [(0, 10), (0, 9), ..., (8, 0), (9, 0)]
Maze with path:
+---+---+---+---+---+---+---+---+---+---+
| # | # | # | # | # | # | # | # | ┌ | E |
+---+---+---+---+---+---+---+---+---+---+
| # |   |   |   |   |   |   | # | │ | # |
+---+---+---+---+---+---+---+---+---+---+
| # |   | # | # | # | # | ┌ | ─ | ┘ | # |
+---+---+---+---+---+---+---+---+---+---+
| # |   | # | ┌ | ─ | ─ | ┘ | # |   | # |
+---+---+---+---+---+---+---+---+---+---+
| # |   | # | │ | # | # | # |   | # | # |
+---+---+---+---+---+---+---+---+---+---+
| # |   |   | └ | ┐ | # |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+
| # | # | # | # | │ | # |   | # | # | # |
+---+---+---+---+---+---+---+---+---+---+
| # | ┌ | ─ | ─ | ┘ | # |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+
| # | │ | # | # | # | # |   | # |   | # |
+---+---+---+---+---+---+---+---+---+---+
| ┌ | ┘ |   |   |   |   |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+
| S | # | # | # | # | # | # | # | # | # |
+---+---+---+---+---+---+---+---+---+---+
```

### Path 2:
```
Distance: 27
Coordinates: [(0, 10), (0, 9), ..., (8, 0), (9, 0)]
Maze with path:
+---+---+---+---+---+---+---+---+---+---+
| # | # | # | # | # | # | # | # | ┌ | E |
+---+---+---+---+---+---+---+---+---+---+
| # | ┌ | ─ | ─ | ─ | ─ | ┐ | # | │ | # |
+---+---+---+---+---+---+---+---+---+---+
| # | │ | # | # | # | # | └ | ─ | ┘ | # |
+---+---+---+---+---+---+---+---+---+---+
| # | │ | # |   |   |   |   | # |   | # |
+---+---+---+---+---+---+---+---+---+---+
| # | │ | # |   | # | # | # |   | # | # |
+---+---+---+---+---+---+---+---+---+---+
| # | └ | ─ | ─ | ┐ | # |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+
| # | # | # | # | │ | # |   | # | # | # |
+---+---+---+---+---+---+---+---+---+---+
| # | ┌ | ─ | ─ | ┘ | # |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+
| # | │ | # | # | # | # |   | # |   | # |
+---+---+---+---+---+---+---+---+---+---+
| ┌ | ┘ |   |   |   |   |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+
| S | # | # | # | # | # | # | # | # | # |
+---+---+---+---+---+---+---+---+---+---+
```

## File Structure
```
MazeSolver/
│
├── maze_data.py        # Contains the maze input as a 2D array
├── maze_solver.py      # Contains the main logic for solving the maze
├── main.py             # Entry point for running the program
└── README.md           # This file
```
