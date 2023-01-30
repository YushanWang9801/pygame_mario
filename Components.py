import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

from random import randint, choice 

# Parameters
WIDTH, HEIGHT = 800, 400
OBS_SIZE, FONT_SIZE = 40, 40  # for obstacles and font size
PLAYER_SIZE  = 50
COIN_SIZE = 30

SKY_LEVEL    = 150
GROUND_LEVEL = 333
FONT_POS_X   = 700
INIT_GRAVITY = -20
PLAYER_GROUND_LEVEL = (GROUND_LEVEL+ 3/4*PLAYER_SIZE)


# Classes
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 1:
            self.surface = pygame.image.load('images/obstacle1.png')
            self.y_pos   = SKY_LEVEL
        elif type == 2:
            self.surface = pygame.image.load('images/obstacle2.png')
            self.y_pos   = GROUND_LEVEL
        else:
            self.surface = pygame.image.load('images/obstacle3.png')
            self.y_pos   = GROUND_LEVEL

        self.image = pygame.transform.scale(self.surface,(OBS_SIZE, OBS_SIZE))
        self.rect    = self.image.get_rect(
                            bottomright=(randint(900,1100), self.y_pos))
        self.speed = 5
        self.facing_right = False

    def flipping(self):
        if self.rect.left <= self.left_boundary: 
            self.rect.right += OBS_SIZE
            self.facing_right = True
            self.surface = pygame.transform.flip(self.surface, True, False)
        elif self.rect.right >= self.right_boundary: 
            self.rect.left -= OBS_SIZE
            self.facing_right = False
            self.surface = pygame.transform.flip(self.surface, True, False)

    def update(self):
        self.rect.left -= self.speed
        if self.rect.x <= -100: self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img_1_path  = 'images/Capture1.png'
        img_2_path  = 'images/Capture3.png'
        img_3_path  = 'images/Capture4.png'

        self.player_img_list = [img_1_path, img_2_path, img_3_path]
        self.player_index = 0
        player_surface = pygame.image.load(self.player_img_list[self.player_index])

        self.image = pygame.transform.scale(player_surface,(PLAYER_SIZE,PLAYER_SIZE))
        self.rect = self.image.get_rect(midbottom=(100,GROUND_LEVEL))

        self.jump_sound = pygame.mixer.Sound('images/jump.mp3')
        self.jump_sound.set_volume(0.5)
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_LEVEL:
            self.gravity = INIT_GRAVITY
            self.jump_sound.play()
        
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y  += self.gravity
        if self.rect.bottom >= GROUND_LEVEL:
            self.rect.bottom = GROUND_LEVEL
        
    def player_animation(self):
        self.player_index += 0.1
        if self.player_index >= len(self.player_img_list):
            self.player_index = 0

        player_surface = pygame.image.load(self.player_img_list[int(self.player_index)])
        self.image = pygame.transform.scale(player_surface,(PLAYER_SIZE,PLAYER_SIZE))

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()

class Coin(pygame.sprite.Sprite):
    def __init__(self, type, coin_num):
        super().__init__()
        self.surface = pygame.image.load('images/coin.png')
        if type == 1: self.y_pos   = SKY_LEVEL
        else:         self.y_pos   = GROUND_LEVEL
        self.image = pygame.transform.scale(self.surface,(COIN_SIZE, COIN_SIZE))
        self.rect = coin_surface.get_rect(bottomright= \
                    (1000+ COIN_SIZE*coin_num, self.y_pos))
        self.speed = 5

    def update(self):
        self.rect.left -= self.speed
        if self.rect.x <= -100: self.kill()

# Background
background_img_path = 'images/backg.jpg'
background_surface  = pygame.image.load(background_img_path)
background_surface  = pygame.transform.scale(background_surface,
                                                (WIDTH, HEIGHT))

# obstacles  
obstacle_group = pygame.sprite.Group()

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Coins 
coins_group = pygame.sprite.Group()

# Texts
font_path = 'fonts/Pixeltype.ttf'
test_font = pygame.font.Font(font_path, FONT_SIZE)

text_score_surface = test_font.render("Scores: ", False, "Green")
text_score_rect    = text_score_surface.get_rect(center= (FONT_POS_X, FONT_SIZE))

text_life_surface = test_font.render("Life: ", False, "Green")
text_life_rect = text_score_surface.get_rect(center= (FONT_POS_X, FONT_SIZE*2))

# Coins
coin_path = 'images/coin.png'
coin_surface = pygame.image.load(coin_path)
coin_surface = pygame.transform.scale(coin_surface, (COIN_SIZE, COIN_SIZE))
coin_rect    = coin_surface.get_rect(center=(200, SKY_LEVEL))


# Game Over State Components
game_over_path = 'images/gameOver.png'
game_over_surface = pygame.image.load(game_over_path)
game_over_surface = pygame.transform.scale(game_over_surface, (400, 50))
game_over_rect = game_over_surface.get_rect(center=(400, 100))

player_dead_path = 'images/mariodead.png'
player_dead_surface = pygame.image.load(player_dead_path)
player_dead_surface = pygame.transform.scale(player_dead_surface, 
                                                    (PLAYER_SIZE, PLAYER_SIZE))
player_dead_rect    = player_dead_surface.get_rect(midbottom=(100, GROUND_LEVEL))


restart_path = 'images/restart.png'
restart_surface = pygame.image.load(restart_path)
restart_surface = pygame.transform.scale(restart_surface, (80, 80))
restart_rect = restart_surface.get_rect(center=(400,220))
