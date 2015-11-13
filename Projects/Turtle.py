import turtle
import time

turtle.down()
turtle.color(1.0, 0.0, 0.0) # all red, no green, no blue
turtle.begin_fill()
for side in range(4):
 turtle.forward(100)
 turtle.left(90)
turtle.end_fill()
time.sleep(5) # wait 5 seconds
turtle.bye() # close the turtle window
