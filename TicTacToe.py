#---------------------------TicTacToe Functions-------------------------------#


#Function below displays board.
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board(board):
    print(board[1] +'|'+ board[2] +'|'+ board[3])
    print('-----')
    print(board[4] +'|'+ board[5] +'|'+ board[6])
    print('-----')
    print(board[7] +'|'+ board[8] +'|'+ board[9])



#Randomly chooses which player goes first.
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'



#Asks first_player if they want to be X's or O's.
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



#Has you enter a marker and the position you want to place it on the board.
def place_marker(board, marker, position):

    board[position] = marker



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



#Checks if a specific position contains an X or O.
def space_check(board, position):

    return board[position] == ' '



#Checks if the tictactoe board is full of X's or O's.  If its full and nobody has won its a tie.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True



def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(turn +' Choose your position: (1-9) '))

    return position



# Asks the player if they want to play again.
def replay():
    print('\n' * 10)
    if input("Do you want to play again?  Please enter Yes or No: ") == 'Yes':
        return True
    else:
        return False



#-----------------------------Game Starts Below-------------------------------#


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board each time this loop is started.
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break



#-----------------------------Game Ends Here----------------------------------#
