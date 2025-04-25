from window import Windows
from maze import Maze
from perfomTime import MazePerfomTime


def main():
    maze = maze_setup_with_window()
    #maze.solve("dfs_recursive")
    timer = MazePerfomTime(maze)
    #print(timer.measure_single_solve_time("bfs_iterative"))
    #print(timer.measure_single_solve_time("dfs_iterative"))
    #print(timer.measure_multiple_solve_time("bfs_iterative", 100))
    #print(timer.measure_multiple_solve_time("dfs_iterative", 100))
    maze.solve("bfs_iterative")

    maze.get_window().wait_for_close()

def maze_setup_with_window(seed = None):
    window = Windows(1400, 1400)
    maze_rows = 100
    maze_cols = 100
    maze_x_offset = 0
    maze_y_offset = 0
    cell_width = None
    cell_height = None

    return Maze(maze_x_offset, maze_y_offset, maze_rows, maze_cols, cell_width, cell_height, window,seed,animate_draw=False, animate_solve=False)

def maze_setup_no_window(seed = None):
    window = None
    maze_rows = 40
    maze_cols = 40
    maze_x_offset = 0
    maze_y_offset = 0
    cell_width = 10
    cell_height = 10

    return Maze(maze_x_offset, maze_y_offset, maze_rows, maze_cols, cell_width, cell_height, window,seed, animate_draw=False ,animate_solve=False)

if __name__ == "__main__":
    main()