import random
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("Blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        food_x_cor = random.randint(-350,350)
        food_y_cor = random.randint(-280,280)
        self.goto(food_y_cor,food_y_cor)
       

   

        

