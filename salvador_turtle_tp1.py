#Game: Drawing
#Instructions: W to move forward, A to change direction to left, D to turn direction to right
#R to reset, 1 to draw a circle, 2 to draw a square, 3 to change bg to blue
#4 to change bg to black
#Have fun
import turtle

dr = turtle.Screen()
dr.title("Drawing")
dr.bgcolor("black")

# pointer
point = turtle.Turtle()
point.color("white")
point.goto(0,0)

# forward
def move():
    point.forward(50)

#left
def goleft():
   point.left(90)

#right
def goright():
    point.right(90)


#reset
def clear():
    point.clear()
    point.penup()
    point.goto(0,0)
    point.pendown()
#circle
def circle():
     point.circle(50)
    

#square
def square():
   point.fd(100)
   point.rt(90)
   point.fd(100)
   point.rt(90)
   point.fd(100)
   point.rt(90)
   point.fd(100)

#change bg blue
def bg1():
    dr.bgcolor("blue")
#change bg black
def bg2():
    dr.bgcolor("black")
#key bind
dr.listen()
dr.onkeypress(move, "w")
dr.onkeypress(goleft, "a")
dr.onkeypress(goright, "d")
dr.onkeypress(clear, "r")
dr.onkeypress(circle, "1")
dr.onkeypress(square, "2")
dr.onkeypress(bg1, "3")
dr.onkeypress(bg2, "4")

