from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.my_turtles = []
        self.create_snake()
        self.head = self.my_turtles[0]

    def create_snake(self):
        for position in START_POSITION:
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(position)
            self.my_turtles.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.my_turtles) - 1, 0, -1):
            new_x = self.my_turtles[seg_num - 1].xcor()
            new_y = self.my_turtles[seg_num - 1].ycor()
            self.my_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.my_turtles[0].setheading(RIGHT)
