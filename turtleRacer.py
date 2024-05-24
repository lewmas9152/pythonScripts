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
    for i, racer in enumerate(colors):
        racer =turtle.Turtle()
        racer.forward(2)
        turtles.append(racer)
    
    return turtles


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
    turtles = create_turtles(colors)
    time.sleep(20)
    
main()

                