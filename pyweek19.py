import os, pygame, math, sys
import pygame._view
from pygame.locals import *
from levels import levels
from audio import *

# directory variables
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

# screen constants
SCREEN_X = 352
SCREEN_Y = 352
TILE_SIZE = 32

level_count = 0
level = []
switch_active = False

# image constants
WALL_IMG = 'block.gif'
TRAP_IMG = 'spikes.gif'
PLAYER_IMG = 'player.gif'
SWITCH_IMG = 'switch.gif'
GOAL_IMG = 'goal_animation.gif'
PLAYER_IMG = 'player.gif'
GHOST_IMG = 'ghost.gif'
TITLE_IMG = 'title.gif'


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
class TileSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.image, self.rect = load_image(image)

    def update(self):
        self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)
        self.screen.blit(self.image, self.rect)

class WallSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, WALL_IMG)

class TrapSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, TRAP_IMG)

class SwitchSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, SWITCH_IMG)

class GoalSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, GOAL_IMG)

class GhostSprite(TileSprite):
    def __init__(self, screen, x, y):
        TileSprite.__init__(self, screen, x, y, GHOST_IMG)

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.image, self.rect = load_image(PLAYER_IMG)

    def update(self):
        self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

def check_collision(x, y):
    if level[y][x] == 1:
        hit_wall()
        return True
    if level[y][x] == 2:
        hit_wall()
        return True
    return False

def check_death(x, y):
    if level[y][x] == 3:
        step_spike()
        return True
    if level[y][x] == 7:
        step_spike()
        return True
    return False

def check_switch(x, y):
    global switch_active
    if level[y][x] == 4:
        if not switch_active:
            hit_switch()
            switch_active = True
        return True
    switch_active = False
    return False

def check_goal(x, y):
    if level[y][x] == 5:
        return True
    return False

def next_level():
    global level_count
    level_count += 1
    if level_count >= len(levels):
        sys.exit()
    level_end()
    main_loop()

def restart():
    main_loop()

background = pygame.image.load(TITLE_IMG)
backgroundRect = background.get_rect()



def main_loop():
    # initialize pygame and variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Pyweek19')
    pygame.mouse.set_visible(0)
    global level_count, level

    # initialize level
    level = levels[level_count]

    # initialize variables and sprite lists
    walls = []
    maze_walls = []
    traps = []
    ghosts = [] 

    y = 0
    for row in level:
        x = 0
        for col in row:
            if (col == 1):
                walls.append(WallSprite(screen, x, y))
            if (col == 2):
                maze_walls.append(WallSprite(screen, x, y))
            if (col == 3):
                traps.append(TrapSprite(screen, x, y))
            if (col == 4):
                switch = SwitchSprite(screen, x, y)
            if (col == 5):
                goal = GoalSprite(screen, x, y)
            if (col == 6):
                player = PlayerSprite(screen, x, y)
            if (col == 7):
                traps.append(TrapSprite(screen, x, y))
                ghosts.append(GhostSprite(screen, x, y))
            x += 1
        y += 1

    # game loop
    while True:

        if check_goal(player.x, player.y):
            next_level()

        if check_death(player.x, player.y):
            level[player.y][player.x] = 7
            restart()

        # check event queue
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_LEFT:
                    if not check_collision(player.x - 1, player.y):
                        player.move_left()
                elif event.key == K_RIGHT:
                    if not check_collision(player.x + 1, player.y):
                        player.move_right()
                elif event.key == K_UP:
                    if not check_collision(player.x, player.y - 1):
                        player.move_up()
                elif event.key == K_DOWN:
                    if not check_collision(player.x, player.y + 1):
                        player.move_down()
                

        # draw sprites on screen
        #screen.fill(BACKGROUND_COLOR)

        if level_count == 0:
            screen.blit(background,backgroundRect)
        else:
            screen.fill(BACKGROUND_COLOR)

        for wall in walls:
            wall.update()
        for ghost in ghosts:
            ghost.update()
        if check_switch(player.x, player.y):
            for maze_wall in maze_walls:
                maze_wall.update()
            for trap in traps:
                trap.update()
        switch.update()
        goal.update()
        player.update()

        # refresh screen
        pygame.display.flip()




def main():
    main_loop()

if __name__ == '__main__':
    main()
