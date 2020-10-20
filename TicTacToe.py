#Asks player 1 if he/she wants to be X's or O's.
def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("\nPlayer 1, do you want to be X's or O's?  Please enter X or O: ").upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1,player2)

# This assigns player1_marker to whatever player1 enters as the input and assigns player2_marker to whichever marker play 1 didn't pick.
# player1_marker, player2_marker = player_input()




#Display board.
def display_board(board):
    print(board[1] +'|'+ board[2] +'|'+ board[3])
    print('-----')
    print(board[4] +'|'+ board[5] +'|'+ board[6])
    print('-----')
    print(board[7] +'|'+ board[8] +'|'+ board[9])

board = ['#',' ',' ','X','O','X','O',' ','O','X']
#display_board(board)





#Has you enter a marker and the position you want to place it on the board.
def place_marker(board, marker, position):

    board[position] = marker


# place_marker(board, 'X', 1)





#Checks if X's or O's won.
def win_check(board, mark):
# Checks for 3 aligned X's or O's
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # Row 1
    (board[4] == mark and board[5] == mark and board[6] == mark) or # Row 2
    (board[7] == mark and board[8] == mark and board[9] == mark) or # Row 3
    (board[1] == mark and board[4] == mark and board[7] == mark) or # Column 1
    (board[2] == mark and board[5] == mark and board[8] == mark) or # Column 2
    (board[3] == mark and board[6] == mark and board[9] == mark) or # Column 3
    (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark)) # Diagonal


#win_check(board, 'X')





#Randomly chooses which player goes first.
def choose_first_player():
    import random
    if (random.randint(1,2)) == 1:
        print("Player 1 goes first.")
    else:
        print("Player 2 goes first.")


#choose_first_player()




#Checks if a specific position contains an X or O.
def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return True
    else:
        return False


#space_check(board, 3)





#Checks if the tictactoe board is full of X's or O's
def full_board_check(board):
    count = 0
    for space in board:
        if space == 'X' or space == 'O' in board:
            count += 1
            if count == 9:
                return True
            else:
                return False


#full_board_check(board)





# Asks the player if they want to play again.
def replay():
    if input("Do you want to play again?  Please enter Yes or No: ") == 'Yes':
        return True
    else:
        return False


replay()


# position = 'WRONG'
# game_board_digits = range(0,10)
# digit_choice = False

# # Board position input check.
# while position.isdigit() == False or digit_choice == False:
#     position = input("\nPlease enter the positon you would like to place your marker on the board.  Please remember to enter a digit between 1-9':" )

#     # Two conditions to check: 1.) Is the input a digit? 2.) Is the input an acceptable digit(1 or 2)?
#     # Digit Check
#     if position.isdigit() == False:
#         print("Sorry, that is not a digit")

#     # Acceptable Digit Check
#     if position.isdigit() == True:
#         if int(position) in game_board_digits:
#             digit_choice = True

#         else:
#             print("Sorry, you did not enter a digit between 1-9")
#             digit_choice = False







