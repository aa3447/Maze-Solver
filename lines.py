
class Line():
    def __init__(self, point_one, point_two, tags=None ):
        self.point_one = point_one
        self.point_two = point_two
        self.tags = tags if tags is not None else []
    
    def draw(self, canvas, line_color):
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=line_color, width=2, tags=self.tags)

        