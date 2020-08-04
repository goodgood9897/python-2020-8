import turtle
j = turtle.Turtle()
j.penup()
j.shape('turtle')
j.color('blue')
step = 20

for i in range(60):
    j.forward(step)
    j.left(24)
    j.stamp()
    step = step + 3
    
turtle.done()