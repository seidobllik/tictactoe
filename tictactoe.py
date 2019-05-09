# Tic Tac Toe


def printboard():
    print('| |0|1|2|')
    for row in board:
        s = '|'
        for column in board[row]:
            s += column + '|'
        print('|' + row + s)

def checkforwins():
    pass
    
        
board = {'a':[' ', ' ', ' '],
         'b':[' ', ' ', ' '],
         'c':[' ', ' ', ' ']}
player1 = 'X'
player2 = 'O'

turn = 1 # multiply by -1 each turn to change turns. p1 = 1, p2 = -1.
print("Please enter your location choice in the following format:\n" +
      "\t[row letter][column number]\n" +
      "\tex. A2, or C3\n")

while True:
    try:
        printboard()
        checkforwins()
        print("")
        player = (player1 if turn == 1 else player2)
        location = input('Player ' + player + ', enter a location: ')
        if board[location[0]][int(location[1])] != ' ':
            print('*'*10 + 'That location is already taken. Choose again.' + '*'*10)
            continue
        board[location[0]][int(location[1])] = player if board[location[0]][int(location[1])] == ' ' else board[location[0]][int(location[1])]
        turn *= -1
    except IndexError:
        print('*'*10 + 'Please check your column value and try again.' + '*'*10)
        continue
    except KeyError:
        print('*'*10 + 'Please check your row value and try again.' + '*'*10)
        continue
    except ValueError:
        print('*'*10 + 'Please check your input format and try again.' + '*'*10)
        continue
