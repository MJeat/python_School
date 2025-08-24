import turtle
from random import randint

# Set turtle speed to slowest
turtle.speed(1)

# Draw 16-by-16 lattice
turtle.color("gray")  # Color for lattice

# Draw horizontal lines
for y in range(-80, 81, 10):
    turtle.penup()
    turtle.goto(-80, y)  # Move to the start of the line
    turtle.pendown()
    turtle.forward(160)

# Draw vertical lines
turtle.right(90)
for x in range(-80, 81, 10):
    turtle.penup()
    turtle.goto(x, 80)  # Move to the start of the line
    turtle.pendown()
    turtle.forward(160)

# Set pen size and color for the random walk
turtle.pensize(3)
turtle.color("red")

# Start the random walk at the center of the lattice
turtle.penup()
turtle.goto(0, 0)  # Go to the center
turtle.pendown()

# Initialize current pen location at the center of lattice
x = y = 0  
while abs(x) < 80 and abs(y) < 80:
    r = randint(0, 3)  # Random direction

    if r == 0:
        x += 10  # Walk right
        turtle.setheading(0)
    elif r == 1:
        y -= 10  # Walk down
        turtle.setheading(270)
    elif r == 2:
        x -= 10  # Walk left
        turtle.setheading(180)
    elif r == 3:
        y += 10  # Walk up
        turtle.setheading(90)

    turtle.forward(10)  # Move forward

turtle.done()  # Finish the drawing
# it will stops if the cursor hits the border