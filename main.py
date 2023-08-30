# imported required libraries
import pygame,random
from pygame.math import Vector2
import sys

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]

    def drawSnake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size,
                                cell_size)
            pygame.draw.rect(screen,(182,191,122),block_rect)


class Fruit:
    def __init__(self):
        # position x and y
        # a square form of fruit
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.position = Vector2(self.x, self.y)

    def create_fruit(self):
        fruit = pygame.Rect(int(self.position.x*cell_size),int(self.position.y*cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit)
# Initialized the pygame module
pygame.init()

# Create a screen(with size) and clock object
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,111,70))
    fruit.create_fruit()
    snake.drawSnake()
    pygame.display.update()
    clock.tick(60)
