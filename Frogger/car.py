from turtle import Turtle


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()

    def move(self, distance):
        self.forward(distance)

    def set_location(self, x, y):
        self.goto(x, y)


