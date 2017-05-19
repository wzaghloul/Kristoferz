col = 7
row = 6
coli = col -1 # max. index in col
rowi = row -1 # max. index in row
human = 0
ans = str(input('Möchtest du anfangen? (\'j\' / \'n\')'))[0].lower()
moves = 0

#field = [zeile][spalte] wird definiert
field = [[i * j for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        field[i][j] = 0

# field Ursprung oben links
#   0 1 2 3 4 5 6 
# 0 . . . . . . .
# 1 . . . . . . .
# 2 . . . . . . . 
# 3 . . . . . . .
# 4 . . . . . . .
# 5 . . . . . . .

def printboard ():  #Update Board
    print ('\n\n0 1 2 3 4 5 6 \n-------------') #reference for user
    for n in field:
        print(' '.join([str(elem) for elem in n])) #print(field[i][j])

printboard()

def movePossible(spalte):
  if (field[0][spalte] == 0):
    return True
  else:
    return False

def checkforWin():
    # horizontal:
    for a in range(row):    #to check each row
      for b in range (col - 3):   #to start at each columns but the last 3 to the right
        current = field [rowi - a][b]
        if (current != 0 and current == field [rowi - a][b + 1] and current == field [rowi - a][b + 2] and current == field [rowi - a][b + 3]):
          print ('\n---' + str(current) + ' WINS in row ' + str(a) + ' ---\n')
          return True
    # vertical:
    for a in range(row -3):    #to check each column
      for b in range (col):    #to start at each row but the top 3
        ## print (str(rowi - a) + ',' + str(b))  #to test order
        current  = field[rowi - a][b]
        if (current !=0 and current ==  field [rowi - a -1][b] and current == field [rowi - a -2][b] and current == field [rowi - a -3][b]):
          print ('\n---' + str(current) + ' WINS in column: ' + str(b) + ' ---\n')
          return True
    # posdiagonal (from bottom left to top right) /
    for a in range(row - 3):
      for b in range(col - 3):
        ## print (str(rowi - a) + ',' + str(b))
        current  = field[rowi - a][b]
        if (current !=0 and current == field[rowi - a -1][b +1] and current == field [rowi - a -2][b +2] and current == field [rowi - a -3][b +3]):
          print ('\n---' + str(current) + ' WINS diagonally ---\n')
          return True
    # negdiagonal (from top left to bottom right) \
    for a in range(row - 3):
      for b in range(col - 3):
        ## print (str(a) + ',' + str(b))
        current  = field[a][b]
        if (current !=0 and current == field[a +1][b +1] and current == field [a +2][b +2] and current == field [a +3][b +3]):
          print ('\n---' + str(current) + ' WINS diagonally ---\n')
          return True


def humanTurn(chip):
  retry = True
  while(retry):
    retry = False
    userInput = int(input('Du bist dran. 0 bis 6 eingeben: '))
    if (not(userInput <= row and userInput >= 0)):
      print('Ich habe gesagt zwischen 0 und 6!')
      retry = True
    if (movePossible(userInput)):
        for i in range(row):
        ## print (i)
            if (field[rowi - i][userInput] == 0):
                field[rowi - i][userInput] = chip
                printboard()
                break
    else:
        print('Spalte voll!')
        retry = True

# kann man MAIN nennen
for i in range (row * col):
  if (not(checkforWin())):
    if (ans == 'j' or ans == 'y'):
      human = 0
    else:
      human = 1
    if (moves % 2 == human):
      humanTurn('H')
    else:
      humanTurn('X')
      # bis computerTurn gemacht wird
    moves += 1
  else:
    break
