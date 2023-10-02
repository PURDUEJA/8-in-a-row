"""
Ultimate Connect.
Creators: Jacob Purdue and Nick Kho
Start date: Thursday 20th July
"""
import time
import asyncio
from guiGame import image, GUIclass
import numpy as np
import pygame
import sys
import math
from Button import Button
from pygame import mixer

pygame.init()
# Sets window settings resolution and title.
current_resolution = (1280, 720)
SCREEN = pygame.display.set_mode(current_resolution, pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Connect")

# Background image
BG = pygame.image.load("../assets/tempBG_1280x720.png")
BOARD8X7 = pygame.image.load("../assets/Board8x7.drawio.png")
BOARD9X8 = pygame.image.load("../assets/Board9x8.drawio.png")
BOARD10X9 = pygame.image.load("../assets/Board10x9.drawio.png")
BOARD11X10 = pygame.image.load("../assets/Board11x10.drawio.png")
BOARDTEST = pygame.image.load("../assets/BOARDTEST.png")
BOARDTEST2 = pygame.image.load("../assets/BOARDTEST2.png")
# Counters
blue = pygame.image.load("../assets/CounterBlue.png")
yellow = pygame.image.load("../assets/CounterYellow.png")
red = pygame.image.load("../assets/CounterRed.png")
boards = []
board = int
boards.extend([BOARD8X7, BOARD9X8, BOARD10X9, BOARD11X10])

# Music

# Initiate mixer.
mixer.init()
click = pygame.mixer.Sound("../assets/Click.wav")
pygame.mixer.music.load("../assets/Approach 3.mp3")
pygame.mixer.music.play()
DEFAULT_VOLUME = 0.5
mixer.music.set_volume(DEFAULT_VOLUME)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def spawnCounter():
    print("asdf")


def refresh():
    pass


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
gridGUI = GUIclass(811, 711)
#putCounter(0, 1)
#putCounter(0, 2)
putCounter(7, 1)
putCounter(7, 2)
gridGUI.updateToGrid(grid)



async def playerTurnLoop():
    startMouseCapture()
    PLAYERS = [1, 2]
    gameOver = False

    board = image("board", pygame.image.load("../assets/Board8x7.drawio.png"), 3, 0, 0)
    #p1 = image("p1", pygame.image.load("CounterRed.png"), 2, 0, 0)
    #p2 = image("p2", pygame.image.load("CounterBlue.png"), 2, 0, 0)

    gridGUI.images["board"] = board
    #gridGUI.images["p1"] = p1
    #gridGUI.images["p2"] = p2
    gridGUI.update()
    await gridGUI.start()
    await getMouseInput()
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



def get_font(size):  # Returns font in the desired size

    return pygame.font.Font("../assets/DiloWorld-mLJLv.ttf", size)


def main_menu():
    """Main menu for the game."""
    new_resolution = (1280, 720)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    width = 1280
    height = 720
    speed = [1, 1]
    clock = pygame.time.Clock()
    ball = pygame.image.load("../assets/CounterYellow.png").convert()
    ballrect = ball.get_rect()

    while True:
        # Gets position of the mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Ultimate Connect", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # All buttons on main menu.
        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Changes colour of button when hovered by mouse.
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Runs button when clicked.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                mixer.music.stop()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    pygame.quit()
                    sys.exit()
        # Background animation
        # https://www.geeksforgeeks.org/stimulate-bouncing-game-using-pygame/
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        SCREEN.blit(ball, ballrect)
        #pygame.display.flip()
        clock.tick(60)

        pygame.display.update()


def play():
    """Puts user into the start game menu"""
    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # Fills screen with black to place anything over.
        SCREEN.fill("black")

        # Main header text.
        PLAY_TEXT = get_font(45).render("Game Setup.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # Return to main menu.
        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Continue to game
        START_GAME = Button(image=None, pos=(640, 160),
                            text_input="Start game", font=get_font(75), base_color="White", hovering_color="Green")

        # Highlights options text while mouse hovers
        START_GAME.changeColor(PLAY_MOUSE_POS)
        START_GAME.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_GAME.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    mixer.music.pause()
                    game()

        pygame.display.update()


turn = 0


def game():
    """Plays the game itself"""
    new_resolution = (811, 711)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    current_resolution = new_resolution
    asyncio.run(main())
    pygame.display.update()


def options():
    """Allows the user to change some settings, such as colourblindness."""
    while True:
        current_volume = round(pygame.mixer.music.get_volume(), 1)

        # Gets mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Main header text.
        OPTIONS_TEXT = get_font(45).render("Options.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Master volume text.
        MUSIC_TEXT = get_font(35).render("Music Volume.", True, "Black")
        MUSIC_RECT = MUSIC_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(MUSIC_TEXT, MUSIC_RECT)

        # Current volume text.
        VOL_TEXT = get_font(35).render(str(current_volume * 100), True, "Black")
        VOL_RECT = VOL_TEXT.get_rect(center=(640, 310))
        SCREEN.blit(VOL_TEXT, VOL_RECT)

        # Button to return to main menu from options.
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights options text while mouse hovers
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Volume adjust buttons
        VOL_UP = Button(image=None, pos=(760, 360),
                        text_input="+", font=get_font(75), base_color="Black", hovering_color="Green")

        VOL_DOWN = Button(image=None, pos=(520, 360),
                          text_input="-", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights options text while mouse hovers
        VOL_UP.changeColor(OPTIONS_MOUSE_POS)
        VOL_UP.update(SCREEN)
        VOL_DOWN.changeColor(OPTIONS_MOUSE_POS)
        VOL_DOWN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Button click for decreasing volume.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOL_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    new_volume = round(current_volume - 0.1, 1)
                    if new_volume > 1:
                        new_volume = 1.0
                    elif new_volume < 0:
                        new_volume = 0.0
                    mixer.music.set_volume(new_volume)

            # Button click for increasing volume.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOL_UP.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    new_volume = round(current_volume + 0.1, 1)
                    if new_volume > 1:
                        new_volume = 1.0
                    elif new_volume < 0:
                        new_volume = 0.0
                    mixer.music.set_volume(new_volume)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    main_menu()

        pygame.display.update()

main_menu()
