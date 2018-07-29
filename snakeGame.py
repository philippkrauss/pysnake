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
        self.running = True

    def logic(self, key):
        if self.running is not True:
            self.gameOver(key)
        else:
            self.game(key)

    def game(self, key):
        self.calculateDirection(key)
        self.index += 1
        if ((self.index % 10) == 0):
            self.snake.grow()
        self.snake.move(self.direction)

        if self.collision():
            self.running = False
        else:
            self.gamefield.clear()
            self.snake.render(self.gamefield)
            self.render(self.gamefield.matrix)

    def collision(self):
        snakeHead = self.snake.getHead()
        if snakeHead[0] < 0:
            return True
        if snakeHead[0] >= self.gamefield.height:
            return True
        if snakeHead[1] < 0:
            return True
        if snakeHead[1] >= self.gamefield.width:
            return True
        return False



    def calculateDirection(self, key):
        if key == Key.LEFT:
            self.direction = Direction.LEFT
        if key == Key.RIGHT:
            self.direction = Direction.RIGHT
        if key == Key.UP:
            self.direction = Direction.UP
        if key == Key.DOWN:
            self.direction = Direction.DOWN

    def gameOver(self, key):
        self.render(self.gamefield.matrix)

gameEngine = SnakeGame()
gameEngine.mainLoop()


# TODO
# position snake in middle of game field
# do collision detection with snake
# do collision detection with boundaries
# adjust speed
