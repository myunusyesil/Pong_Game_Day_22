from turtle import Turtle, Screen


class Pongscreen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.move = 0
        self.penup()
        self.goto(0, -400)
        self.pensize(5)
        self.pd = False
        self.center_line()

    def center_line(self):

        for y_pos in range(-400, 400, 20):
            self.pd = not self.pd
            if self.pd:
                self.pendown()
            else:
                self.penup()

            self.goto(0, y_pos)
