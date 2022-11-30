from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.i = randint(10, 20)
        self.j = randint(10, 20)
        self.b_speed = 0.0999

    def move(self):
        new_x = self.xcor() + self.i
        new_y = self.ycor() + self.j
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.j *= -1

    def bounce_x_mid(self):
        self.i *= -1
        self.j *= -1.001

    def bounce_x(self):
        self.i *= -0.999
        self.b_speed = 0.0995

    def bounce_x_edge(self):
        self.i *= -1.001
        self.b_speed *= 0.09975

    def res_pos(self):
        self.goto(0, 0)
        self.b_speed = 0.1
        self.bounce_x()
