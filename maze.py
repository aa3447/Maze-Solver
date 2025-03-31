from cells import Cell
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width = None, cell_height = None, window = None):
        self.__window = window
        
        if window is not None:
            if x1 < 0 or x1 >= window.get_width():
                raise ValueError("x1 must be between 0 and window width")
            if y1 < 0 or y1 >= window.get_height():
                raise ValueError("y1 must be between 0 and window height")
            
            if cell_width is None:
                self.__cell_width = (window.get_width() - x1) // num_cols
            else:
                if cell_width <= 0:
                    raise ValueError("cell_width must be above 0")
                self.__cell_width = cell_width
            
            if cell_height is None:
                self.__cell_height = (window.get_height() - y1) // num_rows
            else:
                if cell_height <= 0:
                    raise ValueError("cell_height must be above 0")
                self.__cell_height = cell_height
            
        else:
            if cell_width <= 0 or cell_height <= 0:
                raise ValueError("cell_width and cell_height must be above 0")
            if x1 < 0:
                raise ValueError("x1 must be above 0")
            if y1 < 0:
                raise ValueError("y1 must be above 0")
            self.__cell_width = cell_width
            self.__cell_height = cell_height
       
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError("num_rows and num_cols must be above 0")
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__x1 = x1
        self.__y1 = y1
        self.__cells = []
        self._create_cells()

    def _create_cells(self):
        for row in range(self.__num_rows):
            rows = []
            
            for col in range(self.__num_cols):
                cell = Cell(self.__x1 + col * self.__cell_width, 
                                self.__y1 + row * self.__cell_height,
                                self.__x1 + (col + 1) * self.__cell_width,
                                self.__y1 + (row + 1) * self.__cell_height,
                                self.__window)
                if self.__window is not None:
                    cell.draw()
                    self._animate()
                rows.append(cell)
        
            self.__cells.append(rows)

    def _animate(self):
        self.__window.redraw()
        sleep(0.05)

    def get_cells(self):
        return self.__cells
    
    def get_x1(self):
        return self.__x1
    
    def get_y1(self):
        return self.__y1
    
    def get_window(self):
        return self.__window