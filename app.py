import turtle
import random

window_length = 500
window_height = 500

turtles = 8

turtle.screensize(window_length, window_height)


class TurtleRacer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def start_game():
    turtle_list = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
    start = -(window_length / 2) + 20

    for t in range(turtles):
        new_pos_x = start + t * (window_length) // turtles
        turtle_list.append( TurtleRacer( colors[t], ( new_pos_x, -230 ) ) )
        turtle_list[t].turt.showturtle()

start_game()
