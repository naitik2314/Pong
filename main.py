import time
from turtle import Screen
from ball import Ball
from line import Line
from name import Name
from pong import Pong
from score import Score

#Setup the screen
screen = Screen() #We make an object named screen from the Screen class present in turtle
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Score limit
score_limit = screen.numinput("Points", "Enter the number of points you want to play game for", minval=3, maxval=30)
player_1 = screen.textinput("Players", "Name of the first player")
player_2 = screen.textinput("Players", "Name of the second player")

pong1 = Pong((-495, 0))
pong2 = Pong((490, 0))
line = Line()
player_1_write = Name(player_1, (-250, 370))
player_2_write = Name(player_2, (250, 370))
screen.update()
score1 = Score((-250, 340), player_1)
score2 = Score((250, 340), player_2)

screen.listen()
screen.onkeypress(pong1.move_up, "w")
screen.onkeypress(pong1.move_down, "s")
screen.onkeypress(pong2.move_up, "Up")
screen.onkeypress(pong2.move_down, "Down")

ball = Ball()

# score1.increase_score()
game_is_on = True
#To always keep the screen updated, as we are doing screen.tracer(0)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    #Detect collision with the wall
    if ball.ycor() > 390 or ball.ycor() < -390:
        ball.bounce_y()

    #Detect collision with the paddle
    if ball.distance(pong2) < 50 and ball.xcor() > 460 or ball.distance(pong1) < 50 and ball.xcor() < -460:
        ball.bounce_x()

    #Detect if the left paddle missed
    if ball.xcor() < -490:
        ball.ball_reset_position()
        score2.increase_score()
    
    #Detect if right paddle missed the ball
    if ball.xcor() > 490:
        ball.ball_reset_position()
        score1.increase_score()

    if score1.score == score_limit:
        score1.won()
        game_is_on = False
    
    elif score2.score == score_limit:
        score2.won()
        game_is_on = False


screen.exitonclick()
