import turtle


def bottom_left(monk: turtle.Turtle, size):
    jianju.penup()
    jianju.backward(size)
    jianju.right(90)
    jianju.forward(size)
    jianju.left(90)
    jianju.pendown()


def square_curl(monk: turtle.Turtle, size, direction=1, depth=8):
    starting_position = monk.position()
    starting_heading = monk.heading()

    for i in range(depth):
        monk.right(direction * 90)
        size -= 2
        monk.forward(size)

    monk.penup()
    monk.setposition(starting_position)
    monk.setheading(starting_heading)
    monk.pendown()


jianju = turtle.Turtle()
screen = turtle.Screen()

jianju.speed(0)

element_length = 25
direction = 1
bottom_left(jianju, element_length)
for square in range(1, 5):
    for _ in range(4):
        for _ in range(2 ** square):
            jianju.forward(element_length)
            square_curl(jianju, element_length - 1, 4/3)
        jianju.left(90)
    bottom_left(jianju, element_length * 2 ** (square - 1))

screen.exitonclick()
