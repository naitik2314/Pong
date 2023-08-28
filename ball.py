import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.change_y = 10
        self.change_x = 10
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + self.change_x
        new_y = self.ycor() + self.change_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.change_y = self.change_y * -1

    def bounce_x(self):
        self.change_x = self.change_x * -1
    
    def ball_reset_position(self):
        self.goto(9, 0)
