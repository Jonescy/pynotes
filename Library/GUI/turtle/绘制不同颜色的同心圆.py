import turtle

t = turtle.Pen()

my_colors = ("red", "yellow", "green", "black")

t.width(4)
t.speed(5)
for i in range(5):
    t.penup()
    t.goto(0, -i*10)
    t.pendown()
    t.color(my_colors[i % len(my_colors)])
    t.circle(30+i*10)

turtle.done()

