import turtle
def draw_circle(size):
    turtle.pencolor('red')
    turtle.circle(size)
    draw_circle(size)
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)



turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)

turtle.pencolor('red')
turtle.circle(30)


turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)
