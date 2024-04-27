import turtle
turtle.bgcolor("black")
col = ('red', 'yellow', 'green', 'cyan', 'white', 'blue')
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(25)
for i in range(150):
    t.color(col[i % 6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)