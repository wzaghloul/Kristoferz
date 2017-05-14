# 4Gewinnt Kristoferz

# Variables
col = 7
row = 6
empty_chip = '.'
human_chip = 'X'
pc_chip = 'O'
moves = 0
playerstart = input ("Who shall start? Please write Pc (1) or Human (2): ")
while str.lower(playerstart) != "pc" and str.lower(playerstart) != "human" and playerstart != str(1) and playerstart != str(2):
	print("Invalid input, please try again.")
	playerstart = input ("Who shall start? Please write Pc (1) or Human (2): ")
level = input ("Select difficulty. Random (1), Middle (2), Hard (3), Godlike (4): ")
while str.lower(level) != "random" and str.lower(level) != "middle" and str.lower(level) != "hard" and str.lower(level) != "godlike" and level != str(1) and level != str(2) and level != str(3) and level != str(4):
	print("Invalid input, please try again.")
	level = input ("Select difficulty. Random (1), Middle (2), Hard (3), Godlike (4): ")
# Diesen Teil kann man wahrscheinlich schöner schreiben :)
turn = 0

# 7 columns x 6 rows Field
field = [[i * j for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        field[i][j] = empty_chip
for n in field:
	print(' '.join([str(elem) for elem in n]))
print("1 2 3 4 5 6 7")

def human_turn(human_move):
# Human move (geht nicht)
	""" 
	human_move = input ("Select a number between 1 and 7: ")
	if human_move<1 or human_move>7:
		print("Invalid move")
		human_turn(human_move)
	for i in range(row):
		if field[human_move][i] == empty_chip:
			field[human_move][i] = human_chip
		else:
			print("Invalid move")
			human_turn(human_move)
	moves+=1 
	"""	
	return[human_move];

def pc_turn(pc_move):
# Pc move (in Bearbeitung)
	"""
	pc_move = random.randint(1,7)

	moves+=1 
	"""
	return[pc_move];

def startplayer(playerstart): 
# Input to select starting player. Kann auch gross geschrieben werden oder mit 1 und 2
# Eventuell input durch Touch-Screen
	if str.lower(playerstart) == "pc" or playerstart == str(1):
		print ("Computer starts")
	elif str.lower(playerstart) == "human" or playerstart == str(2):
		print ("Human starts")
	return [playerstart];
startplayer(playerstart)

def turn(playerstart,moves):
# Zeigt wer dran ist
	if  (str.lower(playerstart) == "human" or playerstart == str(2)) and moves%2 == 0:
		turn = "human"
		print ("It´s your turn. ")
		human_turn(human_move)
	elif (str.lower(playerstart) == "pc" or playerstart == str(1)) and moves%2 == 1:
		turn = "human"
		print ("It´s your turn. ")
		human_turn(human_move)
	else:
		turn = "pc"
		pc_turn(pc_move)
	return [turn];
turn(playerstart,moves)
