col = 7
row = 6
moves = 0


#field = [[]]
field = [[i * j for j in range(col)] for i in range(row)]
#print(field[i][j])
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

def printboard ():
  for n in field:
    print(' '.join([str(elem) for elem in n])) #print(field[i][j])

printboard()

def movePossible(x):
  if (field[0][x] == 0):
    return True
  else:
    return
  
def humanTurn ():
  userInput = int(raw_input('Du bist dran. 0 bis 6 eingeben: '))
  if (movePossible(userInput)):
    for i in range(row):
      # print (i)
      if (field[row - i - 1][userInput] == 0):
        field[row - i - 1][userInput] = 'H'
        printboard()
        break
  else:
    print('Spalte voll!')
    humanTurn()


