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
#Instantiate mixer
mixer.init()
click = pygame.mixer.Sound("../assets/Click.wav")
pygame.mixer.music.load("../assets/Approach 3.mp3")
pygame.mixer.music.play()
volume = 0.5
mixer.music.set_volume(volume)


BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


ROW_COUNT = 7
COLUMN_COUNT = 8

game_over = False
turn = 0

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(SCREEN, "gray", (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(SCREEN, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(SCREEN, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                pygame.draw.circle(SCREEN, BLACK, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), (RADIUS - 5))
                pygame.draw.circle(SCREEN, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), (RADIUS - 7))
            elif board[r][c] == 2:
                pygame.draw.circle(SCREEN, BLUE, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                pygame.draw.circle(SCREEN, BLACK, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), (RADIUS - 5))
                pygame.draw.circle(SCREEN, BLUE, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), (RADIUS - 7))
    pygame.display.update()


def get_font(size):  # Returns font in the desired size

    return pygame.font.Font("../assets/DiloWorld-mLJLv.ttf", size)

def main_menu():
    """Main menu for the game."""
    new_resolution = (1280, 720)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    # Load audio file


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
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                mixer.music.stop()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    options(volume)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def one_winner():
    """Winner screen."""
    new_resolution = (1280, 720)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    SCREEN.fill("red")
    while True:
        # Gets position of the mouse
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        WIN_TEXT = get_font(100).render("Red Won!", True, "#FFFFFF")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 100))

        # Return to main menu.
        WIN_BACK = Button(image=None, pos=(640, 660),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Black")

        WIN_BACK.changeColor(WIN_MOUSE_POS)
        WIN_BACK.update(SCREEN)

        SCREEN.blit(WIN_TEXT, WIN_RECT)

        # Return to main menu.
        WIN_AGAIN = Button(image=None, pos=(640, 330),
                           text_input="Play Again", font=get_font(75), base_color="White", hovering_color="Black")

        WIN_AGAIN.changeColor(WIN_MOUSE_POS)
        WIN_AGAIN.update(SCREEN)

        # Runs button when clicked.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    main_menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_AGAIN.checkForInput(WIN_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    game(board, turn, game_over)

        pygame.display.update()

def two_winner():
    """Winner screen."""
    new_resolution = (1280, 720)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    SCREEN.fill("blue")
    while True:
        # Gets position of the mouse
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        WIN_TEXT = get_font(100).render("Blue Won!", True, "#FFFFFF")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 100))

        # Return to main menu.
        WIN_BACK = Button(image=None, pos=(640, 660),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Black")

        WIN_BACK.changeColor(WIN_MOUSE_POS)
        WIN_BACK.update(SCREEN)

        # Return to main menu.
        WIN_AGAIN = Button(image=None, pos=(640, 330),
                          text_input="Play Again", font=get_font(75), base_color="White", hovering_color="Black")

        WIN_AGAIN.changeColor(WIN_MOUSE_POS)
        WIN_AGAIN.update(SCREEN)

        SCREEN.blit(WIN_TEXT, WIN_RECT)

        # Runs button when clicked.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    main_menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_AGAIN.checkForInput(WIN_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    game(board, turn, game_over)

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
                    game(board, turn, game_over)

        pygame.display.update()

turn = 0

def game(board, turn, game_over):
    """Plays the game itself"""
    new_resolution = (800, 800)
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    current_resolution = new_resolution
    board = create_board()
    print_board(board)

    while not game_over:
        draw_board(board)
        GAME_MOUSE_POS = pygame.mouse.get_pos()

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
                pygame.draw.rect(SCREEN, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(SCREEN, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    pygame.draw.circle(SCREEN, BLACK, (posx, int(SQUARESIZE / 2)), RADIUS - 5)
                    pygame.draw.circle(SCREEN, RED, (posx, int(SQUARESIZE / 2)), RADIUS - 7)
                else:
                    pygame.draw.circle(SCREEN, BLUE, (posx, int(SQUARESIZE / 2)), RADIUS)
                    pygame.draw.circle(SCREEN, BLACK, (posx, int(SQUARESIZE / 2)), RADIUS - 5)
                    pygame.draw.circle(SCREEN, BLUE, (posx, int(SQUARESIZE / 2)), RADIUS - 7)


            if event.type == pygame.MOUSEBUTTONDOWN:

                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            game_over = True
                            one_winner()

                # # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            game_over = True
                            two_winner()

                turn += 1
                turn = turn % 2

                if game_over:
                    pass

        pygame.display.update()

def options(volume):
    """Allows the user to change some settings, such as colourblindness."""
    while True:
        # Gets mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Main header text.
        OPTIONS_TEXT = get_font(45).render("Options.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Master volume text.
        OPTIONS_TEXT = get_font(35).render("Music Volume.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Current volume text.
        OPTIONS_TEXT = get_font(35).render(str(volume * 100), True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 310))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)


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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    main_menu()
            # Button click for decreasing volume.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOL_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    volume = round(volume - 0.1, 1)
                    new_volume = volume
                    if volume > 1:
                        volume = 1.0
                        new_volume = 1.0
                    elif volume < 0:
                        volume = 0.0
                        new_volume = 0.0
                    mixer.music.set_volume(new_volume)
                    print(new_volume)

            # Button click for increasing volume.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOL_UP.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../assets/Click.wav"))
                    volume = round(volume + 0.1, 1)
                    new_volume = volume
                    if volume > 1:
                        new_volume = 1.0
                        volume = 1.0
                    elif volume < 0:
                        new_volume = 0.0
                        volume = 0.0
                    mixer.music.set_volume(new_volume)
                    print(new_volume)

        pygame.display.update()
main_menu()