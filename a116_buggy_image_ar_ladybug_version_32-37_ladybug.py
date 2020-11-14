import turtle as trtl

# The Big Head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# Legs From Spider Code But Instead With 6 Legs.
legs = 6
leg_len = 60
degree = 270 / legs
ladybug.pensize(5)
counter = 0

# Draw The Legs.

while (counter < legs):
  ladybug.goto(0,-35)
  ladybug.setheading((degree*counter)-45)
  if (counter >= 3):
      ladybug.setheading((degree*counter))
  ladybug.forward(leg_len)
  counter = counter + 1

# Main Body Part.
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# Determine Dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# Place Dots On Ladybug
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

# Finish Code.
ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
