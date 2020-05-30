import turtle

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
