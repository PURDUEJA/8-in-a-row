"""
Ultimate Connect.
Creators: Jacob Purdue and Nick Kho
Start date: Thursday 20th July
"""
import time
import asyncio
from guiGame import image, GUIclass
import pygame
import sys
import math
from Button import Button
from pygame import mixer

pygame.init()
# Sets window settings resolution and title.
current_resolution = (1280, 720)
SCREEN = pygame.display.set_mode(current_resolution)
pygame.display.set_caption("Ultimate Connect")
# Background
BG = pygame.image.load("../assets/Background.png")
# Counters
blue = pygame.image.load("../assets/CounterBlue.png")
yellow = pygame.image.load("../assets/CounterYellow.png")
red = pygame.image.load("../assets/CounterRed.png")
purple = pygame.image.load("../assets/CounterPurple.png")
green = pygame.image.load("../assets/CounterGreen.png")
pink = pygame.image.load("../assets/CounterPink.png")
getcounter = pygame.image.load("../assets/GetCounter.png")
skipturn = pygame.image.load("../assets/SkipTurn.png")
taketurn = pygame.image.load("../assets/TakeTurn.png")

# Adjusted sizes for displaying in options
blue_display = pygame.transform.smoothscale(blue, (40, 40))
yellow_display = pygame.transform.smoothscale(yellow, (40, 40))
red_display = pygame.transform.smoothscale(red, (40, 40))
purple_display = pygame.transform.smoothscale(purple, (40, 40))
green_display = pygame.transform.smoothscale(green, (40, 40))
pink_display = pygame.transform.smoothscale(pink, (40, 40))

# Default colourblind
selcol1 = "Black"
selcol2 = "Black"
selcol3 = "Black"


# Music
# Initiate mixer.
mixer.init()
click = pygame.mixer.Sound("../assets/Click.wav")
pygame.mixer.music.load("../assets/Music.mp3")
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






async def playerTurnLoop():
    placedCounters = []
    grid = []
    for y in range(7):
        grid_list = []

        for x in range(8):
            grid_list.append(0)

        grid.append(grid_list)
    playerTurn = 1
    gridGUI = GUIclass(1011, 711)
    # putCounter(0, 1)
    # putCounter(0, 2)
    gridGUI.updateToGrid(grid)
    gridGUI.spawnPowerups()
    gridGUI.updateToGrid(grid)
    gridGUI.update()
    # startMouseCapture()
    PLAYERS = [1, 2]
    gameOver = False

    board = image("board", pygame.image.load("../assets/Board.png"), 3, 0, 0)
    #p1 = image("p1", pygame.image.load("CounterRed.png"), 2, 0, 0)
    #p2 = image("p2", pygame.image.load("CounterBlue.png"), 2, 0, 0)

    gridGUI.images["board"] = board
    #gridGUI.images["p1"] = p1
    #gridGUI.images["p2"] = p2
    gridGUI.update()
    if bruh123 == 123:
        winner = await gridGUI.start()
        gridGUI.test()
        return winner
    else:
        test = await gridGUI.start()
        gridGUI.test()
    #await asyncio.sleep(5)
    # pygame.display.update()


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
    running = "ye"
    while running == "ye":
        global bruh123
        bruh123 = 1
        await playerTurnLoop()
        bruh123 = 123
        lol = winner_screen()
        if lol == "bruh":
            pass
        else:
            running = "no"

    # checkDiagonallyOpposite(8, 4, 1, 4)
    # checkDiagonallyOpposite(0, 0, 1, 4)

def get_font(size):  # Returns font in the desired size

    return pygame.font.Font("../assets/Font.ttf", size)


def main_menu():
    """Main menu for the game."""
    new_resolution = (1280, 720)
    SCREEN = pygame.display.set_mode(new_resolution)

    while True:
        # Background
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

        pygame.display.update()


def play():
    """Puts user into the start game menu"""
    new_resolution = (1280, 720)
    SCREEN = pygame.display.set_mode(new_resolution)
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

        # Highlights game start while mouse hovers
        START_GAME.changeColor(PLAY_MOUSE_POS)
        START_GAME.update(SCREEN)

        # Starts rules
        RULES_BUTTON = Button(image=None, pos=(640, 260),
                            text_input="Instructions", font=get_font(50), base_color="White", hovering_color="Green")


        START_GAME.changeColor(PLAY_MOUSE_POS)
        START_GAME.update(SCREEN)
        RULES_BUTTON.changeColor(PLAY_MOUSE_POS)
        RULES_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    main_menu()
                if START_GAME.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    mixer.music.pause()
                    game()
                if RULES_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    rules()

        pygame.display.update()




def game():
    """Plays the game itself"""
    new_resolution = (1011, 711)
    SCREEN = pygame.display.set_mode(new_resolution)
    current_resolution = new_resolution
    asyncio.run(main())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

