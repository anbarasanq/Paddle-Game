from turtle import Turtle


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right = 0
        self.left = 0
        self.updated_score()

    def updated_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"{self.right}", align="center", font=("Courier", 80, "normal"))
        self.goto(200, 200)
        self.write(f"{self.left}", align="center", font=("Courier", 80, "normal"))

    def scorel(self):
        self.right += 1
        self.updated_score()

    def scorer(self):
        self.left += 1
        self.updated_score()

