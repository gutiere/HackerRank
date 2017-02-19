# Example input
# 1
# 2 1 6
# K a 2
# q c 3
# q d 1

# 1
# 2 1 1
# N B 2
# Q B 1
# Q A 4

# 1
# 4 1 0
# q a 1
# r a 2
# r b 2
# r b 1
# q d 4

# 1
# 4 1 0
# q a 4
# r b 2
# b a 2
# b b 1
# q a 1

from __future__ import print_function
from copy import deepcopy

checking = True
currentPlayer = 'w'

def main():
    # g = int(raw_input())
    g = 1

    # Find the solution for 'g' amount of games.
    for _ in range(g):
        # Instantiate and populate board.
        masterBoard = [[0 for c in range(4)] for r in range(4)]


        # m = getInfo(masterBoard)

        # m = 2
        # masterBoard[1][3] = 'Q'
        # masterBoard[1][1] = 'R'
        # masterBoard[0][1] = 'B'
        # masterBoard[1][0] = 'B'
        # masterBoard[0][0] = 'q'

        # m = 1
        # masterBoard[1][1] = 'N'
        # masterBoard[1][0] = 'Q'
        # masterBoard[0][3] = 'q'

        m = 2
        masterBoard[0][0] = 'N'
        masterBoard[3][3] = 'q'

        recursiveBoardChecking(masterBoard, m, currentPlayer)

        if (checking == True):
            print("NO")

def recursiveBoardChecking(board, counter, color):
    printBoard(board)
    print("Color: " + color)

    if (checkWhiteWin(board) == False):

        if (color == 'b'): nextPlayer = 'w'
        elif (color == 'w'): nextPlayer = 'b'

        for b in getBoards(board, color):
            if (board != None and counter != 0 and checking == True):
                recursiveBoardChecking(b, counter - 1, nextPlayer)

# Get all boards that can be made for user's turn.
def getBoards(board, color):
    global checking
    boards = []
    # Loop through entire board.
    for r in range(4):
        if (checking == False):
            break
        for c in range(4):
            if (checking == False):
                break
            # White turn
            if (color == 'w'):
                # Analyze only white pieces.
                if (board[c][r] in ['Q', 'R', 'B', 'N']):
                    boards = boards + getPieceOptions(board, c, r)
            # Black turn
            elif (color == 'b'):
                # Analyze only black pieces.
                if (board[c][r] in ['q', 'r', 'b', 'n']):
                    boards = boards + getPieceOptions(board, c, r)
            else:
                print("Incorrect player syntax.")

    return boards

# Get all boards that can be made from a specific piece.
def getPieceOptions(board, c, r):
    boards = []
    # Define possible movement for a queen.
    if (board[c][r] in ['Q', 'q']):
        boards = boards + findStraightMoves(board, c, r)
        boards = boards + findDiagonalMoves(board, c, r)
    # Define possible movement for a rook.
    elif (board[c][r] in ['R', 'r']):
        boards = boards + findStraightMoves(board, c, r)
    # Define possible movement for a bishop.
    elif (board[c][r] in ['B', 'b']):
        boards = boards + findDiagonalMoves(board, c, r)
    # Define possible movement for a knight.
    elif (board[c][r] in ['N', 'n']):
        boards = boards + findLMoves(board, c, r)

    return boards

# Find all boards associated with L movement of a piece.
def findLMoves(board, c, r):
    boards = []
    if (c - 2 >= 0):
        if (r - 1 >= 0):
            boards.append(generateNewBoard(board, c, r, c - 2, r - 1))
        if (r + 1 <= 3):
            boards.append(generateNewBoard(board, c, r, c - 2, r + 1))
    if (c + 2 <= 3):
        if (r - 1 >= 0):
            boards.append(generateNewBoard(board, c, r, c + 2, r - 1))
        if (r + 1 <= 3):
            boards.append(generateNewBoard(board, c, r, c + 2, r + 1))
    if (r - 2 >= 0):
        if (c - 1 >= 0):
            boards.append(generateNewBoard(board, c, r, c - 1, r - 2))
        if (c + 1 <= 3):
            boards.append(generateNewBoard(board, c, r, c + 1, r - 2))
    if (r + 2 <= 3):
        if (c - 1 >= 0):
            boards.append(generateNewBoard(board, c, r, c - 1, r + 2))
        if (c + 1 <= 3):
            boards.append(generateNewBoard(board, c, r, c + 1, r + 2))
    return boards

