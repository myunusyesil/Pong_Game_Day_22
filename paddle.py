from turtle import Turtle

PADDLE_WIDTH = 4
PADDLE_LENGTH = 1


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.penup()

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        # print("move up")

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        # print("move down")

