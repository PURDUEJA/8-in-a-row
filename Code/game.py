"""
Ultimate Connect.
Creators: Jacob Purdue and Nick Kho
Start date: Thursday 20th July
"""
import sys
import time

grid = []
for y in range(12):

    grid_list = []

    for x in range(14):
        grid_list.append(0)

    grid.append(grid_list)


def printGrid():
    """"""
    print("\n".join(map(str, grid)))


def putCounter(collumn, player):
    """"""
    if grid[0][collumn] != 0:
        return "failed"

    else:

        underneath = False

        row = 0
        # print(row, collumn)

        while underneath is False:

            if isUnderBlocked(row, collumn):
                place(row, collumn, player)
                # print("placed")
                underneath = True
            else:
                row += 1


def isUnderBlocked(row, collumn):
    """"""
    try:
        test = (grid[row + 1][collumn] != 0)
    except IndexError:
        # print("indexerror")
        return True
    if test is True:

        return True

    else:

        return False


def checkConnection():
    for row in grid:
        for collumn in grid:
            if collumn != 0:
                pass


# 14 x 12

def checkSurroundings(collumn, row, player):
    print("checking: ", collumn, row)
    valids = []
    startingRow = row - 2
    print(grid[11][1])

    # Offset by two because of the loop of 3. Actually starts at -1.
    for i in range(3):
        print(startingRow, "the starting row")
        startingRow += 1
        startingCol = collumn - 2
        for x in range(3):
            print(startingCol, "col")
            startingCol += 1
            try:
                print(startingRow, startingCol, grid[startingCol][startingRow])
                # print(grid[startingRow][startingCol])
                # print(player)
                if grid[startingCol][startingRow] is player:

                    # Add it if the coordinate is the original coordinate provided.
                    print(startingCol, collumn, startingRow, row)
                    print(startingCol is not collumn) and (startingRow is not row)
                    if (startingCol is not collumn) and (startingRow is not row):
                        valids.append([startingCol, startingRow])

            except IndexError:
                print("IndexError")
                pass
    print(valids)


def checkDiagonallyOpposite(row, col, player, checkNumber):
    rows = len(grid)
    cols = len(grid[0])

    # Check if there are 4 spaces diagonally bottom-right.
    # Row = 4
    # Max = 14
    # Check Number = 4
    # if max - row (10) <= (10) max - checkNumber:
    #   run
    if row > rows - checkNumber or col < 4:
        return False

    # Check the four diagonal squares in the bottom-right direction
    # and return the result.
    # for i in range(checkNumber):
    #     print(row+i, col-i, grid[row+i][col-i], i)
    # print(grid[8][4])
    # print(grid[9][3])
    # print(all(grid[row+i][col-i] == player for i in range(checkNumber)))
    return all(grid[row+i][col-i] == player for i in range(checkNumber))


def checkDiagonally(row, col, player, checkNumber):
    rows = len(grid)
    cols = len(grid[0])

    # Check if there are 4 spaces diagonally bottom-right.
    if row > rows - checkNumber or col > cols - checkNumber:
        return False

    # Check the four diagonal squares in the bottom-right direction
    # and return the result.

    return all(grid[row+i][col+i] == player for i in range(checkNumber))


def checkInRow(row, col, player, checkNumber):
    rows = len(grid)
    cols = len(grid[0])
    # Check if there are 4 rows to the right of the chosen.
    if col > cols - checkNumber:
        return False

    # Check the next 4 in a row and return the result.
    # print("asdf")
    # print(grid[row][col])
    # for i in range(checkNumber):
        # print(grid[row][col + i], row, (col + i))
    # print(all(grid[row][col+i] == player for i in range(checkNumber)))
    return all(grid[row][col+i] == player for i in range(checkNumber))


def checkUnderneath(row, col, player, checkNumber):
    rows = len(grid)
    cols = len(grid[0])

    # Check if there are 4 spaces underneath the chosen spot.
    if row > rows - checkNumber:
        return False

    # Check the next 4 underneath and return the result.
    return all(grid[row + i][col] == player for i in range(checkNumber))


def checkInThatDirection(col, row, originalCol, originalRow):
    x_offset = originalCol - col
    y_offset = originalRow - row


def checkWinner(checkNumber):
    winnerFound = 0
    totaltimes = 0
    winnerFoundBool = False
    while winnerFoundBool == False:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                totaltimes += 1
                players = [1, 2]
                for player in players:
                    if grid[row][col] is player:
                        # Check diagonally, horizontally, and vertically.
                        if (player if checkInRow(row, col, player, checkNumber) else 0):
                            return player

                        # winnerFoundBool = True if (winnerFound != 0) else 0

                        if (player if checkDiagonally(row, col, player, checkNumber) else 0):
                            return player

                        # winnerFoundBool = True if (winnerFound != 0) else 0
                        if (player if checkUnderneath(row, col, player, checkNumber) else 0):
                            return player

                        if (player if checkDiagonallyOpposite(row, col, player, checkNumber) else 0):
                            return player
                        # winnerFoundBool = True if (winnerFound != 0) else 0
        return winnerFound
    return winnerFound

def place(row, collumn, player):
    """"""
    grid[row][collumn] = player


# putCounter(0, 1)
putCounter(1, 1)
putCounter(2, 1)
putCounter(0, 1)
putCounter(0, 1)
putCounter(0, 1)
putCounter(2, 1)
# putCounter(3, 1)
putCounter(1, 1)
putCounter(1, 1)
putCounter(3, 2)
putCounter(3, 2)
putCounter(3, 1)
putCounter(4, 2)
putCounter(4, 2)
putCounter(4, 2)
putCounter(4, 1)
# checkSurroundings(11, 1, 1)
print(grid[11][0])
printGrid()
print("Winner Found" if checkWinner(4) else "Nothing Found")
# checkDiagonallyOpposite(8, 4, 1, 4)
# checkDiagonallyOpposite(0, 0, 1, 4)
