from turtle import Screen
from pongscreen import Pongscreen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.tracer(0)


pongscreen = Pongscreen()
left_paddle = Paddle()
left_paddle.goto(-560, 0)

right_paddle = Paddle()
right_paddle.goto(560, 0)

screen.listen()
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)


# Create screen and draw centerline

is_on = True
while is_on:
    screen.update()




screen.exitonclick()