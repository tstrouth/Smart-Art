import turtle
import random

def draw(iterations, angle):
    wn = turtle.Screen()
    color = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    b = turtle.Turtle()
    #b.hideturtle()
    b.ht()
    b.speed(0)
    #b.tracer(0,0)
    for i in range(1, iterations):
        b.color(random.choice(color))
        b.circle(10000000000//i)
        #b.end_fill()
        b.up()
        b.lt(angle)
        b.forward(i)
        b.begin_fill()
        #b.down()
    wn.exitonclick()


draw(5000, 270)
