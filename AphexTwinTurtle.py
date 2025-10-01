import turtle
import time

#turtle.speed(0)    

def loop():
    turtle.color("black", "black")
    turtle.begin_fill()

    turtle.penup()
    turtle.setpos(0, -120)
    turtle.pendown()

    def draw(r):
        turtle.circle(r)

        turtle.penup()
        turtle.setpos(0, -r/15 -120)
        turtle.pendown()

    for i in range (2):
        draw(150 + 10 * i)

    time.sleep(0.2)
    turtle.end_fill()

    turtle.penup()
    turtle.setpos(100, 80-120)


    r1=10
    turtle.circle(r1, 110)

    turtle.pendown()

    turtle.color("black", "black")
    turtle.begin_fill()

    turtle.forward(140)

    r2=10
    turtle.circle(r2, 70)
    turtle.forward(145)

    r3=20
    turtle.circle(r3,180)
    turtle.forward(35)

    r4=25
    turtle.circle(r4,45)
    turtle.forward(20)

    r5=10
    turtle.circle(-r5, 170)
    turtle.forward(120)

    r6=14
    turtle.circle(r6, 175)
    turtle.forward(50)

    r7=20
    turtle.circle(-r7, 50)
    turtle.forward(5)

    r8=10
    turtle.circle(r8, 105)
    turtle.forward(15)

    r9=15
    turtle.circle(-r9, 161)
    turtle.forward(117)

    r10=11
    turtle.circle(r10, 163)
    turtle.forward(15)

    time.sleep(0.1)
    turtle.end_fill()

    time.sleep(2)

repetition = 1

while repetition == 1:
    turtle.hideturtle()

    loop()
    turtle.clear()
    turtle.reset()


turtle.done()
