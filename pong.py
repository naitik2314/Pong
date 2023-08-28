from turtle import Turtle

MOVE_DISTANCE = 25

class Pong(Turtle):
    
    def __init__(self, pong_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.speed(0)
        self.pong_position = pong_position
        self.create_pong()

    def create_pong(self):
        self.goto(self.pong_position)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < 350:
            self.setheading(90)
            self.forward(MOVE_DISTANCE)
    
    def move_down(self):
        if self.ycor() > -350:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)
