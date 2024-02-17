from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segments = Turtle('square')
        new_segments.color('white')
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def left(self):
        if self.head != RIGHT:
            self.segments[0].setheading(LEFT)
    def up(self):
        if self.head != DOWN:
            self.segments[0].setheading(UP)
    def right(self):
        if self.head != LEFT:
            self.segments[0].setheading(RIGHT)
    def down(self):
        if self.head != UP:
            self.segments[0].setheading(DOWN)



