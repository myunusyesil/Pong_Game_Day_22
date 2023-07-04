from turtle import Screen
from pongscreen import Pongscreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

DISTANCE_FROM_PADDLE = 50

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.tracer(0)

# Create screen and draw centerline
pongscreen = Pongscreen()
ball = Ball()
left_paddle = Paddle((-560, 0))
right_paddle = Paddle((560, 0))

scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

is_on = True

vx = 5
vy = 5

while is_on:
    screen.update()
    time.sleep(0.012)
    ball.move(vx, vy)

    # Detect collisions with wall
    if ball.ycor() < -380 or ball.ycor() > 380:
        print("collision")
        vy *= -1

    # Detect collisions with l_paddle
    if ball.distance(left_paddle) < DISTANCE_FROM_PADDLE and ball.xcor() < -550:
        random_velocity = random.random()
        vx *= -1

    elif ball.distance(right_paddle) < DISTANCE_FROM_PADDLE and ball.xcor() > 550:
        vx *= -1

    # Detect when paddles miss the ball
    if ball.xcor() > 620:
        scoreboard.increase_l_score()
        ball.goto(0, 0)
        vx *= -1
    elif ball.xcor() < -620:
        scoreboard.increase_r_score()
        ball.goto(0, 0)
        vx *= -1

screen.exitonclick()
