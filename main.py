from window import Windows
from maze import Maze
from perfomTime import MazePerfomTime


def main():
    #window = Windows(1400, 1400)
    window = None
    maze_rows = 40
    maze_cols = 40
    maze_x_offset = 0
    maze_y_offset = 0
    cell_width = 10
    cell_height = 10
    #cell_width = None
    #cell_height = None
    seed = None
    maze = Maze(maze_x_offset, maze_y_offset, maze_rows, maze_cols, cell_width, cell_height, window,seed, animate_draw=False ,animate_solve=False)
    #maze.solve("dfs_recursive")
    timer = MazePerfomTime(maze)
    #print(timer.measure_single_solve_time("bfs_iterative"))
    #print(timer.measure_single_solve_time("dfs_iterative"))
    print(timer.measure_multiple_solve_time("bfs_iterative", 100))
    print(timer.measure_multiple_solve_time("dfs_iterative", 100))
    #maze.solve("bfs_iterative")

    #window.wait_for_close()

if __name__ == "__main__":
    main()