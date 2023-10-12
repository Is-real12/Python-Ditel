tiktok_board = [' '] * 9


def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')


display_board(tiktok_board)

while True:
    position_x = int(input('Player X, enter a position (1-9): ')) - 1
    if tiktok_board[position_x] == ' ':
        tiktok_board[position_x] = 'X'
    else:
        print('Position already taken. Try again.')
        continue

    display_board(tiktok_board)

    position_o = int(input('Player O, enter a position (1-9): ')) - 1
    if tiktok_board[position_o] == ' ':
        tiktok_board[position_o] = 'O'
    else:
        print('Position already taken. Try again.')
        continue

    display_board(tiktok_board)
c