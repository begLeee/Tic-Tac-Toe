
def check_winner(game):
    # check column
    for n in range(0, 3):
        raw = set([game[n][0],game[n][1],game[n][2]])
        if len(raw) == 1 and game != 0:
            winner = game[n][0]
            return winner
    # check raw
    for n in range(0, 3):
        column = set([game[0][n], game[1][n], game[2][n]])
        if len(column) == 1 and game != 0:
            winner = game[0][n]
            return winner
    # check diagonals
    diagonal_1 = set([game[0][0], game[1][1], game[2][2]])
    diagonal_2 = set([game[0][2], game[1][1], game[2][0]])
    if len(diagonal_1) == 1 or len(diagonal_2) == 1 and game[1][1] != 0:
        winner = game[1][1]
        return winner


