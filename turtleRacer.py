import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'yellow', 'brown', 'black', 'cyan']


def get_number_of_racers():
     racers = 0
     while True:
         racers = input("How many racers would you like to compete?(2-10) ")
         if racers.isdigit():
             racers = int(racers)
             if 2<=racers <=10:
                 return racers
             else:
                 print("Invalid number of racers")
         else:
             print("Please enter a valid number of racers")


def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer =turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)* spacingX, -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y>= HEIGHT//2 -10:
                return colors[turtles.index(racer)]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


def main():
    print("Welcome to Turtle Racer!")            
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print("The winning turtle is the one colored", winner)
    time.sleep(5)
    
main()

                