from turtle import Turtle
import turtle
MOVE_PACE = 20
UP = 90.0
DOWN = 270.0
RIGHT = 0.0
LEFT = 180.0

class Snake:
    def __init__(self):
        self.segments = []
        self.start_snake()
        self.head = self.segments[0]

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position_x, position_y):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.goto(position_x, position_y)
        new_snake.color("white")
        self.segments.append(new_snake)

    def start_snake(self):
        position = 0
        for loop in range(1, 4):
            self.add_segment(0, 0)
            position -= 20

    def extend(self):
        self.add_segment(self.segments[len(self.segments)-1].xcor(), self.segments[len(self.segments)-1].ycor())

    def move_snake(self):
        for idx in range(len(self.segments) -1, 0, -1):
            x_axis = self.segments[idx-1].xcor()
            y_axis = self.segments[idx-1].ycor()
            self.segments[idx].goto(x_axis, y_axis)
        self.head.fd(MOVE_PACE)

