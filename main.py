# imported required libraries
import pygame, random
from pygame.math import Vector2
import sys


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size,
                                     cell_size)
            pygame.draw.rect(screen, (182, 191, 122), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class Fruit:
    def __init__(self):
        self.x = None
        self.y = None
        self.position = None
        self.randomize()

    def create_fruit(self):
        fruit = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.create_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    def check_fail(self):
        #check if snake is outside of screen
        if not 0 <= self.snake.body[0].x <= cell_number:
            self.game_over()
    def game_over(self):
        pass


# Initialized the pygame module
pygame.init()

# Create a screen(with size) and clock object
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

SCREEN_UPADTE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPADTE, 150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPADTE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 111, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
