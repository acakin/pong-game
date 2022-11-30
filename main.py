import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
l = Turtle()
p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))
b = Ball((0, 0))
s = Scoreboard()

screen.listen()
screen.onkeypress(p1.up, "w")
screen.onkeypress(p1.down, "s")
screen.onkeypress(p2.up, "Up")
screen.onkeypress(p2.down, "Down")

l.color("white")
l.penup()
l.goto(0, -340)
l.setheading(90)
l.hideturtle()
for _ in range(12):
    l.forward(40)
    l.penup()
    l.forward(20)
    l.pendown()

game_is_on = True
while game_is_on:
    time.sleep(b.b_speed)
    screen.update()
    b.move()

    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()
        game_is_on = True

    if b.xcor() < -330 and b.distance(p1) < 25 or b.xcor() > 330 and b.distance(p2) < 25:
        b.bounce_x_mid()

    elif b.xcor() < -330 and b.distance(p1) < 50 or b.xcor() > 330 and b.distance(p2) < 50:
        b.bounce_x()

    elif b.xcor() < -330 and b.distance(p1) < 70 or b.xcor() > 330 and b.distance(p2) < 70:
        b.bounce_x_edge()

    if b.xcor() < -380:
        b.res_pos()
        s.p2_counter()

    if b.xcor() > 380:
        b.res_pos()
        s.p1_counter()

screen.exitonclick()
