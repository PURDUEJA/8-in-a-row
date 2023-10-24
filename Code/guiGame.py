import asyncio
import math
import random
import multiprocessing
import time
from threading import Thread

import pygame

print("asjhdfkjahsdfgjakhsdfkjhgasdffdsa")


class GUIclass:
    def __init__(self, x, y):
        self.images = {}
        self.text = {}
        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        self.mouseX = 0
        self.x = x
        self.y = y
        self.images["redGhost"] = image(
            "redGhost", pygame.image.load("CounterRed.png"), 1, 0, 0
        )
        self.images["blueGhost"] = image(
            "blueGhost", pygame.image.load("CounterBlue.png"), 1, 0, 0
        )
        self.grid = []
        self.playerTurn = 1
        pygame.mixer.init()
        self.powerups = {10: "GetCounter",
                         11: "SkipTurn",
                         12: "TakeTurn"}
        self.powerupGrid = [[0, 0],
                            [0, 0],
                            [0, 0]]
        self.powerupImages = {}

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
                            self.images[f"{collumn}, {row}"] = image("redCounter", pygame.image.load("counterRed.png"), 2, collumn, row)
                            #print(collumn)
                            #print(row)
                        case 2:
                            #print("22222")
                            self.images[f"{collumn}, {row}"] = image("yellowCounter", pygame.image.load("counterBlue.png"), 2, collumn, row )
                        case 10:
                            powerup = self.powerups[10]
                            scaled_image = pygame.image.load(f"{powerup}.png")
                            scaled_image.set_alpha(128)
                            #scaled_image = pygame.transform.scale(pygame.image.load(f"{powerup}.png"), (30, 30))
                            self.images[f"{collumn}, {row}"] = image(powerup, scaled_image, 2, collumn, row )
                        case 11:
                            powerup = self.powerups[11]
                            scaled_image = pygame.image.load(f"{powerup}.png")
                            scaled_image.set_alpha(128)
                            #scaled_image = pygame.transform.scale(pygame.image.load(f"{powerup}.png"), (30, 30))
                            self.images[f"{collumn}, {row}"] = image(powerup, scaled_image, 2, collumn, row )
                        case 12:
                            powerup = self.powerups[12]
                            scaled_image = pygame.image.load(f"{powerup}.png")
                            scaled_image.set_alpha(128)
                            #scaled_image = pygame.transform.scale(pygame.image.load(f"{powerup}.png"), (30, 30))
                            self.images[f"{collumn}, {row}"] = image(powerup, scaled_image, 2, collumn, row )
        self.update()

    def animateCounter(self, player, column):
        print("AJKSDHJKLADHJKLAHJKLSDAHJKLDAHJKLSDJKLH")
        x = (column + 1) * (1011/10) + (9 - (self.getPercentage(self.x, (column * (1011/10)), 10)))

        underneath = False
        row = 0
        while underneath == False:
            if self.isUnderBlocked(row, column):
                underneath = True
            else:
                row += 1
        ending_y = (row * (711 / 6.96) + (10 - ((self.getPercentage(self.y, (row * (711 / 7)), 7)) * 3.47)))
        current_y = 11

        # soft hard coding AHAHAHAHAHAHAHAHAHAHAHAHA forehead
        match player:
            case 1:
                bruh = "counterRed.png"
            case 2:
                bruh = "counterBlue.png"
        layer = 2
        self.images["fallingImage"] = image("fallingCounter", pygame.image.load(bruh), layer, x, current_y)

        listofsortedimages = sorted(self.images.values(), key = lambda x:x.layer)
        dontRenderThese = ["redGhost", "blueGhost", "board", "fallingCounter", "redCounter", "yellowCounter"]
        deletedObjs = 0
        for objectNum in range(len(listofsortedimages)):
            print(objectNum)
            # print(listofsortedimages[objectNum].Name)
            if listofsortedimages[objectNum - deletedObjs].Name in dontRenderThese:
                listofsortedimages.pop(objectNum - deletedObjs)
                deletedObjs += 1
        accel_factor = 1.012

        column_image = pygame.image.load("Column.png")
        column_x = x
        while ending_y > current_y:

            # Simulate gravity
            current_y *= accel_factor
            if current_y < ending_y / 3:
                accel_factor = 1.012
            elif current_y < ending_y / 2:
                accel_factor = 1.012
            else:
                accel_factor = 1.012

            self.images["fallingImage"] = image("fallingCounter", pygame.image.load(bruh), layer, x, current_y)



            fill_color = (255, 255, 255)
            fill_rect = pygame.Rect(x, current_y - 10, 91, 101)
            pygame.draw.rect(self.screen, fill_color, fill_rect)
            for object in listofsortedimages:
                #    if object.Name != "redGhost" or object.Name != "blueGhost":
                # self.screen.blit(object.File, (object.x, object.y))
                print(object.Name)
                print(object.x)
                print(object.y)

                print((object.x + 1) * (1011/10) + (9 - (self.getPercentage(self.x, (object.x * (1011/10)), 10))))
                print(object.y * (711/6.96) + (10 - ((self.getPercentage(self.y, (object.y * (711/7)), 7)) * 3.47)))

                # self.screen.blit(object.File, (object.x + 1) * (1011/10) + (9 - (self.getPercentage(self.x, (object.x * (1011/10)), 10))),
                #                object.y * (711/6.96) + (10 - ((self.getPercentage(self.y, (object.y * (711/7)), 7)) * 3.47)))

            self.screen.blit(self.images["fallingImage"].File, (x, current_y))


            # self.screen.blit(self.images["board"].File, (self.images["board"].x, self.images["board"].y))
            column_offset = 5
            self.screen.blit(column_image, (x - column_offset, 0))
            # self.update()
            print(f"Updated {current_y}")


            # test

            # Stops only the final frame from rendering
            if ending_y > current_y:
                pygame.display.update()

        self.images.pop("fallingImage")


    def updateTexts(self):
        for textKey in self.text.keys():
            self.screen.blit(
                self.text[textKey].File,
                (
                    self.text[textKey].x,
                    self.text[textKey].y
                )
            )

    def update(self):
        self.screen.fill((255, 255, 255))
        # Assume there are 5 layers.

        # Create a list of keys and sort it based on the layer.
        # Then iterate through this list and access the dictionary of images based on this.
        # This would improve efficiency by more than 18x but cbf lol

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
                            (self.getPercentage(self.x, self.mouseX, 10) * (1011/10) + (9 - (self.getPercentage(self.x, self.mouseX, 10))), 10),
                        )
                        #print("asdfa")
                    elif self.images[imageKey] is self.images["blueGhost"]:
                        self.screen.blit(
                            self.images["blueGhost"].File,
                            (self.getPercentage(self.x, self.mouseX, 10) * (1011/10) + (
                                        9 - (self.getPercentage(self.x, self.mouseX, 10))), 10),
                        )
                    elif self.images[imageKey].Name != "board":
                        self.screen.blit(
                            self.images[imageKey].File,
                            (
                                (self.images[imageKey].x + 1) * (1011/10) + (9 - (self.getPercentage(self.x, (self.images[imageKey].x * (1011/10)), 10))),
                                self.images[imageKey].y * (711/6.96) + (10 - ((self.getPercentage(self.y, (self.images[imageKey].y * (711/7)), 7)) * 3.47))
                            ),
                        )
                        #print("1")

                    else:
                        self.screen.blit(self.images[imageKey].File, (0, 0))
                        #print("3")
        self.updatePowerupVisual()
        self.loadPowerupSides()
        self.updateTexts()
        pygame.display.update()  # Updates the display window

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"



    def getPercentage(self, max, number2, percentiles):
        # 700, 50, 7
        # 711, 550, 7
        result = self.x / percentiles  # 700 / 7 = 100 # 711/7 = 101.5
        result = number2 / result  # 50 / 100 = 0.5 # 550 / 101.5 = 5.3
        result = math.floor(result)  # 0 # = 5
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
        # print(self.grid)
        if self.grid[0][collumn] != 0:
            return "failed"

        else:
            underneath = False

            row = 0
            # print(row, collumn)

            while underneath is False:
                if self.isUnderBlocked(row, collumn):
                    print("lmao")
                    powerup = self.place(row, collumn, player)
                    # print("567856785678")
                    print(self.powerupGrid)
                    print(self.playerTurn)
                    if self.powerupGrid[2][self.playerTurn - 1] != 0:
                        pass
                    elif powerup != 0:
                        self.storePowerup(powerup)
                        # print("6789678967896789")
                    # print("placed")
                    underneath = True
                else:
                    row += 1

    def isUnderBlocked(self, row, collumn):
        """"""
        try:
            values = [0, 10, 11, 12]
            if self.grid[row + 1][collumn] not in values:
                test = True
            else:
                test = False
        except IndexError:
            # print("indexerror")
            return True
        if test is True:
            return True

        else:
            return False

    def place(self, row, collumn, player):
        """"""
        powerup = self.grid[row][collumn]
        self.grid[row][collumn] = player
        return powerup

    def spawnPowerups(self):

        for i in range(random.randint(4, 7)):
            test = random.randint(1, 6)
            # print(test)
            self.grid[test][random.randint(0, 7)] = random.randint(10, 12)

    def storePowerup(self, powerup):
        i = 0
        while self.powerupGrid[i][self.playerTurn - 1] != 0:
            i += 1
        self.powerupGrid[i][self.playerTurn - 1] = powerup

    def updatePowerupVisual(self):
        for x in range(2):
            for y in range(3):
                if self.powerupGrid[y][x] != 0:
                    self.powerupImages[f"{x}, {y}"] = image(f"{x}, {y}", pygame.image.load(f"{self.powerups[self.powerupGrid[y][x]]}.png"), 1, x, y)
                else:
                    try:
                        del self.powerupImages[f"{x}, {y}"]
                    except KeyError:
                        pass

    def loadPowerupSides(self):
        #print(self.powerupImages)
        for imageKey in self.powerupImages.keys():
            # print(self.powerupImages[imageKey].x, self.powerupImages[imageKey].y)
            # print("asjkhdfaskdhjfhasjkdfsa")
            # print(imageKey)
            x = self.powerupImages[imageKey].x
            x *= 910
            x += 5
            y = self.powerupImages[imageKey].y
            y *= 711/7.07
            y += 109.7

            self.screen.blit(self.powerupImages[imageKey].File, (x, y))

    def usePower(self, power, player):
        print("182397491234y132412")
        match power:
            case "SkipTurn":
                if self.playerTurn is not player:
                    match self.playerTurn:
                        case 1:
                            self.playerTurn = 2
                        case 2:
                            self.playerTurn = 1
                else:
                    pass
            case "GetCounter":
                if self.playerTurn is not player:
                    match self.playerTurn:
                        case 1:
                            self.playerTurn = 2
                        case 2:
                            self.playerTurn = 1
                else:
                    pass
            case "TakeTurn":
                font = pygame.font.Font(None, 40)
                color = (0, 0, 0)
                match self.playerTurn:
                    case 1:
                        str = "2"
                        color = (0, 0, 255)
                    case 2:
                        str = "1"
                        color = (255, 0, 0)
                text = font.render(f"Take Turn Powerup: Let Player {str} this counter", True, color)
                self.text["test"] = image("test", text, 0, 5, 3)
    async def start(self):
        print("started")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # print(self.powerupGrid)
                    if event.button == 1: #Left click
                        x, y = pygame.mouse.get_pos()

                        x_coord = self.getPercentage(self.x, x, 10)
                        y_coord = self.y / 7
                        y_coord = y / y_coord
                        y_coord = math.floor(y_coord)
                        #print(x_coord, y_coord)
                        #print(f"Mouse clicked at position ({x_coord}, {y_coord})")
                        # print("asdfasdfasdfasfs")
                        if x <= (1011/10) or x >= (1011 - (1011/10)):

                            print(f"y: {y_coord}")
                            other_x = x_coord
                            if x_coord == 9:
                                other_x = 1
                            print(f"x: {other_x}")
                            try:
                                power = self.powerups[self.powerupGrid[y_coord - 1][other_x]]
                                self.usePower(power, other_x + 1)
                                self.powerupGrid[y_coord - 1][other_x] = 0
                                sound = pygame.mixer.Sound("assets_Click.wav")
                                sound.play()
                            except KeyError:
                                pass
                            except IndexError:
                                pass
                            self.updateToGrid(self.grid)
                        else:
                            self.text.clear()
                            # print("123412341234")
                            numbers = [0, 10, 11, 12]
                            if self.grid[0][x_coord - 1] in numbers:
                                # print("2345234523452345")

                                # task = asyncio.create_task(self.animateCounter(self.playerTurn, x_coord - 1))
                                # asyncio.run(task)
                                # await self.animateCounter(self.playerTurn, x_coord - 1)
                                # await self.animateCounter(self.playerTurn, x_coord - 1)
                                # help
                                # p1 = multiprocessing.Process(target = self.animateCounter, args = [self.playerTurn, x_coord - 1])
                                # p1.start()
                                Thread(target = self.animateCounter(self.playerTurn, x_coord - 1)).start()
                                self.putCounter((x_coord - 1), self.playerTurn)
                                # print("456745674567")
                                print(f"Placed Counter {self.playerTurn} at ({x_coord},{x_coord})")
                                sound = pygame.mixer.Sound("assets_Click.wav")
                                sound.play()
                                if self.checkWinner(4):
                                    self.gg()
                                    running = False
                                print("hello")
                                # await task


                            else:
                                # print("3456345634563456")
                                print("Can't place here")
                            self.updateToGrid(self.grid)
                            if running:
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
        return self.playerTurn

    def coordsToPos(self, x, y):
        return [(x * 101), (y * 101)]

    def gg(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Winner is {self.playerTurn}", True, (255, 255, 255))
        self.screen.blit(text, (1011/2, 711/2))
        print(f"Winner is {self.playerTurn}")
        pygame.display.update()
        return self.playerTurn

    def test(self):
        pygame.display.update()


class image:
    def __init__(self, name, file, layer, x, y):
        self.File = file
        self.Name = name
        self.layer = layer
        self.x = x
        self.y = y
