import turtle
import time

length_vertical = (int)(input("Enter the length of the vertical sides"))
length_horizontal = length_vertical*2
turtle.down()
turtle.color(0.0,1.0,0.0)
turtle.begin_fill()
for side in range(2):
    turtle.forward(length_vertical)
    turtle.left(90)
    turtle.forward(length_horizontal)
    turtle.left(90)
turtle.end_fill()
time.sleep(5)
time.bye()
