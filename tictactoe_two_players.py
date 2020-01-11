#board
#display board
#play game
#handles turn
#check win
    #check rows
    #check columns
    #check Diagonals
#check tie
#flip player
#end game


initial_board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
game_still_going = True
winner = None
current_player = "X"


def display_board():
    print("")
    print(" " + board[0] + " " + "|" + " " + board[1] + " " + "|" + " " + board[2] + " ")
    print("___|___|___")
    print(" " + board[3] + " " + "|" + " " + board[4] + " " + "|" + " " + board[5] + " ")
    print("___|___|___")
    print(" " + board[6] + " " + "|" + " " + board[7] + " " + "|" + " " + board[8] + " ")
    print("   |   |   ")


def handle_turn(player):
    print(player + "'s Turn.")
    position = input("Choose a Position From 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid Input.")
            position = input("Choose a Position From 1-9: ")
        position = int(position) - 1
        if board[position] == " ":
            valid = True
        else:
            print("The Position is Already Filled. Choose Wisely!")
            position = input("Choose a Position From 1-9: ")
    board[position] = player
    display_board()


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != " "
    col_2 = board[1] == board[4] == board[7] != " "
    col_3 = board[2] == board[5] == board[8] != " "
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != " "
    diag_2 = board[2] == board[4] == board[6] != " "
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def check_if_win():
    global winner
    row = check_rows()
    column = check_columns()
    diagonals = check_diagonals()
    if row:
        winner = row
    elif column:
        winner = column
    elif diagonals:
        winner = diagonals
    else:
        winner = None
    return


def check_if_tie():
    global game_still_going
    if(" " not in board):
        game_still_going = False
    return


def check_if_game_over():
    check_if_win()
    check_if_tie()


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def replay_game():
    global game_still_going
    global winner
    global current_player
    print("\nDo You Want To Play More?")
    print("Press 1 To Play")
    print("Press 2 To Quit")
    kp = input("> ")
    kp = int(kp)
    while True:
        if(kp == 1):
            global board
            board = initial_board
            game_still_going = True
            winner = None
            current_player = "X"
            play_game()
        elif(kp == 2):
            quit()
        else:
            print("Invalid Input")


def play_game():
    print("TIC TAC TOE")
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("There is a Tie.")
    replay_game()


play_game()
