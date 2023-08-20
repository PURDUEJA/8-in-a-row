import pygame, sys
from Button import Button

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
boards = []
resolutions = [(811, 811), (811, 811), (811, 811), (811, 811)]
board = int
boards.extend([BOARD8X7, BOARD9X8, BOARD10X9, BOARD11X10])


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
    b_res = board_size()
    board = pygame.transform.smoothscale(boards[b_res], (811, 711))
    res_change(b_res)
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(board, (0, 0))

        # Return to main menu.
        TEMP_BACK = Button(image=None, pos=(405, 761),
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

        pygame.display.update()

def board_size():
    """Menu for users to select board size."""
    while True:
        # Gets mouse position
        BOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Main header text.
        BOARD_TEXT = get_font(45).render("Select a board size.", True, "Black")
        BOARD_RECT = BOARD_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(BOARD_TEXT, BOARD_RECT)

        # Button to return to play from board.
        BOARD_BACK = Button(image=None, pos=(640, 560),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights options text while mouse hovers
        BOARD_BACK.changeColor(BOARD_MOUSE_POS)
        BOARD_BACK.update(SCREEN)

        # Button to return to main menu from options.
        eight_by_seven = Button(image=None, pos=(640, 160),
                              text_input="8x7", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights text while mouse hovers
        eight_by_seven.changeColor(BOARD_MOUSE_POS)
        eight_by_seven.update(SCREEN)

        # Button to return to main menu from options.
        nine_by_eight = Button(image=None, pos=(640, 260),
                                text_input="9x8", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights text while mouse hovers
        nine_by_eight.changeColor(BOARD_MOUSE_POS)
        nine_by_eight.update(SCREEN)

        # Button to return to main menu from options.
        ten_by_nine = Button(image=None, pos=(640, 360),
                               text_input="10x9", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights text while mouse hovers
        ten_by_nine.changeColor(BOARD_MOUSE_POS)
        ten_by_nine.update(SCREEN)

        eleven_by_ten = Button(image=None, pos=(640, 460),
                             text_input="11x10", font=get_font(75), base_color="Black", hovering_color="Green")

        # Highlights text while mouse hovers
        eleven_by_ten.changeColor(BOARD_MOUSE_POS)
        eleven_by_ten.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if eight_by_seven.checkForInput(BOARD_MOUSE_POS):
                    b_res = 0
                    return b_res

            if event.type == pygame.MOUSEBUTTONDOWN:
                if nine_by_eight.checkForInput(BOARD_MOUSE_POS):
                    b_res = 1
                    return b_res

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ten_by_nine.checkForInput(BOARD_MOUSE_POS):
                    b_res = 2
                    return b_res

            if event.type == pygame.MOUSEBUTTONDOWN:
                if eleven_by_ten.checkForInput(BOARD_MOUSE_POS):
                    b_res = 3
                    return b_res

        pygame.display.update()

def res_change(b_res):
    """Change resolution."""
    new_resolution = resolutions[b_res]
    SCREEN = pygame.display.set_mode(new_resolution, pygame.RESIZABLE)
    current_resolution = new_resolution


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