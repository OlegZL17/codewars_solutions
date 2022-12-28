"""
DESCRIPTION:
Write a method that takes a field for well-known board game "Battleship" as an argument
and returns true if it has a valid disposition of ships, false otherwise.
Argument is guaranteed to be 10*10 two-dimension array.
Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing several "ships"
and objective is to destroy enemy's forces by targetting individual cells on his field.
The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version.
In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1).
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
"""


def validate_battlefield(field):
    def count_fragments(x, y, down=True):
        cnt = 0
        if down:
            while x < 10:
                if field[x][y] == 1:
                    cnt += 1
                    x += 1
                else:
                    return cnt
        else:
            while y < 10:
                if field[x][y] == 1:
                    cnt += 1
                    y += 1
                else:
                    return cnt
        return cnt

    def make_ship(x, y, length, down=True):
        if down:
            for i in range(length):
                field[x + i][y] = length
            for i in range(length):
                if check_around(x + i, y, length):
                    return True
        else:
            for i in range(length):
                field[x][y + i] = length
            for i in range(length):
                if check_around(x, y + i, length):
                    return True
        ships[length] = ships.get(length, 0) + 1

    def check_around(x, y, num):
        cnt = 0
        total = 0
        cord1 = []
        cord2 = []
        for i in range(-1, 2):
            if 0 <= x + i < 10:
                for j in range(-1, 2):
                    if 0 <= y + j < 10:
                        if field[x + i][y + j] != 0:
                            cnt += 1
                            total += field[x + i][y + j]
                            cord1.append(x + i)
                            cord2.append(y + j)
        if total / cnt == num and any(map(lambda x: len(set(x)) == 1, (cord1, cord2))):
            return False
        else: return True

    ships = {1: 0, 2: 0, 3: 0, 4: 0}

    for i in range(10):
        for j in range(10):
            if field[i][j] == 1:
                if i < 9 and field[i + 1][j] == 1:
                    if make_ship(i, j, count_fragments(i, j)):
                        return False
                elif j < 9 and field[i][j + 1] == 1:
                    if make_ship(i, j, count_fragments(i, j, False), False):
                        return False
                else:
                    ships[1] = ships[1] + 1
                    if check_around(i, j, 1):
                        return False
    return ships == {1: 4, 2: 3, 3: 2, 4: 1}