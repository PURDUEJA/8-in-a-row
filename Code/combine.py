"""
Ultimate Connect.
Creators: Jacob Purdue and Nick Kho
Start date: Thursday 20th July
"""
import pygame
from Button import Button
grid = []

def resetGrid():
    grid = []
    for y in range(7):

        grid_list = []

        for x in range(8):
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
                return (row)
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
    # Grid Placement
    print("Counter placed at ({}, {})".format(collumn, row))


def clearTerminal():
    for i in range(20):
        print("\n")


def playerTurnLoop():
    resetGrid()
    PLAYERS = [1, 2]
    gameOver = False

    """ Grid Creation goes here """
    # | grid | is the board size: 8x7
    # Sync GUI to | grid |.
    # | grid | is a 2d list.
    # To get the value of the grid, use grid[y][x]. e.g check the space (2, 6): print(grid[6][2])
    # example function: UpdateGUI(grid)
    print(grid)

    # Iterate until the game has concluded.
    while gameOver == False:

        # Switch between each players' turns.
        for player in PLAYERS:

            # Run until a valid placement is found.
            chosenSquare = False
            while chosenSquare is False:
                try:
                    clearTerminal()
                    printGrid()
                    desiredPlacement = int(input(
                        "Player {} turn.\nType a collumn to drop in ({})".format(player, ("1-" + str(len(grid[0]))))))
                    desiredPlacement -= 1
                    # print(desiredPlacement)
                    # print(0 <= desiredPlacement)
                    # print(desiredPlacement <= len(grid[0]))
                    if 0 <= desiredPlacement and desiredPlacement <= len(grid[0]) and grid[0][desiredPlacement] == 0:
                        chosenSquare = True
                except:
                    pass

            # Continues once a valid coordinate has been determined.

            """ Counter Placement on GUI Goes Here """
            """ Custom GUI Selection for Counter Placement can go here"""
            row = putCounter(desiredPlacement, player)
            print("DEBUG: Placed value of {} at x:{}".format(desiredPlacement, player))
            # Note
            # | desiredPlacement | is the column value (x). This will drop a counter at the lowest position if there is valid space.
            # | row | is the (y).
            # | desiredPlacement | can be seen as the x value of the grid.
            # | grid | variable is the board. To get the value of the grid, use grid[y][x]. e.g check the space (2, 6): print(grid[6][2])
            # | grid |'s size is 7 by 6
            # | player| is the value of the counter being dropped.
            print(player)
            print(desiredPlacement)
            # Print the value of | grid | and | desiredPlacement |
            # | printGrid() | to check the grid in the terminal

            # Easiest way is to sync the grids and have no counter animation
            # example function: UpdateGUI(grid)

            # Can have animated counter placement:
            # example function: DropCounterGUI(row, desiredPlacement)

            # Winner Checks
            gameOver = True if checkWinner(4) else False
            if gameOver == True:
                clearTerminal()
                printGrid()
                print("Game Over! {} Wins.".format(player))

                """ GUI Game Over Screen Goes Here """
                # | player | is the player number that won.
                # example function: displayWinnerScreen(player)

                return True


# Start the game
""" Starting screen function can go here. To trigger the game, run playerTurnLoop()"""


pygame.init()
# Sets window settings resolution and title.
current_resolution = (1280, 720)
SCREEN = pygame.display.set_mode(current_resolution, pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Connect")

# Background image
BG = pygame.image.load("../assets/tempBG_1280x720.png")
# Board
BOARD8X7 = pygame.image.load("../assets/Board8x7.drawio.png")
# Counters
BLUE = pygame.image.load("../assets/CounterBlue.png")
RED = pygame.image.load("../assets/CounterRed.png")
# Resoltuion
resolution = (811, 811)
board = int
# Set
ROW_COUNT = 7
COLUMN_COUNT = 8
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
turn = 0

size = (width, height)

def get_font(size):  # Returns font in the desired size

    return pygame.font.Font("../assets/DiloWorld-mLJLv.ttf", size)

def main_menu():
    """Main menu for the game."""
    new_resolution = (1280, 720)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    while True:
        SCREEN.blit(BG, (0, 0))

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
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

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
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_GAME.checkForInput(PLAY_MOUSE_POS):
                    game(board)

        pygame.display.update()

def game(board):
    """Plays the game itself"""
    new_resolution = (811, 911)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    current_resolution = new_resolution
    board = BOARD8X7

    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(board, (0, 100))

        # Return to main menu.
        TEMP_BACK = Button(image=None, pos=(405, 861),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        TEMP_BACK.changeColor(GAME_MOUSE_POS)
        TEMP_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if TEMP_BACK.checkForInput(GAME_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEMOTION:
                print(RED, BLUE, board)
                posx = event.pos[0]
                if turn == 0:
                    SCREEN.blit(RED, (posx, int(SQUARESIZE / 2)))
                else:
                    SCREEN.blit(BLUE, (posx, int(SQUARESIZE / 2)))

        pygame.display.update()


def options():
    """Allows the user to change some settings, such as colourblindness."""
    while True:
        # Gets mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Main header text.
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Button to return to main menu from options.
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights options text while mouse hovers
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()


        pygame.display.update()

main_menu()

