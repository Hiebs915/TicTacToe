game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


'''count = 0
for row in game:
    print(count, row)
    count += 1'''

def game_board():
	print("   0  1  2")
	for count, row in enumerate(game):
   		print(count, row)

game_board()

game[0][1] = 2

game_board()

