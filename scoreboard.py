from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def get_high_score():
    with open("data.txt") as data:
        high_score = int(data.read())
    return high_score


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update()

    def update_high_score(self):
        with open("data.txt", "w") as data:
            data.write(f"{self.score}")
        self.high_score = get_high_score()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.update_high_score()
            self.score = 0
        self.update()
