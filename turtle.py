import turtle
j = turtle.Turtle()
j.color('blue')
j.shape('turtle')

d = turtle.Turtle()
d.color('yellow')
d.shape('turtle')

f = turtle.Turtle()
f.color('red')
f.shape('turtle')

for i in range(360):
    j.forward(1)
    j.left(1)

for i in range(4):
    d.forward(100)
    d.left(90)

for i in range(3):
    f.left(120)
    f.forward(100)

turtle.done()