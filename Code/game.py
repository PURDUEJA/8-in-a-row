"""
Ultimate Connect.
Creators: Jacob Purdue and Nick Kho
Start date: Thursday 20th July
"""
import pygame
import sys

# Intializes pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("jacob stinks")

button_width = 200
button_height = 100
button_color = (0, 255, 0)  # Green color (RGB)
button_text_color = (255, 255, 255)  # White color (RGB)
button_text_size = 30
button_text = "Click Me!"

def draw_button(x, y):
    pygame.draw.rect(screen, button_color, (x, y, button_width, button_height))
    font = pygame.font.SysFont(None, button_text_size)
    text = font.render(button_text, True, button_text_color)
    text_rect = text.get_rect(center=(x + button_width / 2, y + button_height / 2))
    screen.blit(text, text_rect)

while True:
    break
    # ^ This stops the gui from being run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x < mouse_x < x + button_width and y < mouse_y < y + button_height:
                # Do something when the button is clicked
                print("Button clicked!")

    screen.fill((255, 255, 255))  # Fill the screen with white color
    x = (screen_width - button_width) // 2
    y = (screen_height - button_height) // 2
    draw_button(x, y)
    pygame.display.flip()

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
    if row > rows - checkNumber:
        return False

    # Check the next 4 in a row and return the result.
    return all(grid[row][col+i] == player for i in range(checkNumber))


def checkUnderneath(row, col, player, checkNumber):
    rows = len(grid)
    cols = len(grid[0])

    # Check if there are 4 spaces underneath the chosen spot.
    if col > cols - checkNumber:
        return False

    # Check the next 4 underneath and return the result.
    return all(grid[row + i][col] == player for i in range(checkNumber))


def checkInThatDirection(col, row, originalCol, originalRow):
    x_offset = originalCol - col
    y_offset = originalRow - row


def checkWinner(checkNumber):
    winnerFound = 0
    while winnerFound is 0:
        for row in grid:
            for col in grid:
                players = [1, 2]
                for player in players:
                    winnerFound = player if checkInRow(row, col, player, checkNumber) else 0
                    winnerFound = player if checkDiagonally(row, col, player, checkNumber) else 0
                    winnerFound = player if checkUnderneath(row, col, player, checkNumber) else 0
    return winnerFound

def place(row, collumn, player):
    """"""
    grid[row][collumn] = player


putCounter(0, 1)
putCounter(1, 1)
putCounter(2, 1)
checkSurroundings(11, 1, 1)
print(grid[11][0])
printGrid()