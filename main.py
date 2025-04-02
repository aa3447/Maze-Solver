from window import Windows
from maze import Maze
import random

def main():
    window = Windows(800, 800)
    maze_rows = 5
    maze_cols = 5
    maze_x_offset = 0
    maze_y_offset = 0
    cell_width = None
    cell_height = None
    seed = None
    Maze(maze_x_offset, maze_y_offset, maze_rows, maze_cols, cell_width, cell_height, window,seed)
    window.wait_for_close()

if __name__ == "__main__":
    main()