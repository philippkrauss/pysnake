class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = []
        self.clear()

    def set(self, row, col, value=1):
        self.matrix[row][col] = value

    def clear(self):
        self.matrix = []
        for rowIndex in range(self.height):
            row = []
            for colIndex in range(self.width):
                row.append(0)
            self.matrix.append(row)
