from paddle import Paddle
from turtle import Screen
from ball import Ball
from score_board import Score_board
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("punk")
screen.listen()
screen.tracer(0)
paddle1 = Paddle(360, 0)
paddle2 = Paddle(-360, 0)
ball = Ball()
score_board = Score_board()

screen.onkey(paddle1.mo_up, "Up")
screen.onkey(paddle1.mo_down, "Down")
screen.onkey(paddle2.mo_up, "w")
screen.onkey(paddle2.mo_down, "s")

is_game_on = True
s = 0
while is_game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()
    if ball.xcor() > 335 and paddle1.distance(ball) < 50 or ball.xcor() < -335 and paddle2.distance(ball) < 50:
        ball.bouncex()
    if ball.xcor() > 390:
        ball.reset()
        score_board.scorel()
    if ball.xcor() < -390:
        ball.reset()
        score_board.scorer()

screen.exitonclick()