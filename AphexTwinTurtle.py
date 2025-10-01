import turtle

turtle.hideturtle()

turtle.color("black", "black")
turtle.begin_fill()

def draw(r):
    turtle.circle(r)

    turtle.penup()
    turtle.setpos(0, -r/15)
    turtle.pendown()

for i in range (2):
    draw(150 + 10 * i)

turtle.end_fill()

turtle.penup()
turtle.setpos(90, 70)
turtle.pendown()

turtle.color("black", "black")
turtle.begin_fill()

r=10
turtle.circle(r, 110)
turtle.forward(140)

r=10
turtle.circle(r, 70)
turtle.forward(145)

r=20
turtle.circle(r,180)
turtle.forward(35)

r=25
turtle.circle(r,45)
turtle.forward(30)

r=10
turtle.circle(-r, 170)
turtle.forward(120)

r=14
turtle.circle(r, 175)
turtle.forward(50)

r=20
turtle.circle(-r, 50)
turtle.forward(5)

r=10
turtle.circle(r, 105)
turtle.forward(15)

r=15
turtle.circle(-r, 161)
turtle.forward(117)

turtle.end_fill()


turtle.done()