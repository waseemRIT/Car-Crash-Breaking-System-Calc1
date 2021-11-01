from turtle import *


def go_to_start(car):
    car.penup()
    car.goto(-210, 0)
    car.pendown()


def case1_text(car):
    """ Types Case1 on Screen"""
    car.penup()
    car.goto(-280, 200)
    car.color("White")
    car.write("Case 1: ", font=("Arial", 32, 'normal', 'bold', 'italic', 'underline'))
    car.pendown()


def case2_text(car):
    """ Types Case2 on Screen"""
    car.reset()
    car.penup()
    car.goto(-280, 200)
    car.color("White")
    car.write("Case 2: ", font=("Arial", 32, 'normal', 'bold', 'italic', 'underline'))
    car.pendown()


def street(car):
    """ Draws the border of the street"""
    car.pencolor(0, 0, 0)
    car.left(90)
    car.forward(150)
    car.right(90)
    car.forward(450)
    car.right(90)
    car.forward(250)
    car.right(90)
    car.forward(450)
    car.right(90)
    car.forward(100)
    car.right(90)
    car.penup()
    car.forward(40)
    car.pendown()


def wall(car):
    """ Draws the wall that the car will hit!"""
    car.color("white")
    car.penup()
    car.forward(350)
    car.penup()
    car.left(90)
    car.forward(100)
    car.pendown()
    car.right(180)
    car.forward(150)


def starting_text(car):
    car.penup()
    car.goto(-280, -200)
    car.write("Press Any Key To Start the Test: ", font=("Arial", 16, 'normal', 'bold', 'italic', 'underline'))
    car.pendown()


def car1(IMAGE):
    screen = Screen()
    screen.register_shape(IMAGE)
    car = Turtle()
    car.speed(0)
    car.shape(IMAGE)
    screen.colormode(255)
    screen.bgcolor(112, 120, 100)
    screen.title("Case 1 ")
    case1_text(car)
    go_to_start(car)
    street(car)
    wall(car)
    go_to_start(car)
    car.penup()
    car.left(90)
    car.forward(40)
    car.pendown()

    starting_text(car)
    go_to_start(car)
    car.penup()

    car.forward(40)
    car.pendown()

    start = input("Press Any Key To Start the Test: ")

    # Now stop before the wall
    car.speed(1)
    car.penup()
    car.forward(325)
    car.pendown()


def main():
    IMAGE = "car\car-2-icon-48.gif"
    car1(IMAGE)


if __name__ == '__main__':
    main()
