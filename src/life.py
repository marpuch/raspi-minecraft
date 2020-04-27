import random


class Board:

    def __init__(self, x: int=20, y: int=10):
        self.board = [[bool(random.getrandbits(1)) for i in range(x)] for j in range(y)]
        self.x = x
        self.y = y

    def __str__(self):
        result = []
        for y in self.board:
            for x in y:
                result.append('X' if x else '.')
            result.append('\n')
        return ''.join(result)

    def get(self, x: int, y: int) -> bool:
        return self.board[y][x]

    def next(self):
        next_board = []
        for y, row in enumerate(self.board):
            next_row = []
            next_board.append(next_row)
            for x, cell in enumerate(row):
                next_row.append(self.__next_cell(x, y))
        self.board = next_board

    def __next_cell(self, x, y) -> bool:
        c = self.__count_neighbours(x, y)
        alive = self.board[y][x]
        if alive and c in (2, 3):
            return True
        if not alive and c == 3:
            return True
        return False

    def __count_neighbours(self, x, y):
        return self.__count(x-1, y) + self.__count(x+1, y) + self.__count(x, y-1) + self.__count(x, y+1) + \
               self.__count(x-1, y-1) + self.__count(x-1, y+1) + self.__count(x+1, y-1) + self.__count(x+1, y+1)

    def __count(self, x, y):
        return 1 if self.board[y % self.y][x % self.x] else 0

    def is_dead(self) -> bool:
        for y in self.board:
            for x in y:
                if x:
                    return True
        return False


if __name__ == '__main__':
    game = Board()
    game_hist = set()
    steps = 1
    while True:
        game_str = str(game)
        print(game_str)
        if game_str in game_hist:
            break
        game_hist.add(game_str)
        game.next()
        steps += 1

    print("Game ended after {} steps".format(steps))
