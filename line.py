from turtle import Turtle
LINE_POSITIONS = [(0, 380), (0, 300), (0, 220), (0, 140), (0, 60), (0, -20), (0, -100), (0, -180), (0, -260), (0, -340), (0, -420)]

class Line():
    def __init__(self):
        self.create_line()

    def create_line(self):
        for position in LINE_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.shapesize(stretch_len=0.3, stretch_wid=3)
            new_segment.penup()
            new_segment.goto(position)
