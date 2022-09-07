from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(self.x, self.y)

    def mo_up(self):
        position = self.ycor() + 20
        self.goto(self.x, position)

    def mo_down(self):
        position = self.ycor() - 20
        self.goto(self.x, position)









