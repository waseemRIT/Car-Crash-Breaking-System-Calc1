from turtle import Screen, Turtle


def car(IMAGE):
    screen = Screen()
    screen.register_shape(IMAGE)

    turtle = Turtle()
    turtle.shape(IMAGE)
    turtle.forward(100)
    x = input("")


def main():
    IMAGE = "car\car-2-icon-48.gif"
    car(IMAGE)


if __name__ == '__main__':
    main()