from turtle import *
import time


# this function helps in taking the turtle to the starting point of the car's moving position
def go_to_start(car):
    car.penup()
    car.goto(-210, 0)
    car.pendown()


# writes case 1 on screen
def case1_text(car):
    """ Types Case1 on Screen"""
    car.penup()
    car.goto(-280, 200)
    car.color("White")
    car.write("Case 1: ", font=("Arial", 32, 'normal', 'bold', 'italic', 'underline'))
    car.pendown()
    car.hideturtle()


# writes case 2 on screen
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
    car.write("Please Use Automatic Brakes To Save Lives!!!\n Thanks For Listening",
              font=("Arial", 16, 'normal', 'bold', 'italic'))
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
    screen.title("Demonstration")

    screen.delay(0)
    # this writes case 1
    case1_writer = Turtle()
    case1_writer.hideturtle()
    case1_writer.color(112, 120, 100)
    case1_writer.penup()
    case1_text(case1_writer)
    pendown()
    go_to_start(car1)
    street(car1)
    wall(car1)

    go_to_start(car1)

    car1.penup()
    car1.left(90)
    car1.forward(40)
    car1.pendown()

    go_to_start(car1)
    car1.penup()

    car1.forward(30)
    car1.pendown()

    # time.sleep(0.5)
    screen.delay(10)

    # Now stop before the wall
    car1.penup()
    car1.speed(1)
    car1.left(90)
    car1.forward(50)
    car1.right(90)
    car1.forward(155)

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

    # creating the braking starting point line
    brake_line = Turtle()
    brake_line.hideturtle()
    brake_line.left(90)
    brake_line.penup()
    brake_line.forward(25)
    brake_line.pendown()
    brake_line.forward(90)
    brake_line.right(180)
    brake_line.penup()
    brake_line.forward(100)
    brake_line.pendown()

    time.sleep(5)
    screen.delay(70)
    car1.forward(160)
    car1.pendown()

    screen.delay(0)
    # draw line between cars
    border()

    # initialize case 2     --------------------------------------------------
    car2 = Turtle()
    screen.register_shape(IMAGE2)
    car2.shape(IMAGE2)

    # Cars starting point
    car2.speed(0)
    screen.delay(0)
    case1_writer.clear()  # removes case 1 from screen
    case2_text(car2)
    car2.penup()
    car2.goto(-170, -30)
    car2.pendown()

    time.sleep(2)
    car2.penup()
    screen.delay(20)

    car2.forward(160)
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

    # draws the line
    brake_line2 = Turtle()
    brake_line2.hideturtle()
    brake_line2.penup()
    brake_line2.forward(20)
    brake_line2.pendown()
    brake_line2.right(90)
    brake_line2.forward(70)

    # the car hits the brakes
    screen.delay(75)
    # car stops on line for a sec then hits the brakes
    time.sleep(3)
    car2.forward(170)

    car2.pendown()

    screen.delay(15)
    # Remover the car and the man
    car2.hideturtle()
    man2.hideturtle()

    # the crash
    screen.delay(0)
    screen.register_shape(IMAGE5)
    crash = Turtle()
    crash.shape(IMAGE5)
    crash.penup()
    crash.speed(0)
    crash.goto(190.00, -30.00)
    crash.pendown()

    # Writes the final words!!
    starting_text(car2)

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