def winner_screen():
    """Winner screen."""
    new_resolution = (1011, 711)
    SCREEN = pygame.display.set_mode(new_resolution)
    SCREEN.fill("black")
    while True:
        # Gets position of the mouse
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        WIN_TEXT = get_font(75).render("Game Over.", True, "White")
        WIN_RECT = WIN_TEXT.get_rect(center=(1011/2, 60))
        SCREEN.blit(WIN_TEXT, WIN_RECT)

        WIN_BACK = Button(image=None, pos=(1011/2, 400),
                          text_input="MAIN MENU", font=get_font(45), base_color="White", hovering_color="Green")
        WIN_AGAIN = Button(image=None, pos=(1011/2, 200),
                           text_input="Play Again", font=get_font(45), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(1011/2, 600),
                             text_input="QUIT", font=get_font(45), base_color="White", hovering_color="Green")

        WIN_AGAIN.changeColor(WIN_MOUSE_POS)
        WIN_AGAIN.update(SCREEN)
        QUIT_BUTTON.changeColor(WIN_MOUSE_POS)
        QUIT_BUTTON.update(SCREEN)
        WIN_BACK.changeColor(WIN_MOUSE_POS)
        WIN_BACK.update(SCREEN)
        # Runs button when clicked.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    mixer.music.play()
                    return "main"
                if WIN_AGAIN.checkForInput(WIN_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    return "bruh"
                if QUIT_BUTTON.checkForInput(WIN_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def rules():
    """Rules menu."""
    new_resolution = (1280, 721)
    SCREEN = pygame.display.set_mode(new_resolution)
    SCREEN.fill("White")
    while True:
        RULES_MOUSE_POS = pygame.mouse.get_pos()

        HEADER_TEXT = get_font(45).render("Instructions", True, "Black")
        HEADER_RECT = HEADER_TEXT.get_rect(center=(640, 60))
        # Move instructions down lines
        font = pygame.font.Font("../assets/Font.ttf", 30)
        text_color = "Black"
        text = "Players choose yellow or red discs. They drop the discs " \
               "into the grid by clicking at that location, starting in the middle or at the edge to " \
               "stack their colored discs upwards, horizontally, or diagonally. " \
               "Use strategy and powerups to block opponents while aiming to be the first player " \
               "to get 4 in a row to win."

        max_line_length = 90
        lines = []

        # Split the text into lines
        words = text.split()
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= max_line_length:
                current_line += word + " "
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)

        y_position = 100  # Starting y-position for the text
        for line in lines:
            text_surface = font.render(line, True, text_color)
            SCREEN.blit(text_surface, (50, y_position))
            y_position += text_surface.get_height() + 10  # vertical spacing



        pygame.display.flip()

        POWERUPS_TEXT = get_font(40).render("Powerups", True, "Black")
        POWERUPS_RECT = POWERUPS_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(HEADER_TEXT, HEADER_RECT)
        SCREEN.blit(POWERUPS_TEXT, POWERUPS_RECT)

        # Button to return to main menu from options.
        RULES_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(SCREEN)

        # Extra counter instructions
        SCREEN.blit(getcounter, (50, 320))
        GETCOUNTER_TEXT = get_font(25).render("Extra Counter", True, "Black")
        GETCOUNTER_RECT = GETCOUNTER_TEXT.get_rect(center=(250, 370))
        SCREEN.blit(GETCOUNTER_TEXT, GETCOUNTER_RECT)

        # Skip turn counter instructions
        SCREEN.blit(skipturn, (500, 320))
        SKIPTURN_TEXT = get_font(25).render("Skip Enemy Turn", True, "Black")
        SKIPTURN_RECT = SKIPTURN_TEXT.get_rect(center=(700, 370))
        SCREEN.blit(SKIPTURN_TEXT, SKIPTURN_RECT)

        # Take turn counter instructions
        SCREEN.blit(taketurn, (950, 320))
        TAKETURN_TEXT = get_font(25).render("Take Enemys turn", True, "Black")
        TAKETURN_RECT = TAKETURN_TEXT.get_rect(center=(1160, 370))
        SCREEN.blit(TAKETURN_TEXT, TAKETURN_RECT)

        # General powerup instructions
        DESC_TEXT = get_font(30).render(
            "Powerups can be collected by placing a counter on a slot that contains a powerup.", True, "Black")
        DESC_RECT = DESC_TEXT.get_rect(center=(640, 470))
        SCREEN.blit(DESC_TEXT, DESC_RECT)
        DESC2_TEXT = get_font(30).render(
            "And can be used by clicking your powerup counter slot on your side of the screen.", True, "Black")
        DESC2_RECT = DESC2_TEXT.get_rect(center=(640, 510))
        SCREEN.blit(DESC2_TEXT, DESC2_RECT)
        DESC3_TEXT = get_font(30).render(
            "These can be used at any point during your turn.", True, "Black")
        DESC3_RECT = DESC3_TEXT.get_rect(center=(640, 550))
        SCREEN.blit(DESC3_TEXT, DESC3_RECT)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    play()

        pygame.display.update()



def options():
    """Allows the user to change some settings, such as colourblindness."""
    new_resolution = (1280, 721)
    SCREEN = pygame.display.set_mode(new_resolution)
    while True:

        current_volume = round(pygame.mixer.music.get_volume(), 1)

        # Gets mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Main header text.
        OPTIONS_TEXT = get_font(45).render("Options", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Music volume text.
        MUSIC_TEXT = get_font(35).render("Music Volume", True, "Black")
        MUSIC_RECT = MUSIC_TEXT.get_rect(center=(340, 160))
        SCREEN.blit(MUSIC_TEXT, MUSIC_RECT)

        # Current volume text.
        VOL_TEXT = get_font(35).render(str(current_volume * 100), True, "Black")
        VOL_RECT = VOL_TEXT.get_rect(center=(340, 210))
        SCREEN.blit(VOL_TEXT, VOL_RECT)

        # Colourblind text.
        COLOR_TEXT = get_font(35).render("Colourblind mode", True, "Black")
        COLOR_RECT = MUSIC_TEXT.get_rect(center=(910, 160))
        SCREEN.blit(COLOR_TEXT, COLOR_RECT)

        # Button to return to main menu from options.
        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights options text while mouse hovers
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Volume adjust buttons
        VOL_UP = Button(image=None, pos=(460, 260),
                        text_input="+", font=get_font(75), base_color="Black", hovering_color="Green")

        VOL_DOWN = Button(image=None, pos=(220, 260),
                          text_input="-", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights options text while mouse hovers
        VOL_UP.changeColor(OPTIONS_MOUSE_POS)
        VOL_UP.update(SCREEN)
        VOL_DOWN.changeColor(OPTIONS_MOUSE_POS)
        VOL_DOWN.update(SCREEN)


        # Colourblind change buttons
        if gridGUI.counterColour1 == "../assets/CounterRed.png":
            selcol3 = "black"
            selcol2 = "black"
            selcol1 = "green"
        if gridGUI.counterColour1 == "../assets/CounterYellow.png":
            selcol3 = "black"
            selcol2 = "green"
            selcol1 = "black"
        if gridGUI.counterColour1 == "../assets/CounterGreen.png":
            selcol3 = "green"
            selcol2 = "black"
            selcol1 = "black"
        COLOR3 = Button(image=None, pos=(1090, 210),
                        text_input="Color 3", font=get_font(25), base_color=selcol3, hovering_color="Green")

        COLOR2 = Button(image=None, pos=(940, 210),
                        text_input="Color 2", font=get_font(25), base_color=selcol2, hovering_color="Green")

        COLOR1 = Button(image=None, pos=(790, 210),
                          text_input="Color 1", font=get_font(25), base_color=selcol1, hovering_color="Green")

        SCREEN.blit(red_display, (750, 250))
        SCREEN.blit(blue_display, (800, 250))
        SCREEN.blit(yellow_display, (900, 250))
        SCREEN.blit(purple_display, (950, 250))
        SCREEN.blit(green_display, (1050, 250))
        SCREEN.blit(pink_display, (1100, 250))

        # Highlights options text while mouse hovers
        COLOR1.changeColor(OPTIONS_MOUSE_POS)
        COLOR1.update(SCREEN)
        COLOR2.changeColor(OPTIONS_MOUSE_POS)
        COLOR2.update(SCREEN)
        COLOR3.changeColor(OPTIONS_MOUSE_POS)
        COLOR3.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Decreases volume if clicked
                if VOL_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    new_volume = round(current_volume - 0.1, 1)
                    if new_volume > 1:
                        new_volume = 1.0
                    elif new_volume < 0:
                        new_volume = 0.0
                    mixer.music.set_volume(new_volume)

                # Increases volume if clicked
                if VOL_UP.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    new_volume = round(current_volume + 0.1, 1)
                    if new_volume > 1:
                        new_volume = 1.0
                    elif new_volume < 0:
                        new_volume = 0.0
                    mixer.music.set_volume(new_volume)

                # Returns user to menu if clicked
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    main_menu()

                if COLOR1.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    gridGUI.images["redGhost"] = image("redGhost", pygame.image.load("../assets/CounterRed.png"), 1, 0, 0)
                    gridGUI.images["blueGhost"] = image("blueGhost", pygame.image.load("../assets/CounterBlue.png"), 1, 0, 0)
                    gridGUI.counterColour1 = "../assets/CounterRed.png"
                    gridGUI.counterColour2 = "../assets/CounterBlue.png"

                if COLOR2.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    gridGUI.images["redGhost"] = image("redGhost", pygame.image.load("../assets/CounterYellow.png"), 1, 0, 0)
                    gridGUI.images["blueGhost"] = image("blueGhost", pygame.image.load("../assets/CounterPurple.png"), 1, 0, 0)
                    gridGUI.counterColour1 = "../assets/CounterYellow.png"
                    gridGUI.counterColour2 = "../assets/CounterPurple.png"

                if COLOR3.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    gridGUI.images["redGhost"] = image("redGhost", pygame.image.load("../assets/CounterGreen.png"), 1, 0, 0)
                    gridGUI.images["blueGhost"] = image("blueGhost", pygame.image.load("../assets/CounterPink.png"), 1, 0, 0)
                    gridGUI.counterColour1 = "../assets/CounterGreen.png"
                    gridGUI.counterColour2 = "../assets/CounterPink.png"

        pygame.display.update()

main_menu()
