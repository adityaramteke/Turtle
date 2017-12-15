import turtle
nice = turtle.Pen()
turtle.bgcolor("black")
for x in range(273):
    nice.pencolor('white')
    nice.speed(0)
    nice.fd(x*2)
    nice.lt(120 + 1)
turtle.mainloop()
