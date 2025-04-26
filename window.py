import tkinter
from tkinter import Tk, BOTH, Canvas

class Windows:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root_widget = Tk()
        self.__root_widget.title("Window")
        self.__canvas = Canvas(self.__root_widget, width=self.__width, height=self.__height, bg="black")
        self.__canvas.pack(anchor=tkinter.CENTER, expand=True)
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.__is_running = False
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def close(self):
        self.__is_running = False

    def draw_line(self, line, line_color):
        line.draw(self.__canvas,line_color)

    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_canvas(self):
        return self.__canvas
        