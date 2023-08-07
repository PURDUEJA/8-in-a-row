import pygame, sys
from Button import Button

pygame.init()

# Sets window settings resolution and title.
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ultimate Connect")

# Background image
BG = pygame.image.load("../assets/tempBG_1280x720.png")
BOARD = pygame.image.load("../assets/board.png")


def get_font(size):  # Returns font in the desired size

    return pygame.font.Font("../assets/DiloWorld-mLJLv.ttf", size)


def game():
    """Plays the game itself"""
    GAME_MOUSE_POS = pygame.mouse.get_pos()

    # Fills background white.
    SCREEN.fill("white")
    SCREEN.blit(BOARD, (0, 0))

    # Return to main menu.
    TEMP_BACK = Button(image=None, pos=(640, 460),
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
                    game()

        pygame.display.update()


def options():
    """Allows the user to change some settings."""
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


def main_menu():
    """Main menu for the game."""
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


main_menu()
