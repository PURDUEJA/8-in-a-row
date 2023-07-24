"""
Ultimate Connect.
Creators: Jacob Purdue and Nick Kho
Start date: Thursday 20th July
"""

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
        print(row, collumn)

        while underneath is False:

            if isUnderBlocked(row, collumn):
                place(row, collumn, player)
                print("placed")
                underneath = True
            else:
                row += 1


def isUnderBlocked(row, collumn):
    """"""
    try:
        test = (grid[row + 1][collumn] != 0)
    except IndexError:
        print("indexerror")
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


def checkSurroundings(row, collumn, player):
    valids = []
    startingRow = row - 2
    for i in range(3):
        startingRow + 1
        startingCol = collumn - 2
        for x in range(3):
            startingCol + 1
            try:
                print(grid[startingRow][startingCol])
                print(player)
                if grid[startingRow][startingCol] is player:
                    valids.append([startingRow, startingCol])
            except IndexError:
                pass
    print(valids)

def checkWinner():
    for row in grid:
        for collumn in grid:
            if collumn != 0:
                pass


def place(row, collumn, player):
    """"""
    grid[row][collumn] = player

putCounter(0, 1)
putCounter(1, 1)
putCounter(2, 1)
checkSurroundings(13, 1, 1)
printGrid()