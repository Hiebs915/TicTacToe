# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# def display_board(board):
#     print(board[0] +'|'+ board[1] +'|'+ board[2])
#     print('-----')
#     print(board[3] +'|'+ board[4] +'|'+ board[5])
#     print('-----')
#     print(board[6] +'|'+ board[7] +'|'+ board[8])

# display_board(board)




def player_input():

    player_choice = 'WRONG'
    acceptable_digits = [1,2]
    digit_choice = False

    while player_choice.isdigit() == False or digit_choice == False:
        player_choice = input('\nDo you want to be player 1 or 2?  Please enter "1" or "2": ')

        # Two conditions to check: 1.) Is the input a digit? 2.) Is the input an acceptable digit(1 or 2)?
        # Digit Check
        if player_choice.isdigit() == False:
            print("Sorry, that is not a digit")

        # Acceptable Digit Check
        if player_choice.isdigit() == True:
            if int(player_choice) in acceptable_digits:
                digit_choice = True
                if int(player_choice) == 1:
                    print("You are player 1 and are X's")
                    player1 = "X"
                if int(player_choice) == 2:
                    print("You are player 2 and are O's")
                    player2 = "O"
            else:
                print("Sorry, you did not enter a '1' or '2'")
                digit_choice = False
    return int(player_choice)


player_input()


