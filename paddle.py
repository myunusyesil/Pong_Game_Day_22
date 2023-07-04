from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LENGTH = 1


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.penup()
        self.goto(pos)
        self.score = 0

    def move_up(self):
        if self.ycor() < 380:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > - 380:
            self.goto(self.xcor(), self.ycor() - 20)



