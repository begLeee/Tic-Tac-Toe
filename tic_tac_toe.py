from game_board import draw_board
from checking_winner import check_winner

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def draw_game():
    draw_board(board)
    count = 0
    while True:

        if count % 2 == 0:
            col = int(input('Player 1\ncol: '))
            raw = int(input('raw: '))
            if board[col-1][raw-1] ==' ':
                del board[col-1][raw-1]
                board[col-1].insert((raw-1), 'X')
                draw_board(board)
                if check_winner(board) == 'X':
                    print('\n===========================\n'
                          'Player 1 has won\n')
                elif check_winner(board) == 'O':
                    print('\n===========================\n'
                          'Player 2 has won\n')
            else:
                print('ERROR: try again')
                continue
        else:
            col = int(input('Player 2\ncol: '))
            raw = int(input('raw: '))
            if board[col-1][raw-1] ==' ':
                del board[col-1][raw-1]
                board[col-1].insert((raw-1), 'O')
                draw_board(board)
                if check_winner(board) == 'X':
                    print('\n===========================\n'
                          'Player 1 has won\n')
                elif check_winner(board) == 'O':
                    print('\n===========================\n'
                          'Player 2 has won\n')
            else:
                print('ERROR: try again')
                continue
        count += 1
        if count == 9:
            print('\n===========================\n'
                  'draw')

print('Hey! It\'s a TIC TAC TOE game.'
      '\nInstructions are simple.'
      '\nYou shoud type first a column then a raw you want to move(from 1 to 3).'
      '\nPlayer 1 plays with "X" and Player 2 plays with "O"'
      '\nLet\'s begin.')
draw_game()
