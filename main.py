from window import Windows
from lines import Line
from points import Point
from cells import Cell
from maze import Maze

def main():
    window = Windows(800, 800)
    maze_rows = 5
    maze_cols = 10
    cell_width = window.get_width() // maze_cols
    cell_height = window.get_height() // maze_rows
    Maze(0, 0, maze_rows, maze_cols, cell_width, cell_height, window)
    window.wait_for_close()

if __name__ == "__main__":
    main()