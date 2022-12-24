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
    line = lambda x: len(set(x)) == 1 and 0 not in x
    zero = False
    diagonals = [[], []]
    for i in range(3):
        col = [[]]
        for j in range(3):
            col[0].append(board[j][i])
            if board[i][j] == 0:
                zero = True
            if i == j:
                diagonals[0].append(board[i][j])
            if i == 2 - j:
                diagonals[1].append(board[i][j])
        if line(board[i]):
            return (1, 2)[2 in board[i]]
        if line(col[0]):
            return (1, 2)[2 in col]
    for i in range(2):
        if line(diagonals[i]):
            return board[1][1]
    return (0, -1)[zero]
