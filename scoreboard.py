from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.setpos(0,280)
        self.color("white")
        self.write(f"Score: {self.scores}",False,"center",("Courier",13,"bold"))

    def increase(self):
        self.scores += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scores} HighScore : {self.highscore}", False, "center", ("Arial", 13, "bold"))
    def game0ver(self):
        if self.scores > self.highscore:
            self.highscore = self.scores
        self.hideturtle()
        self.setpos(0, 0)
        self.color("white")
        self.write(f"GAME OVER", False, "center", ("Times New Roman", 20, "bold"))

    def reset(self):

        if self.scores > self.highscore:
            self.highscore = self.scores
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.highscore}")
        self.scores = 0
        self.update_score()
















