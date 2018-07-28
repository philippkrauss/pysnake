class GameField:
    def __init__(self, width, height):
        self.matrix = []
        for rowIndex in range(height):
            row = []
            for colIndex in range(width):
                row.append(0)
            self.matrix.append(row)

    def set(self, row, col, value=1):
        self.matrix[row][col] = value
