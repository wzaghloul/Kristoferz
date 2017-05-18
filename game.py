col = 7
row = 6
coli = col -1 # max. index in col
rowi = row -1 # max. index in row

moves = 0


#field = [][] wird definiert
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
    print ('0 1 2 3 4 5 6 \n-------------') #reference for user
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
                print ('\n---' + str(current) + 'WINS in row ' + str(a) + ' ---\n')
    # vertical:
    for a in range(row -3):    #to check each column
        for b in range (col):    #to start at each row but the top 3
            ## print (str(rowi - a) + ',' + str(b))  #to test order
            current  = field[rowi - a][b]
            if (current !=0 and current ==  field [rowi - a -1][b] and current == field [rowi - a -2][b] and current == field [rowi - a -3][b]):
                print ('\n---' + str(current) + ' WINS in column: ' + str(b) + ' ---\n')
    # posdiagonal (from bottom left to top right) /
    # negdiagonal (from top left to bottom right) \

def humanTurn():
    # raw_input() was renamed to input() - use comment the version that doesn't fit until we are sure everyone is using the newest version of python
    
    ## userInput = int(raw_input('Du bist dran. 0 bis 6 eingeben: '))
    userInput = int(input('Du bist dran. 0 bis 6 eingeben: '))
    if (movePossible(userInput)):
        for i in range(row):
        ## print (i)
            if (field[rowi - i][userInput] == 0):
                field[rowi - i][userInput] = 'H'
                printboard()
                break
    else:
        print('Spalte voll!')
        humanTurn()

# kann man MAIN nennen
for i in range (row * col):
    humanTurn()
    checkforWin()
    moves = moves +1
