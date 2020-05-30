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

    run = True
    while run:
        for t in turtle_list:
            t.move()

        winner = []
        max_distance = 0
        for t in turtle_list:
            if t.pos[1] > 230 and t.pos[1] > max_distance:
                max_distance = t.pos[1]
                winner = []
                winner.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == max_distance:
                max_distance = t.pos[1]
                winner.append(t.color)

        if len(winner) > 0:
            run = False
            print('The winner is: ')
            for win in winner:
                print(win)

start_game()
