from engine import PygameEngine
from gamefield import GameField


class SnakeGame(PygameEngine):

    def __init__(self):
        PygameEngine.__init__(self)
        self.gamefield = GameField(84, 48)

    def logic(self):
        self.gamefield.set(0, 1)
        self.gamefield.set(1, 1)
        self.gamefield.set(2, 1)
        self.gamefield.set(3, 1)
        self.render(self.gamefield.matrix)


gameEngine = SnakeGame()
gameEngine.mainLoop()
