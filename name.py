from turtle import Turtle


class Name(Turtle):
    def __init__(self, name, position):
        super().__init__()
        self.position = position
        self.name = name
        self.hideturtle()
        self.penup()
        self.color("white")
        self.player_type(name, position)

    def player_type(self, name, position):
        self.goto(self.position)
        self.write(f"{self.name}", align= 'center', font=('Cambria', 18))
