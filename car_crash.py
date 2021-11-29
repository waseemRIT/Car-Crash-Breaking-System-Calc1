from turtle import *
import time


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
    car.pensize(10)
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


def border():
    line = Turtle()
    line.shape("classic")
    line.pencolor("black")
    line.penup()
    line.goto(-180, 20)
    line.pendown()
    line.forward(350)


def demo(IMAGE1, IMAGE2, IMAGE3, IMAGE4, IMAGE5):
    screen = Screen()
    screen.register_shape(IMAGE1)
    car1 = Turtle()
    car1.speed(0)
    car1.shape(IMAGE1)

    screen.colormode(255)
    screen.bgcolor(112, 120, 100)
    screen.title("Case 1 ")

    screen.delay(0)
    case1_text(car1)
    go_to_start(car1)
    street(car1)
    wall(car1)

    go_to_start(car1)

    car1.penup()
    car1.left(90)
    car1.forward(40)
    car1.pendown()

    starting_text(car1)
    go_to_start(car1)
    car1.penup()

    car1.forward(30)
    car1.pendown()

    time.sleep(5)
    screen.delay(10)

    # Now stop before the wall
    car1.penup()
    car1.speed(1)
    car1.left(90)
    car1.forward(50)
    car1.right(90)
    car1.forward(160)

    # creating the man - survives
    screen.delay(0)
    screen.register_shape(IMAGE3)
    man1 = Turtle()
    man1.shape(IMAGE3)
    man1.penup()
    man1.left(90)
    man1.forward(50)
    man1.right(90)
    man1.forward(200)
    man1.pendown()

    screen.delay(70)
    car1.forward(160)
    screen.delay(10)
    car1.pendown()

    screen.delay(0)
    # draw line between cars
    border()

    time.sleep(3)

    # initialize case 2
    car2 = Turtle()
    screen.register_shape(IMAGE2)
    car2.shape(IMAGE2)

    car2.speed(0)
    case2_text(car2)
    car2.penup()
    car2.goto(-170, -30)
    car2.pendown()
    screen.delay(10)

    time.sleep(1.8)

    car2.speed(1)
    car2.penup()
    car2.forward(165)

    # creating the second man - dies
    screen.delay(0)
    man2 = Turtle()
    man2.shape(IMAGE3)
    man2.penup()
    man2.right(90)
    man2.forward(18)
    man2.left(90)
    man2.forward(200)
    man2.pendown()
    # the car hits the brakes
    screen.delay(70)
    car2.forward(165)
    screen.delay(10)
    car2.pendown()

    # the crash
    screen.delay(0)
    screen.register_shape(IMAGE5)
    crash = Turtle()
    crash.shape(IMAGE5)
    crash.penup()
    crash.speed(0)
    crash.goto(190.00, -18.00)
    crash.pendown()
    

    done()


def main():
    car1 = r"car1.gif"
    car2 = r"car_2.gif"
    man1 = r"man3.gif"
    man2 = r"man5.gif"
    crash = r"crash6.gif"
    demo(car1, car2, man1, man2, crash)


if __name__ == '__main__':
    main()
