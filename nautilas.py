import turtle
size=1
turtle.bgcolor("black")
turtle.color("white")
turtle.speed(0)
for x in range(70):
    for _ in range(4):
          turtle.forward(size)
          turtle.right(90)
          size=size + 1
    turtle.right(10)
turtle.done()
