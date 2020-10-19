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





def display_board(board):
    print(board[1] +'|'+ board[2] +'|'+ board[3])
    print('-----')
    print(board[4] +'|'+ board[5] +'|'+ board[6])
    print('-----')
    print(board[7] +'|'+ board[8] +'|'+ board[9])

board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(board)






def place_marker(board, marker, position):

    board[position] = marker

# place_marker(board, 'X', 1)
# display_board(board)


def win_check(board, mark):
# Checks for 3 aligned X's or O's
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))


display_board(board)
win_check(board, 'X')





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







