import pygame

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(BLACK)
            self.logic()
            pygame.display.flip()
            self.clock.tick(20)
        pygame.quit()

    def logic(self):
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
