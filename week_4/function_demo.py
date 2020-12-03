import turtle


def draw_polygon(drawing_turtle: turtle.Turtle, sides=4, size=25):

    for side in range(sides):
        drawing_turtle.forward(size)
        drawing_turtle.left(360 / sides)


nick = turtle.Turtle()
screen = turtle.Screen()

for no_sides in range(3, 12):
    draw_polygon(nick, no_sides, 10 * no_sides)

screen.exitonclick()
