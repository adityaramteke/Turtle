import turtle
heart = turtle.Pen()
window = turtle.Screen()

window.bgcolor("black")
def curvemove():
    for i in range(200):
        heart.rt(1)
        heart.fd(1)

heart.color('red')
heart.begin_fill()
heart.lt(140)
heart.fd(111.65)
curvemove()
heart.lt(120)
curvemove()
heart.fd(111.65)
heart.end_fill()
turtle.done()
