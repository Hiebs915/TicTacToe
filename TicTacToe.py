def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("\nPlayer 1, do you want to be X's or O's?  Please enter X or O: ")

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1,player2)
# This assigns player1_marker to whatever player1 enters as the input and assigns player2_marker to whichever marker play 1 didn't pick.
player1_marker, player2_marker = player_input()






# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# def display_board(board):
#     print(board[0] +'|'+ board[1] +'|'+ board[2])
#     print('-----')
#     print(board[3] +'|'+ board[4] +'|'+ board[5])
#     print('-----')
#     print(board[6] +'|'+ board[7] +'|'+ board[8])






# def marker_positon(board, marker, position):
#     display_board(board)
#     player_input()


#     player_position = 'WRONG'
#     game_board_digits = range(0,10)
#     digit_choice = False

#     # Board position input check.
#     while player_position.isdigit() == False or digit_choice == False:
#         player_position = input('\nPlease enter the positon you would like to place your marker on the board.  Please remember to enter a digit between 1-9': )

#         # Two conditions to check: 1.) Is the input a digit? 2.) Is the input an acceptable digit(1 or 2)?
#         # Digit Check
#         if player_position.isdigit() == False:
#             print("Sorry, that is not a digit")

#         # Acceptable Digit Check
#         if player_position.isdigit() == True:
#             if int(player_position) in game_board_digits:
#                 digit_choice = True

#             else:
#                 print("Sorry, you did not enter a digit between 1-9")
#                 digit_choice = False




