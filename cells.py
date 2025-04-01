from points import Point
from lines import Line

class Cell:
    def __init__(self, x1, y1, x2, y2, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_wall_list = [self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall]
        # top left corner 
        self.__x1 = x1
        self.__y1 = y1
        
        # bottom right corner
        self.__x2 = x2
        self.__y2 = y2

        self.__center_x = (x1 + x2) // 2
        self.__center_y = (y1 + y2) // 2
        
        self.__window = window
    
    def draw(self , line_color = "blue"):
        lines = []

        line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        if self.has_left_wall:
            lines.append((line, line_color))
        else:
            lines.append((line, "white"))
        
        line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        if self.has_right_wall:
            lines.append((line, line_color))
        else:
            lines.append((line, "white"))
        
        line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        if self.has_top_wall:
            lines.append((line, line_color))
        else:
            lines.append((line, "white"))

        line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        if self.has_bottom_wall:
            lines.append((line, line_color))
        else:
            lines.append((line, "white"))

        if self.__window is not None:
            for line in lines:
                self.__window.draw_line(line[0], line[1])


    def draw_move(self, other_cell, undo=False):
        if undo:
            line_color = "gray"
        else:
            line_color = "red"

        line = Line(Point(self.__center_x, self.__center_y), Point(other_cell.__center_x, other_cell.__center_y))
        self.__window.draw_line(line, line_color)
    
    def get_x1(self):
        return self.__x1
    
    def get_y1(self):
        return self.__y1
    
    def get_x2(self):
        return self.__x2
    
    def get_y2(self):
        return self.__y2
    