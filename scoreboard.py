from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Times New Roman", 70, "bold"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Times New Roman", 70, "bold"))

    def p1_counter(self):
        self.p1_score += 1
        self.update()

    def p2_counter(self):
        self.p2_score += 1
        self.update()








