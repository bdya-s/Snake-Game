from turtle import Turtle
CENTER = "center"
FONT = ("Courier", 16, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.high_score = 0
        self.color("white")
        self.update_score(0)

    def update_score(self, score):
        self.setposition(0, 270)
        self.clear()
        self.write(f"Score: {score}", align=CENTER, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game over!", align=CENTER, font=FONT)