from turtle import Turtle


class Score(Turtle):
    def __init__(self, position, name):
        super().__init__()
        self.position = position
        self.name = name
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(self.position)
        self.color("white")
    
    def increase_score(self):
        self.score = self.score + 1
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align= 'center', font=('Arial', 15))

    def won(self):
        self.goto(0, 0)
        self.write(f"{self.name} won the game", align= 'center', font=('Cambria', 20))
    
    