class Snake:
    def __init__(self):
        self.size = 4
        self.body = [(10, 20), (10, 19), (10, 18), (10, 17)]

    def render(self, gamefield):
        for coordinate in self.body:
            gamefield.set(coordinate[0], coordinate[1])

    def move(self, direction):
        head = self.getHead()
        newRow = head[0]
        newCol = head[1]
        if direction is Direction.LEFT:
            newCol -= 1
        if direction is Direction.RIGHT:
            newCol += 1
        if direction is Direction.UP:
            newRow -= 1
        if direction is Direction.DOWN:
            newRow += 1
        newHead = (newRow, newCol)
        self.body.insert(0, newHead)
        while len(self.body) > self.size:
           self.body.pop()

    def getHead(self):
        return self.body[0]

    def grow(self):
        self.size += 1


from enum import Enum

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
