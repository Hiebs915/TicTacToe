#Function below displays board.
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board(board):
    print(board[1] +'|'+ board[2] +'|'+ board[3])
    print('-----')
    print(board[4] +'|'+ board[5] +'|'+ board[6])
    print('-----')
    print(board[7] +'|'+ board[8] +'|'+ board[9])


#display_board(board)





#Randomly chooses which player goes first.
def choose_first_player():
    import random
    first_player = (str(random.randint(1,2)))

    if first_player == '1':
        print("\nPlayer " +first_player+ " goes first.")
    if first_player == '2':
        print("\nPlayer " +first_player+ " goes first.")

    return first_player


#first_player = choose_first_player()





#Asks first_player if they want to be X's or O's.
def player_input(first_player):

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("\nPlayer " +first_player+ " , do you want to be X's or O's?  Please enter X or O: ").upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        player1 = 'O'

    print("\nPlayer 1 is: " + player1)
    print("Player 2 is: " + player2)
    return(player1,player2)


#player_input(first_player)







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


#win_check(board, mark)






#Checks if a specific position contains an X or O.
def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return True
    else:
        return False


#space_check(board, 3)





#Checks if the tictactoe board is full of X's or O's.  If its full and nobody has won its a tie.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


#full_board_check(board)





# Asks the player if they want to play again.
def replay():
    if input("Do you want to play again?  Please enter Yes or No: ") == 'Yes':
        return True
    else:
        return False


#replay()















print('Welcome to Tic Tac Toe!')

while True:
    display_board(board) #Displays the board.

    first_player = choose_first_player() #Chooses the first player (player1 or player2).

    player_input(first_player) #Asks the first_player if they want to be X's or O's and assigns X or O accordingly.

    place_marker(board, input("Player " +first_player+ " Enter your marker (X or O)", int(input("\nPlayer " +first_player+ " Please enter the position you want to place your marker in: "))) # Asks the player to enter the position they would like to place their marker.

    display_board(board)

    full_board_check(board)

    win_check(board, 'X')
        #pass

        #while game_on:
            #Player 1 Turn


            # Player2's turn.

                #pass

        #if not replay():
            #break
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







