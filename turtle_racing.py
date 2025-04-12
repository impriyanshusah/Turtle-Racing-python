import turtle
import random
import time

HEIGHT, WIDTH = 800, 1000
COLORS = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "black",
    "cyan",
]


def get_numbers_of_turtles():
    while True:
        numTurtles = input("Enter the number of turtles (2-10): ")
        if numTurtles.isdigit() and 2 <= int(numTurtles) <= 10:
            return int(numTurtles)
        else:
            print("Invalid input. Please enter a number between 2 & 10.")
            continue


def race(COLORS):
    turtles = create_turtles(COLORS)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return COLORS[turtles.index(racer)]


def create_turtles(COLORS):
    turtles = []
    spacingx = WIDTH // (len(COLORS) + 1)
    for i, COLORS in enumerate(COLORS):
        racer = turtle.Turtle()
        racer.color(COLORS)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + spacingx * (i + 1), -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    screen.bgcolor("white")


def main():
    racers = get_numbers_of_turtles()
    init_turtle()
    random.shuffle(COLORS)
    color = COLORS[:racers]

    winner = race(color)
    print(f"\nWinner is {winner} turtle!")
    time.sleep(2)


if __name__ == "__main__":
    main()
