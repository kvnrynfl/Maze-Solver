import time
import datetime
import os
from maze_solver import dfs_all_paths, validate_maze, read_maze_from_module, visualize_paths, find_start_end

def main():
    maze = read_maze_from_module()

    try:
        validate_maze(maze)
        start, end = find_start_end(maze)
    except ValueError as e:
        print(f"Error: {e}")
        return

    start_time = time.time()

    all_paths = dfs_all_paths(maze, start, end)

    end_time = time.time()
    execution_time = end_time - start_time

    if all_paths:
        all_paths = sorted(all_paths, key=len)

        visualizations = visualize_paths(all_paths, maze)
        output = ""
        for index, visualization in enumerate(visualizations, start=1):
            path = all_paths[index - 1]
            distance = len(path) - 1
            coordinates = path
            
            output += f"Path {index}:\n"
            output += f"Distance: {distance}\n"
            output += f"Coordinates: {coordinates}\n"
            output += "Maze with path:\n"
            output += visualization + "\n"
            output += "\n" + "-" * 20 + "\n"
        
        print(f"Execution time: {execution_time:.4f} seconds")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/{timestamp}.txt"

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(output)
    else:
        print("No path found")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/{timestamp}.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            file.write("No path found")

if __name__ == "__main__":
    main()