# Find all boards associated with diagonal movement of a piece.
def findDiagonalMoves(board, c, r):
    boards = []

    tempC, tempR = c, r

    # Check top left moves.
    tempC = tempC - 1
    tempR = tempR + 1
    while (tempC >= 0 and tempR <= 3):
        boards.append(generateNewBoard(board, c, r, tempC, tempR))
        tempC = tempC - 1
        tempR = tempR + 1
    tempC, tempR = c, r

    # Check top right moves.
    tempC = tempC + 1
    tempR = tempR + 1
    while (tempC <= 3 and tempR <= 3):
        boards.append(generateNewBoard(board, c, r, tempC, tempR))
        tempC = tempC + 1
        tempR = tempR + 1
    tempC, tempR = c, r

    # Check bottom left moves.
    tempC = tempC - 1
    tempR = tempR - 1
    while (tempC >= 0 and tempR >= 0):
        boards.append(generateNewBoard(board, c, r, tempC, tempR))
        tempC = tempC - 1
        tempR = tempR - 1
    tempC, tempR = c, r

    # Check bottom right moves.
    tempC = tempC + 1
    tempR = tempR - 1
    while (tempC <= 3 and tempR >= 0):
        boards.append(generateNewBoard(board, c, r, tempC, tempR))
        tempC = tempC + 1
        tempR = tempR - 1
    tempC, tempR = c, r

    return boards

# Find all boards associated with straight movement of a piece.
def findStraightMoves(board, c, r):
    boards = []
    # Check vertical moves.
    for row in range(4):
        if (board[c][row] not in ['Q', 'R', 'B', 'N']):
            boards.append(generateNewBoard(board, c, r, c, row))

    # Check horizontal moves.
    for col in range(4):
        if (board[col][r] not in ['Q', 'R', 'B', 'N']):
            boards.append(generateNewBoard(board, c, r, col, r))
    return boards

# Generate new board with the desired piece movement.
def generateNewBoard(board, c, r, newC, newR):
    newBoard = None
    invalid = False

    if (board[c][r] not in ['n', 'N']):
        # Scan through spaces between start and finish.
        if (c > newC):
            if (r > newR):
                for col in range(newC, c):
                    for row in range(newR, r):
                        invalid = checkTeamConflict(board, c, r, col, row)
            elif (r < newR):
                for col in range(newC, c):
                    for row in range(newR, r, -1):
                        invalid = checkTeamConflict(board, c, r, col, row)
            else:
                for col in range(newC, c):
                    invalid = checkTeamConflict(board, c, r, col, r)
        elif (c < newC):
            if (r > newR):
                for col in range(newC, c, -1):
                    for row in range(newR, r):
                        invalid = checkTeamConflict(board, c, r, col, row)

            elif (r < newR):
                for col in range(newC, c, -1):
                    for row in range(newR, r, -1):
                        invalid = checkTeamConflict(board, c, r, col, row)
            else:
                for col in range(newC, c, -1):
                    invalid = checkTeamConflict(board, c, r, col, r)
        else:
            if (r > newR):
                for row in range(newR, r):
                    if (checkTeamConflict(board, c, r, c, row) == True):
                        invalid = True
            elif (r < newR):
                for row in range(newR, r, -1):
                    invalid = checkTeamConflict(board, c, r, c, row)
    # Check if a teammate exists between locations.
    if (not invalid):
        newBoard = deepcopy(board)
        newBoard[newC][newR] = newBoard[c][r]
        newBoard[c][r] = '0'
    return newBoard

def checkTeamConflict(board, c ,r, newC, newR):
    if (board[c][r] in ['Q', 'R', 'B', 'N']):
        if (board[newC][newR] in ['Q', 'R', 'B', 'N']):
            return True
    elif (board[c][r] in ['q', 'r', 'b', 'n']):
        if (board[newC][newR] in ['q', 'r', 'b', 'n']):
            return True
    return False

# Import user input into board.
def getInfo(board):
    info = raw_input().split(" ")
    w = int(info[0])
    b = int(info[1])
    m = int(info[2])

    # Add all white pieces.
    for _ in range(w):
        info = raw_input().split(" ")
        c = convertCol(info[1])
        r = int(info[2]) - 1
        # Enter white piece into board.
        board[c][r] = info[0].upper()


    # Add all black pieces.
    for _ in range(b):
        info = raw_input().split(" ")
        c = convertCol(info[1])
        r = int(info[2]) - 1
        # Enter black piece into board.
        board[c][r] = info[0].lower()

    return m

# Convert letter indices to array indices.
def convertCol(Letter):
    return ord(Letter.upper()) - ord('A')

# Print the board with (0,0) in the bottom left.
def printBoard(board):
    if (board != None):
        for r in range(4, 0, -1):
            for c in range(4):
                print(board[c][r - 1], end='')
            print()
        print()

def checkWhiteWin(board):
    win = True
    if (board != None):
        for r in range(4):
            for c in range(4):
                if (board[c][r] == 'q'):
                    win = False
        global checking
        if (win == True and checking == True):
            print("YES")
            checking = False
    return win

if __name__ == "__main__":
    main()
