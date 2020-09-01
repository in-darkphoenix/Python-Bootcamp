import random


def display_board(board):
    print('\n' * 10)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    """
    :return: a tuple - (p1_marker, p2_marker)
    """
    marker = ''
    while not (marker == 'x' or marker == 'o'):
        marker = input('P1, enter x or o - ').lower()
    if marker == 'x':
        return 'x', 'o'
    else:
        return 'o', 'x'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[7] == board[8] == board[9] == mark or
            board[4] == board[5] == board[6] == mark or
            board[1] == board[2] == board[3] == mark or
            board[7] == board[4] == board[1] == mark or
            board[8] == board[5] == board[2] == mark or
            board[9] == board[6] == board[3] == mark or
            board[7] == board[5] == board[3] == mark or
            board[9] == board[5] == board[1] == mark)


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'P1'
    else:
        return 'P2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) and space_check(board, position):
        position = int(input('Choose your next markers position - '))
        return position


def replay():
    choice = input('Wanna play again? yes or no - ')
    return choice == 'yes'


print('Welcome to TIC-TAC-TOE')
print('Manufactured by Ankit Phoenix pvt. ltd.')
while True:
    b = [' '] * 10
    p1m, p2m = player_input()

    turn = choose_first()
    print(turn + ' will choose first')

    while True:
        if turn == 'P1':
            display_board(b)
            p = player_choice(b)
            place_marker(b, p1m, p)
            if win_check(b, p1m):
                display_board(b)
                print('Congrats P1 has won the game!!')
                break
            else:
                if full_board_check(b):
                    print('Prophecy of cat became true, the game is tied!!')
                    break
                else:
                    turn = 'P2'
        else:
            display_board(b)
            p = player_choice(b)
            place_marker(b, p2m, p)
            if win_check(b, p2m):
                display_board(b)
                print('Congrats P2 has won the game!!')
                break
            else:
                if full_board_check(b):
                    print('Prophecy of cat became true, the game is tied!!')
                    break
                else:
                    turn = 'P1'
    if not replay():
        break
