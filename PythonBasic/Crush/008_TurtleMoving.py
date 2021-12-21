
import turtle
import math
wn = turtle.Screen()
imran = turtle.Turtle()

imran.forward(100)
imran.left(90)
imran.forward(100)
imran.left(45)
dist = math.sqrt(100*100/2)
imran.forward(dist)
imran.left(90)
imran.forward(dist)
imran.left(45)
imran.forward(100)

wn.exitonclick()