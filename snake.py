STARTING_POINT =[(0, 0), (-20, 0), (-40, 0)]
UP =90
DOWN =270
LEFT =180
RIGHT =0

from turtle import Turtle 
class Snake(Turtle):
    def __init__(self):
        super().__init__()

        self.segment =[]
        self.create_snake()
        self.head =self.segment[0]


    def create_snake(self):
        for position in STARTING_POINT:
            self.add_segments(position)

    
    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)

        self.segment.clear()
        self.create_snake()
        self.head =self.segment[0]    




    def add_segments(self, position):
        new_segment =Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segments(self.segment[-1].position())    

        
    def move(self):
        for seg in range(len(self.segment) -1, 0, -1):
            new_x =self.segment[seg -1].xcor()
            new_y =self.segment[seg -1].ycor()

            self.segment[seg].goto(new_x, new_y)

        self.segment[0].forward(20)        




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)    

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270) 

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)  

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)    

