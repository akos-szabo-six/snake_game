from email.contentmanager import get_and_fixup_unknown_message_content
from time import sleep
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_in_progress = True
while game_in_progress:
    screen.update()
    sleep(0.2)
    for segment_number in range(len(segments) - 1, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number - 1].ycor()
        segments[segment_number].goto(new_x, new_y)
    segments[0].forward(20)
















screen.exitonclick()