from src.learn import MC, block
from src.life import Board
import time

# rozruch
mc = MC(x=-66, y=-8, z=-272)
mc.say("Aktualizacja Marek")
mc.clean()

# zaczynamy budować
board = Board(10, 10)

while True:
    for i in range(10):
        for j in range(10):
            mc.put(i, 0, j, block.TNT if board.get(i, j) else block.AIR)
    board.next()
    if not board.is_dead():
        break
    time.sleep(2)

