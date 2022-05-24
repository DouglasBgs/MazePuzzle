

import turtle
import time
import os
import pygame

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Labirinto")
wn.setup(1300,700)


start_x = 0
start_y = 0
end_x = 0
end_y = 0
cheeses = []

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)


class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        
class Cheese(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("violet")
        self.penup()
        self.speed(0)


def getGrid(file):
    with open(file) as f:
        lines = f.read().splitlines()
        return [line.strip() for line in lines]
    
def eatCheese(x, y):
    for z in range(len(cheeses)):
        if(x == cheeses[z][0] and y == cheeses[z][1]):
            burp = pygame.mixer.Sound("burp.wav")
            burp.play()
            time.sleep(2)
            burp.stop()
            print('Burp!!')

def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "#":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == "." or character == "C":
                path.append((screen_x, screen_y))

            if character == "S":
                yellow.goto(screen_x, screen_y)
                yellow.stamp()
                end_x, end_y = screen_x, screen_y
                path.append((screen_x, screen_y))

            if character == "E":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)
            
            if character == "C":
                chesse.goto(screen_x, screen_y)
                chesse.stamp()
                cheeses.append((screen_x, screen_y))
            

def search(x,y):
    frontier.append((x, y))
    solution[x, y] = x, y
    while len(frontier) > 0:
       
        current = (x,y)

        if(x - 24, y) in path and (x - 24, y) not in visited:
            cellleft = (x - 24, y)
            solution[cellleft] = x, y
            blue.goto(cellleft)
            frontier.append(cellleft)

        if (x, y - 24) in path and (x, y - 24) not in visited:
            celldown = (x, y - 24)
            solution[celldown] = x, y
            blue.goto(celldown)
            frontier.append(celldown)

        if(x + 24, y) in path and (x + 24, y) not in visited:
            cellright = (x + 24, y)
            solution[cellright] = x, y
            blue.goto(cellright)
            frontier.append(cellright)

        if(x, y + 24) in path and (x, y + 24) not in visited:
            cellup = (x, y + 24)
            solution[cellup] = x, y
            blue.goto(cellup)
            frontier.append(cellup)

        x, y = frontier.pop()
        visited.append(current)
        green.goto(x,y)
        if (x,y) == (end_x, end_y):
            yellow.stamp()
        if (x,y) == (start_x, start_y):
            red.stamp()

def backRoute(x, y):
    yellow.goto(x, y)                      
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]
        eatCheese(x,y)

pygame.init()
pygame.mixer.init()
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
chesse = Cheese()
walls = []
path = []
visited = []
# burp = os.path.abspath('arroto.mp3')
frontier = []
solution = {}
file = 'maze.txt'
grid = getGrid(file)

setup_maze(grid)
search(start_x, start_y)
backRoute(end_x, end_y)

wn.exitonclick()
