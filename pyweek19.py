import os, pygame, math, sys
import pygame._view
from pygame.locals import *

# directory variables
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

# screen constants
SCREEN_X = 112
SCREEN_Y = 128
TILE_SIZE = 16


# image constants

BACKGROUND_COLOR = (120, 170, 240)

# function to load image
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(pygame.compat.geterror()))
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# sprites


def main_loop():
    # initialize pygame and variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Connect Four')
    pygame.mouse.set_visible(0)

    # initialize board
    board = [[0,0,0,0,0,0], \
             [0,0,0,0,0,0], \
             [0,0,0,0,0,0], \
             [0,0,0,0,0,0], \
             [0,0,0,0,0,0], \
             [0,0,0,0,0,0], \
             [0,0,0,0,0,0]]

    # initialize variables and sprite lists
    pieces = []
    arrows = []
    turn = 1
    sel_col = 3

    arrows.append(RightArrowSprite(screen, sel_col + 1, 0))
    arrows.append(LeftArrowSprite(screen, sel_col - 1, 0))
    arrows.append(DownArrowSprite(screen, sel_col, 1))
    sel_piece = SelectedPieceSprite(screen, sel_col, 0, turn)
    board_bg = BoardSprite(screen)

    # game loop
    while True:

        # check event queue
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                

        # draw sprites on screen
        screen.fill(BACKGROUND_COLOR)


        # refresh screen
        pygame.display.flip()




def main():
    main_loop()

if __name__ == '__main__':
    main()
