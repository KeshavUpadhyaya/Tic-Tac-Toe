def print_board(board):

	print("The board look like this: \n")

	for i in range(3):
		print(" ", end=' ')
		for j in range(3):
			if board[i*3+j] == 1:
				print('X', end=' ')
			elif board[i*3+j] == 0:
				print('O', end=' ')	
			elif board[i*3+j] != -1:
				print(board[i*3+j]-1, end=' ')
			else:
				print(' ', end=' ')
			
			if j != 2:
				print(" | ", end=' ')
		print()
		
		if i != 2:
			print("-----------------")
		else: 
			print() 
			
def print_instruction():
	print("Please use the following cell numbers to make your move")
	print_board([2,3,4,5,6,7,8,9,10])


def get_input(turn):

	valid = False
	while not valid:
		
			user = input("Where would you like to place " + turn + " (1-9)? ")
			if user.isdigit() and int(user) >= 1 and int(user) <= 9:
				return int(user)-1
			else:
				print("That is not a valid move! Please try again.\n")
				print_instruction()
		
		
def check_win(board):
	win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	for each in win_cond:
		
			if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
				return board[each[0]-1]
		
	return -1

def quit_game(board,msg):
	print_board(board)
	print(msg)
	quit()

def play():
	
	# setup game
	# alternate turns
	# check if win or end
	# quit and show the board
	
	print_instruction()

	board = []
	for i in range(9):
		board.append(-1)

	first = input("Who's first X or O : ")
	move = 0
	while True:

		# print board
		print_board(board)
		
		if first == 'X':
			print("Turn number " + str(move+1))
			if move % 2 == 0:
				turn = 'X'
			else:
				turn = 'O'
		if first == 'O':
			print("Turn number " + str(move+1))
			if move % 2 == 0:
				turn = 'O'
			else:
				turn = 'X'
		

		# get user input
		user = get_input(turn)
		while board[user] != -1:
			print("Invalid move! Cell already taken. Please try again.\n")
			user = get_input(turn)
		board[user] = 1 if turn == 'X' else 0

		# advance move and check for end game
		move += 1
		if move > 4:
			winner = check_win(board)
			if winner != -1:
				out = "The winner is " 
				out += "X" if winner == 1 else "O" 
				out += " :)"
				quit_game(board,out)
			elif move == 9:
				quit_game(board,"No winner :(")
play()

