from turtle import Turtle

ALIGNMENT = 'CENTER'
FONT = ('Courier', 25, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def increase_l_score(self):
        self.l_score += 1
        self.write_score()

    def increase_r_score(self):
        self.r_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(100, 330)
        self.write(f"{self.r_score}", align='center', font=FONT, move=False)
        self.goto(-100, 330)
        self.write(f"{self.l_score}", align='center', font=FONT, move=False)
