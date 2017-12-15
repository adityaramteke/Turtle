import turtle
import time
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.speed(0)
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.fd(x)
    t.lt(59)
turtle.mainloop()
