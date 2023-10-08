import time
import pygame
import asyncio
import math
from guiGame import image, GUIclass


def spawnCounter():
    print("asdf")


def refresh():
    pass


"""
Ultimate Connect.
Creators: Jacob Purdue and Nick Kho
Start date: Thursday 20th July
"""




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
        test = grid[row + 1][collumn] != 0
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
    return all(grid[row + i][col - i] == player for i in range(checkNumber))


def checkDiagonally(row, col, player, checkNumber):
    rows = len(grid)
    cols = len(grid[0])

    # Check if there are 4 spaces diagonally bottom-right.
    if row > rows - checkNumber or col > cols - checkNumber:
        return False

    # Check the four diagonal squares in the bottom-right direction
    # and return the result.

    return all(grid[row + i][col + i] == player for i in range(checkNumber))


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
    return all(grid[row][col + i] == player for i in range(checkNumber))


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
                        if player if checkInRow(row, col, player, checkNumber) else 0:
                            return player

                        # winnerFoundBool = True if (winnerFound != 0) else 0

                        if (
                            player
                            if checkDiagonally(row, col, player, checkNumber)
                            else 0
                        ):
                            return player

                        # winnerFoundBool = True if (winnerFound != 0) else 0
                        if (
                            player
                            if checkUnderneath(row, col, player, checkNumber)
                            else 0
                        ):
                            return player

                        if (
                            player
                            if checkDiagonallyOpposite(row, col, player, checkNumber)
                            else 0
                        ):
                            return player
                        # winnerFoundBool = True if (winnerFound != 0) else 0
        return winnerFound
    return winnerFound


def place(row, collumn, player):
    """"""
    grid[row][collumn] = player
    placedCounters.append([row, collumn])


def clearTerminal():
    for i in range(20):
        print("\n")


async def getMouseInput():
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    print(f"Mouse clicked at position ({x}, {y})")

def getPercentage(self, max, number2, percentiles):
    # 700, 50, 7
    result = max / percentiles  # 700 / 7 = 100
    result = number2 / result  # 50 / 100 = 0.5
    result = math.floor(result)  # 0
    return result

async def startMouseCapture():
    screenX = 811
    screenY = 711
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    x, y = pygame.mouse.get_pos()

                    x_coord = getPercentage(screenX, x, 8)
                    y_coord = getPercentage(screenY, y, 7)
                    print(f"Mouse clicked at position ({x_coord}, {y_coord}) asdfasdf")
                    print(grid[0][x_coord])
                    if (
                        grid[0][x_coord] == 0
                    ):
                        putCounter(x_coord, playerTurn)
                        print("lmao")
                    gridGUI.updateToGrid(grid)


placedCounters = []
grid = []
for y in range(7):
    grid_list = []

    for x in range(8):
        grid_list.append(0)

    grid.append(grid_list)
playerTurn = 1
gridGUI = GUIclass(1011, 711)
#putCounter(0, 1)
#putCounter(0, 2)
gridGUI.updateToGrid(grid)
gridGUI.spawnPowerups()
gridGUI.updateToGrid(grid)
gridGUI.update()




async def playerTurnLoop():
    # startMouseCapture()
    PLAYERS = [1, 2]
    gameOver = False

    board = image("board", pygame.image.load("Board8x7.drawio.png"), 3, 0, 0)
    #p1 = image("p1", pygame.image.load("CounterRed.png"), 2, 0, 0)
    #p2 = image("p2", pygame.image.load("CounterBlue.png"), 2, 0, 0)

    gridGUI.images["board"] = board
    #gridGUI.images["p1"] = p1
    #gridGUI.images["p2"] = p2
    gridGUI.update()
    winner = await gridGUI.start()
    font = pygame.font.Font(None, 100)
    match winner:
        case 1:
            color = (255, 0, 0)
        case 2:
            color = (0, 0, 255)
    text = font.render(f"Player {winner} wins", True, color)
    gridGUI.screen.blit(text, (300, 300))
    gridGUI.test()
    print(f"Winner is {winner}")
    # pygame.display.update()
    await getMouseInput()






    # This code doesn't do anything  lol
    gameOver = True
    # gridGUI.update()
    while gameOver == False:
        for player in PLAYERS:
            chosenSquare = False
            while chosenSquare is False:
                try:
                    clearTerminal()
                    printGrid()
                    desiredPlacement = int(
                        input(
                            "Player {} turn.\nType a collumn to drop in ({})".format(
                                player, ("1-" + str(len(grid[0])))
                            )
                        )
                    )
                    desiredPlacement -= 1
                    # print(desiredPlacement)
                    # print(0 <= desiredPlacement)
                    # print(desiredPlacement <= len(grid[0]))
                    if (
                        0 <= desiredPlacement
                        and desiredPlacement <= len(grid[0])
                        and grid[0][desiredPlacement] is 0
                    ):
                        chosenSquare = True
                except:
                    pass
            putCounter(desiredPlacement, player)
            gameOver = True if checkWinner(4) else False
            if gameOver == True:
                clearTerminal()
                printGrid()
                print("Game Over! {} Wins.".format(player))
                return True


async def main():
    # putCounter(0, 1)
    # checkSurroundings(11, 1, 1)
    printGrid()
    print("Winner Found" if checkWinner(4) else "Nothing Found")
    await playerTurnLoop()
    # checkDiagonallyOpposite(8, 4, 1, 4)
    # checkDiagonallyOpposite(0, 0, 1, 4)


asyncio.run(main())

pygame.quit()
