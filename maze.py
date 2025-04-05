from cells import Cell
from time import sleep
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width = None, cell_height = None, window = None, seed = None, animate_draw = True, animate_solve = True):
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
        
        if seed is None:
            random.seed()
        else:
            random.seed(seed)
        
        self.__seed = seed
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__x1 = x1
        self.__y1 = y1
        self.__animate_draw = animate_draw
        self.__animate_solve = animate_solve
        self.end_found_for_bfs = False
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
                    if self.__animate_draw:
                        self._animate()
                rows.append(cell)
        
            self.__cells.append(rows)
        self._create_entrance_and_exit()

    def _create_entrance_and_exit(self):
        entrance_cell = self.__cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.is_start = True
        if self.__window is not None:
            entrance_cell.draw()
            if self.__animate_draw:
                self._animate()
        exit_cell = self.__cells[self.__num_rows - 1][self.__num_cols - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.is_end = True
        if self.__window is not None:
            exit_cell.draw()
            if self.__animate_draw:
                self._animate()
        self._create_maze_path()
        self._reset_visited()

    def _create_maze_path(self, x = 0, y = 0):
        self.__cells[y][x].visited = True
        while True:
            to_vist = []
            if y > 0 and not self.__cells[y - 1][x].visited:
                to_vist.append((x, y - 1))
            if y < self.__num_rows - 1 and not self.__cells[y + 1][x].visited:
                to_vist.append((x, y + 1))
            if x > 0 and not self.__cells[y][x - 1].visited:
                to_vist.append((x - 1, y))
            if x < self.__num_cols - 1 and not self.__cells[y][x + 1].visited:
                to_vist.append((x + 1, y))
            if len(to_vist) == 0:
                return
           
            next_cell = random.choice(to_vist)
            
            if next_cell[0] == x:
                if next_cell[1] < y:
                    self.__cells[y][x].has_top_wall = False
                    self.__cells[next_cell[1]][next_cell[0]].has_bottom_wall = False
                else:
                    self.__cells[y][x].has_bottom_wall = False
                    self.__cells[next_cell[1]][next_cell[0]].has_top_wall = False
            else:
                if next_cell[0] < x:
                    self.__cells[y][x].has_left_wall = False
                    self.__cells[next_cell[1]][next_cell[0]].has_right_wall = False
                else:
                    self.__cells[y][x].has_right_wall = False
                    self.__cells[next_cell[1]][next_cell[0]].has_left_wall = False

            if self.__window is not None:
                self.__cells[y][x].draw()
                self.__cells[next_cell[1]][next_cell[0]].draw()
                if self.__animate_draw:
                    self._animate()

            self._create_maze_path(next_cell[0], next_cell[1])


    def solve(self, method = "dfs"):
        method = method.lower()
        if method == "bfs":
            to_vist = [(0,0)]
            result = self._solve_recursive_bfs(to_vist)
            self.end_found_for_bfs = False
            return result
        elif method == "dfs":
            return self._solve_recursive_dfs()
        else:
            raise ValueError("method must be either BFS or DFS")
        

    def _solve_recursive_dfs(self, x = 0, y = 0):
        current_cell = self.__cells[y][x]
        if current_cell.is_end:
            return True
        current_cell.visited = True
        while True:
            to_vist = []
            if y > 0 and not self.__cells[y - 1][x].visited and not self.__cells[y - 1][x].has_bottom_wall:
                to_vist.append((x, y - 1))
            if y < self.__num_rows - 1 and not self.__cells[y + 1][x].visited and not self.__cells[y + 1][x].has_top_wall:
                to_vist.append((x, y + 1))
            if x > 0 and not self.__cells[y][x - 1].visited and not self.__cells[y][x - 1].has_right_wall:
                to_vist.append((x - 1, y))
            if x < self.__num_cols - 1 and not self.__cells[y][x + 1].visited and not self.__cells[y][x + 1].has_left_wall:
                to_vist.append((x + 1, y))
            if len(to_vist) == 0:       
                return False
            
            next_cell = random.choice(to_vist)


            found_end = self._solve_recursive_dfs(next_cell[0], next_cell[1])

            if self.__window is not None:
                if found_end:
                    self.__cells[y][x].draw_move(self.__cells[next_cell[1]][next_cell[0]])
                    if self.__animate_solve:
                        self._animate()
                    return True
            
                self.__cells[y][x].draw_move(self.__cells[next_cell[1]][next_cell[0]], undo=True)
                if self.__animate_solve:
                    self._animate()
    
    def _solve_recursive_bfs(self , to_vist, x = 0, y = 0):
        if self.__cells[y][x].is_end:
            self.end_found_for_bfs = True
            return True
        self.__cells[y][x].visited = True

     
        temp_to_vist = []
        if y > 0 and not self.__cells[y - 1][x].visited and not self.__cells[y - 1][x].has_bottom_wall:
            temp_to_vist.append((x, y - 1))
        if y < self.__num_rows - 1 and not self.__cells[y + 1][x].visited and not self.__cells[y + 1][x].has_top_wall:
            temp_to_vist.append((x, y + 1))
        if x > 0 and not self.__cells[y][x - 1].visited and not self.__cells[y][x - 1].has_right_wall:
            temp_to_vist.append((x - 1, y))
        if x < self.__num_cols - 1 and not self.__cells[y][x + 1].visited and not self.__cells[y][x + 1].has_left_wall:
            temp_to_vist.append((x + 1, y))
        if len(temp_to_vist) == 0:       
            return False
        
        for cell in temp_to_vist:
            if self.__window is not None:
                self.__cells[y][x].draw_move(self.__cells[cell[1]][cell[0]])
                if self.__animate_solve:
                    self._animate()
        
        to_vist.extend(temp_to_vist)
        
        copy_to_vist = to_vist.copy()
        for cell in copy_to_vist:
            if len(to_vist) == 0:
                return False
            if self.end_found_for_bfs:
                return True
            cell_to_vist = to_vist.pop(0)
            self._solve_recursive_bfs(to_vist, cell_to_vist[0], cell_to_vist[1])

             
    def _reset_visited(self):
        for row in self.__cells:
            for col in row:
                col.visited = False          
    
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