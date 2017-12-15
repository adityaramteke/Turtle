import turtle
import random

def go(heading, step_size):
    turtle.setheading(heading)
    turtle.forward(step_size)

def random_walk(step_size, steps):
    # Assumes turtle.mode('standard')
    DIRECTIONS = (EAST, NORTH, WEST, SOUTH) = (0, 90, 180, 270)
    for _ in range(steps):
        go(random.choice(DIRECTIONS), step_size)

if __name__ == '__main__':
    turtle.hideturtle()
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.speed(0)
    random_walk(10, 10000)
    turtle.done()
