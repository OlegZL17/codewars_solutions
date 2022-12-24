"""
DESCRIPTION:
If we were to set up a Tic-Tac-Toe game, we would want to know
whether the board's current state is solved, wouldn't we?
Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array,
where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
"""


def is_solved(board):
    win = lambda x: len(set(x)) == 1 and 0 not in x
    zero = False
    lines = [[], []] + board
    for i in range(3):
        col = []
        for j in range(3):
            col.append(board[j][i])
            if board[i][j] == 0:
                zero = True
            if i == j:
                lines[0].append(board[i][j])
            if i == 2 - j:
                lines[1].append(board[i][j])
        lines.append(col)
    for i in lines:
        if win(i):
            return i[0]
    return (0, -1)[zero]
