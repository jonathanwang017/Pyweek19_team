import os, pygame, math, sys
import pygame._view
from pygame.locals import *

# directory variables
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

# screen constants
SCREEN_X = 352
SCREEN_Y = 352
TILE_SIZE = 32


# image constants
WALL_IMG = 'block.gif'


BACKGROUND_COLOR = (222, 222, 222)

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
class WallSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.image, self.rect = load_image(WALL_IMG)

    def update(self):
        self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)
        self.screen.blit(self.image, self.rect)


def main_loop():
    # initialize pygame and variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Pyweek19')
    pygame.mouse.set_visible(0)

    # initialize board
    board = [[0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0]]

    # initialize variables and sprite lists
    wall = WallSprite(screen, 0, 0)
    wall2 = WallSprite(screen, 1, 0)
    wall3 = WallSprite(screen, 0, 1)

    # game loop
    while True:

        # check event queue
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                

        # draw sprites on screen
        screen.fill(BACKGROUND_COLOR)

        wall.update()
        wall2.update()
        wall3.update()

        # refresh screen
        pygame.display.flip()




def main():
    main_loop()

if __name__ == '__main__':
    main()
