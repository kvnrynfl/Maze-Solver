from tabulate import tabulate

def dfs_all_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    all_paths = []

    def dfs(current, path):
        if current == end:
            all_paths.append(path)
            return
        
        for direction in directions:
            next_col, next_row = current[0] + direction[0], current[1] + direction[1]
            next_pos = (next_col, next_row)
            if 0 <= next_col < cols and 0 <= next_row < rows and maze[next_row][next_col] in [' ', 'E'] and next_pos not in path:
                dfs(next_pos, path + [next_pos])

    dfs(start, [start])
    return all_paths

def get_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]
    symbols = {
        (1, 0): '─',  # right
        (-1, 0): '─', # left
        (0, 1): '│',  # down
        (0, -1): '│'  # up
    }
    corners = {
        ((1, 0), (0, 1)): '┐',  # right to down
        ((1, 0), (0, -1)): '┘', # right to up
        ((-1, 0), (0, 1)): '┌', # left to down
        ((-1, 0), (0, -1)): '└', # left to up
        ((0, 1), (1, 0)): '└',  # down to right
        ((0, 1), (-1, 0)): '┘', # down to left
        ((0, -1), (1, 0)): '┌', # up to right
        ((0, -1), (-1, 0)): '┐'  # up to left
    }
    for i in range(1, len(path) - 1):
        prev_col, prev_row = path[i-1]
        col, row = path[i]
        next_col, next_row = path[i+1]
        prev_direction = (col - prev_col, row - prev_row)
        next_direction = (next_col - col, next_row - row)
        if (prev_direction, next_direction) in corners:
            maze_copy[row][col] = corners[(prev_direction, next_direction)]
        else:
            maze_copy[row][col] = symbols[prev_direction]
    return maze_copy

def print_maze_with_path(maze_with_path):
    return tabulate(maze_with_path, tablefmt="grid")

def validate_maze(maze):
    if not maze:
        raise ValueError("Maze cannot be empty")
    row_length = len(maze[0])
    for row in maze:
        if len(row) != row_length:
            raise ValueError("All rows in the maze must be the same length")
        for cell in row:
            if cell not in [' ', '#', 'S', 'E']:
                raise ValueError("Maze can only contain ' ', '#', 'S', and 'E'")

def find_start_end(maze):
    start, end = None, None
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 'S':
                start = (col_idx, row_idx)
            elif cell == 'E':
                end = (col_idx, row_idx)
    if start is None or end is None:
        raise ValueError("Maze must have a start point 'S' and an end point 'E'")
    return start, end

def read_maze_from_module():
    import maze_data
    return maze_data.maze

def visualize_paths(all_paths, maze):
    visualizations = []
    for path in all_paths:
        maze_with_path = get_maze_with_path(maze, path)
        visualizations.append(print_maze_with_path(maze_with_path))
    return visualizations
