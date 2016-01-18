import turtle

def draw_square(some_turtle):
    for side in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_triangle(some_turtle):
    for side in range(1,4):
        some_turtle.forward(100)
        some_turtle.left(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.speed(1)
    brad.color("white")
    brad.shape("arrow")
    draw_square(brad)
    draw_circle(brad)
    draw_triangle(brad)
    window.exitonclick()

draw_art()