from engine import PygameEngine

class SnakeGame(PygameEngine):

    def __init__(self):
        PygameEngine.__init__(self)

    def logic(self):
        self.render([[0,1,0,0],
                     [0,1,0,0],
                     [0,1,0,0],
                     [0,1,0,0]])

gameEngine = SnakeGame()
gameEngine.mainLoop()
