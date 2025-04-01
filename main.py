from window import Windows
from lines import Line
from points import Point
from cells import Cell
from maze import Maze

def main():
    window = Windows(800, 800)
    maze_rows = 5
    maze_cols = 5
    maze_x_offset = 50
    maze_y_offset = 50
    cell_width = None
    cell_height = 100
    Maze(maze_x_offset, maze_y_offset, maze_rows, maze_cols, cell_width, cell_height, window)
    window.wait_for_close()

if __name__ == "__main__":
    main()