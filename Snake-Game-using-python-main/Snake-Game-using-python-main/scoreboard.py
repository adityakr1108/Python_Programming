from turtle import Turtle


class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setpos(0,280)
        self.hideturtle()
        self.updateScoreBoard()
        

    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", True, align = "center", font = ("Courier", 20, "italic"))

    def increaseScore(self):
        self.score +=1
        self.clear()
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER...{self.score}", align = "center",font  = ("Aerial", 25, "italic"))
        

