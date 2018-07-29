from engine import PygameEngine
from engine import Key
from gamefield import GameField
from snake import Snake
from snake import Direction

class SnakeGame(PygameEngine):

    def __init__(self):
        PygameEngine.__init__(self)
        self.index = 0
        self.gamefield = GameField(84, 48)
        self.snake = Snake()
        self.direction = Direction.RIGHT

    def logic(self, key):
        self.calculateDirection(key)

        self.index += 1
        if ((self.index % 10) == 0):
            self.snake.grow()
        self.gamefield.clear()
        self.snake.move(self.direction)
        self.snake.render(self.gamefield)
        self.render(self.gamefield.matrix)

    def calculateDirection(self, key):
        if key == Key.LEFT:
            self.direction = Direction.LEFT
        if key == Key.RIGHT:
            self.direction = Direction.RIGHT
        if key == Key.UP:
            self.direction = Direction.UP
        if key == Key.DOWN:
            self.direction = Direction.DOWN


gameEngine = SnakeGame()
gameEngine.mainLoop()


# TODO
# position snake in middle of game field
# do collision detection with snake
# do collision detection with boundaries
# adjust speed
