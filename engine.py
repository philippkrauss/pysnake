import pygame
import random
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Set the height and width of the screen
SIZE = [400, 400]

snow_list = []
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

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
        for i in range(len(snow_list)):
            # Draw the snow flake
            pygame.draw.circle(self.screen, WHITE, snow_list[i], 2)

            # Move the snow flake down one pixel
            snow_list[i][1] += 1

            # If the snow flake has moved off the bottom of the screen
            if snow_list[i][1] > 400:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                # Give it a new x position
                x = random.randrange(0, 400)
                snow_list[i][0] = x
        return




