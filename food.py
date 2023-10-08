from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.add_new_food()

    def add_new_food(self):
        self.clear()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
