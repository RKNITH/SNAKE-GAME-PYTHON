from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score =0
        with open("snake_data.txt", mode="r") as data:
            self.highest_score =int(data.read())

        self.color("green")
        self.pen()
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} highest:{self.highest_score}",align="center", font=("arial", 24, "bold"))


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard() 

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align="center", font=("arial", 24, "bold"))


    def reset_score(self):
     if self.score > self.highest_score:
        self.highest_score = self.score
        with open("snake_data.txt", mode="w") as data:
            data.write(f"{self.highest_score}")
     self.score = 0
     self.update_scoreboard()
