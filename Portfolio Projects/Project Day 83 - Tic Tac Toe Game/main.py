import random

print("Welcome to the Tic-Tac-Toe Game")
print("You play 'X', Computer plays 'O'")

current_player = "X"
won = str()
game = True

board = [" "," "," ",
        " "," "," ",
        " "," "," "]


def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def get_input(board):
    try:
        user_input = int(input("Enter a number between 1 and 9: "))
        while True:
            if user_input >= 1 and user_input <= 9 and board[user_input - 1] == " ":
                board[user_input - 1] = current_player
                break
            else:
                user_input = int(input("Try again. Enter a number between 1 and 9: "))
    except ValueError:
        print("Wrong type of value. Try again!")
        get_input(board)


def check_winner_rows(board):
    global won
    if board[0] == board[1] == board[2] and board[0] != " ":
        won = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        won = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        won = board[6]
        return True


def check_winner_cols(board):
    global won
    if board[0] == board[3] == board[6] and board[0] != " ":
        won = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        won = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        won = board[2]
        return True


def check_winner_diagonal(board):
    global won
    if board[0] == board[4] == board[8] and board[0] != " ":
        won = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        won = board[2]
        return True


def check_all_win_conditions(board):
    global game
    if game == False:
        pass
    if check_winner_cols(board) or check_winner_rows(board) or check_winner_diagonal(board):
        display_board(board)
        print(f"{won} won the game!")
        game = False


def tie(board):
    global game
    if " " not in board:
        display_board(board)
        print("Tie!")
        game = False


def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def player_computer(board):
    if current_player == "O":
        rand_number = random.randint(1,9)
        while True:
            if board[rand_number-1] == " ":
                board[rand_number-1] = "O"
                break
            else:
                rand_number = random.randint(1, 9)

            if " " not in board:
                break


#------------------------------Playing with 2 players-----------------------
# while game:
#     display_board(board)
#     get_input(board)
#     tie(board)

#     if game == False:
#        break
#
#     check_all_win_conditions(board)
#
#     change_player()

#------------------------------Playing with a computer-----------------------
while game:
    display_board(board)
    get_input(board)

    check_all_win_conditions(board)
    tie(board)

    if game == True:
        change_player()
        player_computer(board)
        change_player()

        check_all_win_conditions(board)
        tie(board)
