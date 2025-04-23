from window import Windows
from maze import Maze
import random

def main():
    window = Windows(1400, 1400)
    maze_rows = 30
    maze_cols = 30
    maze_x_offset = 0
    maze_y_offset = 0
    cell_width = None
    cell_height = None
    seed = None
    maze = Maze(maze_x_offset, maze_y_offset, maze_rows, maze_cols, cell_width, cell_height, window,seed, animate_draw=False)
    maze.solve("bfs_iterative")
    window.wait_for_close()

if __name__ == "__main__":
    main()