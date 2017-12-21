import turtle

colors_one = ['red', 'yellow']
colors_two = ['yellow', 'red']

turtle.bgcolor("black")
screen = turtle.Screen()
screen.setup(800,600)

circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0,280)
circle.stamp()


def blinking(changed_color_one, changed_color_two):
    circle.goto(0,280)
    circle.color(changed_color_two)
    circle.stamp()
    k = 0
    for i in range(1, 17):
        y = 30*i
        for j in range(i-k):
            x = 30*j

        if i % 4 == 0:
            x =  30*(j+1)
            circle.color(changed_color_one)
            circle.goto(-x,-y+280)
            circle.stamp()
            circle.goto(x,-y+280)
            circle.stamp()
            k += 2

        if i % 4 == 3:
            x =  30*(j+1)
            circle.color(changed_color_two)
            circle.goto(-x,-y+280)
            circle.stamp()
            circle.goto(x,-y+280)
            circle.stamp()



k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()

    if i % 4 == 0:
        x =  30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()        
        k += 2

    if i % 4 == 3:
        x =  30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp() 

square.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):    
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()        

for h in range(100):
    blinking(colors_one[h%2], colors_two[h%2])

turtle.onclick()
