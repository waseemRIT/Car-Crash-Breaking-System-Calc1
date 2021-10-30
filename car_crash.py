from turtle import Screen, Turtle


def car(IMAGE):
    screen = Screen()
    screen.register_shape(IMAGE)

    car = Turtle()
    car.shape(IMAGE)
    screen.bgcolor("gray")
    screen.title("Case 1 ")
    car.penup()
    car.forward(100)
    car.pendown()
    car.left(90)
    car.forward(50)
    car.right(180)
    car.penup()
    car.forward(50)
    car.pendown()
    car.forward(50)
    exit1 = input("Press any key to exit!")





def main():
    IMAGE = "car\car-2-icon-48.gif"
    car(IMAGE)



if __name__ == '__main__':
    main()