from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move(self, x_dis, y_dis):
        self.goto((self.xcor() + x_dis), self.ycor() + y_dis)
