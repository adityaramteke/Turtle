import turtle
nice = turtle.Pen()
for x in range(273):
    nice.pencolor('#4c4c4c')
    nice.speed(0)
    nice.fd(x*2)
    nice.lt(120 + 1)
turtle.mainloop()
