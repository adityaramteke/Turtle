# turtle shape

import turtle
turtle.bgcolor("black")
t = turtle.Pen()
t.speed(0)
t.color('red')
for i in range(20):
    t.circle(i * 3, 180)
    t.rt(45)

turtle.mainloop()
