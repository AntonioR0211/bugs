#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
# The pensize makes a circle which is the spider body.
Spider.pensize(40)
Spider.circle(20)
Spider.goto(20,20)

#Create a spider head
Spider.goto(0,50)
Spider.circle(5)
# This displays how much legs will be there.
Leg = 8
y1 = 70
y2 = y1
leglength = 240 / Leg
print("leglength=", leglength)
Spider.pensize(5)
up = 0
# Tests for how many legs are given and draws however many amounts it is.
#Draw Legs
while (up < Leg):
    Spider.goto(0,20)
    Spider.setheading((leglength*up)-15)
    Spider.pd()
    if (up >= 4):
        Spider.setheading((leglength*up)-15)
        Spider.circle(100, 120)
    if (up < 4):
        Spider.circle(-100, 120)
    Spider.pu()
    up = up + 1

Spider.hideturtle()
# Eyes
Spider.penup()
Spider.goto(20,50)
Spider.pendown()
Spider.color("Red")
Spider.circle(0.1)
Spider.penup()
Spider.goto(-20,50)
Spider.pendown()
Spider.circle(0.1)
wn = trtl.Screen()
wn.mainloop()
