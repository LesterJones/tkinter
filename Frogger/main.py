from turtle import Turtle, Screen
from car import Car
import time
import random

# Set up car variables.
CAR_SPEED = .1
CAR_MOVEMENT = 5
CARS_PER_LANE = 4

# Set up a screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Frogger")
screen.colormode(255)
screen.bgcolor(105, 105, 105)
screen.tracer(0)

# Create the user-turtle.
tim = Turtle()
tim.penup()
tim.color('red')
tim.shape('turtle')
tim.goto(0, -250)
tim.left(90)
tim.shapesize(2)

# Create some road markings.
road_maker = Turtle()
road_maker.penup()
road_maker.pensize(5)
road_maker.speed('fastest')
lane_positions = [200, 100, 0, -100, -200]
for lane in lane_positions:
    road_maker.goto(-390, lane)
    while road_maker.xcor() < 400:
        road_maker.hideturtle()
        road_maker.pendown()
        road_maker.forward(50)
        road_maker.penup()
        road_maker.forward(50)


def create_car_list():
    new_cars = list()
    car_lanes = [-150, -50, 50, 150]
    for car_lane in car_lanes:
        for i in range(CARS_PER_LANE):
            y_coordinate = car_lane
            new_car = Car()
            new_car.color('white')
            new_car.shape('square')
            new_car.goto(random.randint(-400, 400), y_coordinate)
            new_cars.append(new_car)
    return new_cars


def move_left():
    x = tim.xcor() - 50
    y = tim.ycor()
    tim.goto(x, y)


def move_right():
    x = tim.xcor() + 50
    y = tim.ycor()
    tim.goto(x, y)


def move_up():
    x = tim.xcor()
    y = tim.ycor() + 100
    tim.goto(x, y)


def move_down():
    x = tim.xcor()
    y = tim.ycor() - 100
    tim.goto(x, y)


# Position a turtle to display the current_level.
level_turtle = Turtle()
level_turtle.penup()
level_turtle.hideturtle()
level_turtle.goto(0, 230)
level_turtle.pendown()

# Set up on-key movement for the user turtle.
screen.listen()
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")


# Start the game.
level = 1
game_is_on = True
while game_is_on:
    screen.update()
    level_turtle.clear()
    level_turtle.write(f"Level: {level}", align='center', font=("Courier", 40, 'normal'))

    # Create a list of cars based on the number of cars_per_lane and lane_positions.
    vehicles = create_car_list()
    level_is_running = True
    while level_is_running:
        time.sleep(CAR_SPEED)
        screen.update()

        # Move all the vehicles.
        for vehicle in vehicles:
            vehicle.move(CAR_MOVEMENT)
            if vehicle.xcor() >= 400:
                vehicle.set_location(-400, vehicle.ycor())

        # Check for collisions. i.e Tim gets squished.
        for vehicle in vehicles:
            if tim.distance(vehicle.xcor(), vehicle.ycor()) < 10:
                print('Stop')
                tim.shapesize(stretch_wid=4, stretch_len=2)
                you_lose = Turtle()
                you_lose.pencolor('white')
                you_lose.hideturtle()
                you_lose.write('You Lose', align='center', font=('Courier', 40, 'bold'))
                level_is_running = False
                game_is_on = False
                screen.update()

        # Check to see if tim has finished.  If he has increment the level and continue.
        if tim.ycor() > 200:
            tim.goto(0, -250)
            for vehicle in vehicles:
                vehicle.set_location(-450, vehicle.ycor())
            CAR_SPEED *= .9
            level += 1
            level_is_running = False













screen.exitonclick()