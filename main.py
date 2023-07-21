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


def printGrid(list):
    print("\n".join(map(str, list)))


printGrid(grid)


def putCounter(collumn):
    if grid[0][collumn] is 0:

        return "failed"

    else:

        underneath = False

        row = 0

        while underneath is False:

            if checkUnder(grid[0], row):
                place()


def checkUnder(grid_collumn_list, row):
    try:

        if grid_collumn_list[row - 1] is 0:

            return True

        else:

            return False

    except IndexError():

        return False


def place(grid_collumn_list, row, player):
    grid_collumn_list[row] = player