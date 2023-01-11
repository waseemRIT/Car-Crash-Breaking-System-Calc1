# Turtle Car Crash Demo
A simple turtle graphics animation that demonstrates the use of automated braking and manual braking in cars. The animation shows a car approaching a wall and braking in two different scenarios: case 1 with automated braking and case 2 with manual braking.
## Description
This application is written in python, using the turtle library for animation. The program includes several functions that are used to create the animation:
* go_to_start(car) function takes the turtle to the starting point of the car's moving position.
* case1_text(car) function writes "Case 1: Automated Brakes" on the screen
* case2_text(car) function writes "Case 2: Manual Braking" on the screen
* street(car) function draws the border of the street.
* wall(car) function draws the wall that the car will hit.
* starting_text(car) function writes a message on screen encouraging the use of automated brakes to save lives.
* border() function draws a line that separates the two cases.
* demo(IMAGE1, IMAGE2, IMAGE3, IMAGE4, IMAGE5) function is the main function that creates the animation.
The function accepts five arguments: the path of the images of the car in different positions, the user can pass their own images or use the provided images.
## Usage
To run the animation, call the demo function and pass the path of the five images of the car in different positions as arguments.
```py
demo("car1.gif", "car2.gif", "car3.gif", "car4.gif", "car5.gif")
```
## Note
This is a simple animation designed for demonstration purposes, it does not provide any functionality related to the car braking system. Also, the provided images are for demonstration only and you can use your own images for more fun.
