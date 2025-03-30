from cells import Cell
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, window = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows + 1
        self.__num_cols = num_cols + 1
        self.__cell_width = cell_width
        self.__cell_height = cell_height
        self.__window = window
        self.__cells = []
        self._create_cells()

    def _create_cells(self):
        for row in range(self.__num_rows):
            rows = []
            
            for col in range(self.__num_cols):
                cell = Cell(self.__x1 + col * self.__cell_width, 
                                self.__y1 + row * self.__cell_height,
                                self.__x1 + self.__cell_width,
                                self.__y1 + self.__cell_height,
                                self.__window)
                if self.__window is not None:
                    cell.draw()
                    self._animate()
                rows.append(cell)
        
            self.__cells.append(rows)

    def _animate(self):
        self.__window.redraw()
        sleep(0.05)