from turtle import  Screen
from snake import  Snake
from food import Food

from scoreboard import scoreBoard
import time
# from tkinter import PhotoImage

s = Screen()
s.title("My Snake World")
s.bgcolor("Black")
# img = PhotoImage(file='Bnab5y.jpg')
# s.bgpic(img)

# mit.pensize(19)
s.setup(width=800, height=600)

snake = Snake()
food = Food()
score = scoreBoard()


s.listen()
s.onkey(fun=snake.up, key="Up")
s.onkey(fun=snake.left, key="Left")
s.onkey(fun=snake.right, key='Right')
s.onkey(fun=snake.down,key='Down')

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.4)
    snake.move()
    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increaseScore()

    #collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.gameOver()

    #collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on =  False
            score.gameOver()
s.exitonclick()
