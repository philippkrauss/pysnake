from engine import PygameEngine
import random

class SnakeGame(PygameEngine):

    def __init__(self):
        PygameEngine.__init__(self)
        self.snow_list = []
        # Loop 50 times and add a snow flake in a random x,y position
        for i in range(50):
            x = random.randrange(0, 400)
            y = random.randrange(0, 400)
            self.snow_list.append([x, y])

    def logic(self):
        for i in range(len(self.snow_list)):
            # Draw the snow flake
            self.circle(self.snow_list[i])

            # Move the snow flake down one pixel
            self.snow_list[i][1] += 1

            # If the snow flake has moved off the bottom of the screen
            if self.snow_list[i][1] > 400:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                self.snow_list[i][1] = y
                # Give it a new x position
                x = random.randrange(0, 400)
                self.snow_list[i][0] = x

gameEngine = SnakeGame()
gameEngine.mainLoop()
