from random import randint

board = []

for i in range(0, 5):
    board.append(["o"] * 5)

turn = 0

ship_row = randint(0, len(board) - 1)
ship_col = randint(0, len(board) - 1)

board[ship_row][ship_col] = "!"

def print_board():
    for row in board:
        print " ".join(row)

def get_turn():
    correct = False
    while not(correct):
        user_row = int(raw_input("you're row: ")) - 1
        if (user_row >= 0) & (user_row < 5):
            correct = True
        else: print "enter correct row number [1 - 5]"

    correct = False
    while not(correct):
        user_col = int(raw_input("you're col: ")) - 1
        if (user_col >= 0) & (user_col < 5):
            correct = True
        else: print "enter correct col number [1 - 5]"

    if board[user_row][user_col] == "x":
        print "You're making this turn!"
        return 0
    elif board[user_row][user_col] == "!":
        print "You win!"
        return -1
    else:
        board[user_row][user_col] = "x"
        return 1

turn = 1

while turn < 6:
    print "turn: ", turn

    if get_turn() == -1:
        break
    else: print_board()

    turn += 1
