

# We use these codes in the 'write' to know or identify the letter based on the code itself


import turtle
turtle.write('\u1780 \u1782')
# turtle.done()

# Draw triangle:

turtle.pensize(4)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps=3)
turtle.end_fill()


# Draw diamond:

turtle.pensize(4)
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.color("black")
turtle.circle(40, steps=4)

# Draw hexagon:

turtle.pensize(4)
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.color("green")
turtle.circle(40, steps=5)

# Draw circle:

turtle.pensize(4)
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.color("blue")
turtle.circle(40, steps=80) # just increase the steps and ull get a circle

turtle.done() #This is like print, but for turtle

