# Tic Tac Toe

import re

def printboard():
    print('| |0|1|2|')
    for row in board:
        s = '|'
        for column in board[row]:
            s += column + '|'
        print('|' + row + s)


def checkforwins(player):     
    boardString = ""
    
    for row in board:
        for column in board[row]:
            boardString += column
            
    winningPatterns = [re.compile(player + '{3}[\w\s]{6}'),
                       re.compile('[\w\s]{3}' + player + '{3}[\w\s]{3}'),
                       re.compile('[\w\s]{6}' + player + '{3}'),
                       re.compile(player + '[\w\s]{2}' + player + '[\w\s]{2}' + player + '[\w\s]{2}'),
                       re.compile('[\w\s]' + player + '[\w\s]{2}' + player + '[\w\s]{2}' + player + '[\w\s]'),
                       re.compile('[\w\s]{2}' + player + '[\w\s]{2}' + player + '[\w\s]{2}' + player),
                       re.compile(player + '[\w\s]{3}' + player + '[\w\s]{3}' + player),
                       re.compile('[\w\s]{2}' + player + '[\w\s]' + player + '[\w\s]' + player + '[\w\s]{2}')]

    for pattern in winningPatterns:
        if pattern.search(boardString) != None:
            printboard()
            print("Player " + player + " wins!")
            return True
        if " " not in boardString:
            printboard()
            print("Cat's Game, no winners.")
            return True
    return False
            
        
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
##        if checkforwins():
##            break
        print("")
        player = (player1 if turn == 1 else player2)
        location = input('Player ' + player + ', enter a location: ')
        if board[location[0]][int(location[1])] != ' ':
            print('*'*10 + 'That location is already taken. Choose again.' + '*'*10)
            continue
        board[location[0]][int(location[1])] = player if board[location[0]][int(location[1])] == ' ' else board[location[0]][int(location[1])]
        if checkforwins(player):
            break
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
