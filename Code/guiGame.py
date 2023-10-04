import pygame
import math
import asyncio

print("asjhdfkjahsdfgjakhsdfkjhgasdffdsa")


class GUIclass:
    def __init__(self, x, y):
        self.counterColour1 = "../assets/CounterRed.png"
        self.counterColour2 = "../assets/CounterBlue.png"
        self.images = {}
        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        self.mouseX = 0
        self.x = x
        self.y = y
        self.images["redGhost"] = image(
            "redGhost", pygame.image.load("../assets/CounterRed.png"), 1, 0, 0
        )
        self.images["blueGhost"] = image(
            "blueGhost", pygame.image.load("../assets/CounterBlue.png"), 1, 0, 0
        )
        self.grid = []
        self.playerTurn = 1
        pygame.mixer.init()

    def checkInRow(self, row, col, player, checkNumber):
        rows = len(self.grid)
        cols = len(self.grid[0])
        # Check if there are 4 rows to the right of the chosen.
        if col > cols - checkNumber:
            return False

        return all(self.grid[row][col + i] == player for i in range(checkNumber))

    def checkDiagonally(self, row, col, player, checkNumber):
        rows = len(self.grid)
        cols = len(self.grid[0])

        # Check if there are 4 spaces diagonally bottom-right.
        if row > rows - checkNumber or col > cols - checkNumber:
            return False

        # Check the four diagonal squares in the bottom-right direction
        # and return the result.

        return all(self.grid[row + i][col + i] == player for i in range(checkNumber))

    def checkUnderneath(self, row, col, player, checkNumber):
        rows = len(self.grid)
        cols = len(self.grid[0])
        if row > rows - checkNumber:
            return False
        return all(self.grid[row + i][col] == player for i in range(checkNumber))

    def checkDiagonallyOpposite(self, row, col, player, checkNumber):
        rows = len(self.grid)
        cols = len(self.grid[0])

        if row > rows - checkNumber or col < 4:
            return False

        return all(self.grid[row + i][col - i] == player for i in range(checkNumber))

    def checkWinner(self, checkNumber):
        winnerFound = 0
        totaltimes = 0
        winnerFoundBool = False
        while winnerFoundBool == False:
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    totaltimes += 1
                    players = [1, 2]
                    for player in players:
                        if self.grid[row][col] is player:
                            # Check diagonally, horizontally, and vertically.
                            if player if self.checkInRow(row, col, player, checkNumber) else 0:
                                return player

                            # winnerFoundBool = True if (winnerFound != 0) else 0

                            if (
                                    player
                                    if self.checkDiagonally(row, col, player, checkNumber)
                                    else 0
                            ):
                                return player

                            # winnerFoundBool = True if (winnerFound != 0) else 0
                            if (
                                    player
                                    if self.checkUnderneath(row, col, player, checkNumber)
                                    else 0
                            ):
                                return player

                            if (
                                    player
                                    if self.checkDiagonallyOpposite(row, col, player, checkNumber)
                                    else 0
                            ):
                                return player
                            # winnerFoundBool = True if (winnerFound != 0) else 0
            return winnerFound
        return winnerFound
    def updateToGrid(self, grid):
        self.grid = grid
        for row in range(len(self.grid)):
            for collumn in range(len(self.grid[0])):
                #print(row, collumn)
                #print(row, collumn, self.grid[row][collumn])
                if self.grid[row][collumn] != 0:

                    match self.grid[row][collumn]:
                        case 1:
                            #print("1111")
                            self.images[f"{collumn}, {row}"] = image("redCounter", pygame.image.load(self.counterColour1), 2, collumn, row)
                            #print(collumn)
                            #print(row)
                        case 2:
                            #print("22222")
                            self.images[f"{collumn}, {row}"] = image("yellowCounter", pygame.image.load(self.counterColour2), 2, collumn, row )
        self.update()

    def update(self):
        self.screen.fill((255, 255, 255))
        # Assume there are 5 layers.
        for i in range(5):
            for imageKey in self.images.keys():
                if self.images[imageKey].layer == i:
                    if self.images[imageKey] is self.images["redGhost"]:
                        #print(self.mouseX)
                        #print(self.x)
                        #print(self.getPercentage(self.x, self.mouseX, 8))
                        #print(self.getPercentage(self.x, self.mouseX, 8))
                        self.screen.blit(
                            self.images["redGhost"].File,
                            (self.getPercentage(self.x, self.mouseX, 8) * 101.375 + (9 - (self.getPercentage(self.x, self.mouseX, 8))), 10),
                        )
                        #print("asdfa")
                    elif self.images[imageKey] is self.images["blueGhost"]:
                        self.screen.blit(
                            self.images["blueGhost"].File,
                            (self.getPercentage(self.x, self.mouseX, 8) * 101.375 + (
                                        9 - (self.getPercentage(self.x, self.mouseX, 8))), 10),
                        )
                    elif self.images[imageKey].Name is not "board":
                        self.screen.blit(
                            self.images[imageKey].File,
                            (
                                self.images[imageKey].x * 101.375 + (9 - (self.getPercentage(self.x, (self.images[imageKey].x * 101.375), 8))),
                                self.images[imageKey].y * 101.571 + (10 - ((self.getPercentage(self.y, (self.images[imageKey].y * 101.571), 7)) * 3.47))
                            ),
                        )
                        #print("1")

                    else:
                        self.screen.blit(self.images[imageKey].File, (0, 0))
                        #print("3")
        pygame.display.update()  # Updates the display window

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"



    def getPercentage(self, max, number2, percentiles):
        # 700, 50, 7
        result = max / percentiles  # 700 / 7 = 100
        result = number2 / result  # 50 / 100 = 0.5
        result = math.floor(result)  # 0
        return result
    """

    def updateToGrid(self, grid):
        for y in grid:
            for x in y:
                match grid[y][x]:
                    case 1:
                        self.images["counter"] = image(
                            "counter", pygame.image.load("CounterRed.png"), x, y
                        )
                    case 2:
                        self.images["counter"] = image(
                            "counter", pygame.image.load("CounterBlue.png"), x, y
                        )
    """

    def putCounter(self, collumn, player):
        """"""
        if self.grid[0][collumn] != 0:
            return "failed"

        else:
            underneath = False

            row = 0
            # print(row, collumn)

            while underneath is False:
                if self.isUnderBlocked(row, collumn):
                    self.place(row, collumn, player)
                    # print("placed")
                    underneath = True
                else:
                    row += 1

    def isUnderBlocked(self, row, collumn):
        """"""
        try:
            test = self.grid[row + 1][collumn] != 0
        except IndexError:
            # print("indexerror")
            return True
        if test is True:
            return True

        else:
            return False

    def place(self, row, collumn, player):
        """"""
        self.grid[row][collumn] = player

    async def start(self):
        print("started")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #Left click
                        x, y = pygame.mouse.get_pos()

                        x_coord = self.getPercentage(self.x, x, 8)
                        y_coord = self.getPercentage(self.y, y, 7)
                        #print(x_coord, y_coord)
                        #print(f"Mouse clicked at position ({x_coord}, {y_coord})")
                        if (
                            self.grid[0][x_coord] == 0
                        ):
                            self.putCounter(x_coord, self.playerTurn)
                            print(f"Placed Counter {self.playerTurn} at ({x_coord},{y_coord})")
                            sound = pygame.mixer.Sound("../assets/Click.wav")
                            sound.play()
                            if self.checkWinner(4):
                                self.gg()
                                running = False
                        else:
                            print("Can't place here")
                        self.updateToGrid(self.grid)
                        match self.playerTurn:
                            case 1:
                                self.playerTurn = 2
                            case 2:
                                self.playerTurn = 1


            self.update()
            x, y = pygame.mouse.get_pos()
            #print(f"Mouse clicked at position ({x}, {y})")
            self.mouseX = x

            match self.playerTurn:
                case 1:
                    self.images["redGhost"].File.set_alpha(128)
                    self.images["blueGhost"].File.set_alpha(0)
                case 2:
                    self.images["redGhost"].File.set_alpha(0)
                    self.images["blueGhost"].File.set_alpha(128)

    def coordsToPos(self, x, y):
        return [(x * 101), (y * 101)]

    def gg(self):
        print(f"Winner is {self.playerTurn}")


class image:
    def __init__(self, name, file, layer, x, y):
        self.File = file
        self.Name = name
        self.layer = layer
        self.x = x
        self.y = y
