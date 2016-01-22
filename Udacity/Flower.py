__author__ = 'v_shabalin'

import turtle

window = turtle.Screen()
window.bgcolor("white")
brad = turtle.Turtle()
brad.speed(20)
brad.color("blue")
brad.shape("turtle")

def draw_flower(some_turtle):
    some_turtle.right(90)
    for item in range(36):
        some_turtle.forward(100)
        some_turtle.right(40)
        some_turtle.forward(100)
        some_turtle.right(140)
        some_turtle.forward(100)
        some_turtle.right(40)
        some_turtle.forward(100)
        some_turtle.right(140)
        some_turtle.right(10)
    some_turtle.forward(300)
    window.exitonclick()


def draw_star(some_turtle):
    for item in range(1,6):
        some_turtle.forward(100)
        some_turtle.right(144)
draw_flower(brad)