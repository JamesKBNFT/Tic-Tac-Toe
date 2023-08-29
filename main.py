# --- Global Variables ---
game_still_going = True
winner = None
current_player = "X"
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    #Display the board
    display_board()

    while game_still_going:
        user_turn(current_player)

        check_game_over()

        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " Wins!")
    elif winner == None:
        print("Its a Tie!!!!")

def user_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Space is already filled")

    board[position] = player
    display_board()

def check_game_over():
    check_win()
    check_tie()

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def check_win():
    global winner

    #Check row win
    row_win = check_rows()
    #Check Column win
    column_win = check_columns()
    #Check diag win
    diag_win = check_diag()
    if row_win:
        #There is a win
        winner = row_win
    elif column_win:
        #there is a win
        winner = column_win
    elif diag_win:
        #There is a win
        winner = diag_win
    else:
        # No Win
        winner = None
    return

def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
def check_diag():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]






play_game()






