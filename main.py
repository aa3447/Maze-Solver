from window import Windows
from lines import Line
from points import Point

def main():
    window = Windows(800, 600)
    point_one = Point(100, 100)
    point_two = Point(400, 400)
    line_one = Line(point_one, point_two)
    point_three = Point(400, 100)
    point_four = Point(100, 400)
    line_two = Line(point_three, point_four)
    window.draw_line(line_one, "red")
    window.draw_line(line_two, "blue")
    window.wait_for_close()

if __name__ == "__main__":
    main()