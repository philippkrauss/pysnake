import pygame
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Set the height and width of the screen
SIZE = [400, 400]



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





