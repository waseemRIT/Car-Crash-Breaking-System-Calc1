from turtle import *


def go_to_start(car):
    car.penup()
    car.goto(-210, 0)
    car.pendown()


def case1_text(car):
    car.penup()
    car.goto(-280, 200)
    car.color("White")
    car.write("Case 1: ", font=("Arial", 32, 'normal', 'bold', 'italic', 'underline'))
    car.pendown()


def case2_text(car):
    car.reset()
    car.penup()
    car.goto(-280, 200)
    car.color("White")
    car.write("Case 2: ", font=("Arial", 32, 'normal', 'bold', 'italic', 'underline'))
    car.pendown()


def street(car):
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
    car.color("white")
    car.penup()
    car.forward(350)
    car.penup()
    car.left(90)
    car.forward(100)
    car.pendown()
    car.right(180)
    car.forward(150)

def car(IMAGE):
    screen = Screen()
    screen.register_shape(IMAGE)
    car = Turtle()
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


    exit1 = input("Press any key to exit!")


def main():
    IMAGE = "car\car-2-icon-48.gif"
    car(IMAGE)


if __name__ == '__main__':
    main()
