import pygame
from enum import Enum

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
WIDTH = 84
HEIGHT = 48
FACTOR = 10

# Set the height and width of the screen
SIZE = [WIDTH * FACTOR, HEIGHT * FACTOR]


class PygameEngine:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Snow Animation")
        self.clock = pygame.time.Clock()
        return

    def mainLoop(self):
        running = True
        while running:
            key = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    key = event.key
            self.screen.fill(BLACK)
            self.logic(self.getKey(key))
            pygame.display.flip()
            self.clock.tick(20)
        pygame.quit()

    def logic(self, key):
        return

    def circle(self, rectangle):
        pygame.draw.circle(self.screen, WHITE, rectangle, 2)

    def rect(self, rectangle):
        pygame.draw.rect(self.screen, WHITE, rectangle)

    def render(self, matrix):
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[rowIndex])):
                pixel = matrix[rowIndex][colIndex]
                if pixel == 1:
                    pygame.draw.rect(self.screen, WHITE, (colIndex * FACTOR, rowIndex * FACTOR, FACTOR, FACTOR))

    def getKey(self, key):
        if key == 276:
            return Key.LEFT
        if key == 275:
            return Key.RIGHT
        if key == 273:
            return Key.UP
        if key == 274:
            return Key.DOWN

class Key(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
