import random
import pygame
import shelve
from os import path
from Explosion import Explosion
from Player import Player
from Meteor import Meteor
from TekkiePygameLib import Label, Button, InputBox
from ShieldBar import ShieldBar
from Boss import Boss

WIN_WIDTH = 500
WIN_HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MY_COLOR = (139, 247, 192)

img_dir = path.join(path.dirname(__file__), 'img')
explosion_img_dir = path.join(path.dirname(__file__), 'img/Explosions')
sound_dir = path.join(path.dirname(__file__), 'sounds')
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
stop_meteor = True
boss_clock =  0

pygame.mixer.init()
pygame.mixer.music.load(path.join(sound_dir, 'through_space.ogg'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

user_score = Label(x=270, y=20, text="Score: 0", color=WHITE, size=40)
stop_bg_music = Button(440, 0, 100, 23, 'Stop sounds')
shoot_sound = pygame.mixer.Sound(path.join(sound_dir, 'pew.wav'))
background = pygame.image.load(path.join(img_dir, 'spaceBG.png')).convert()
background_StartScreen = pygame.image.load(path.join(img_dir, 'StartScreenBG.png')).convert()
my_player_img = pygame.image.load(path.join(img_dir, 'spaceShip.png')).convert()
my_boss_img = pygame.image.load(path.join(img_dir, 'spaceShip3.png')).convert()
my_meteor_img = pygame.image.load(path.join(img_dir, 'meteor.png')).convert()
my_bullet_img = pygame.image.load(path.join(img_dir, 'bullet.png')).convert()
my_player = Player(win, my_player_img, my_bullet_img, shoot_sound)
my_shieldbar = ShieldBar(win, 10, 10)

meteor_images = []
meteor_list = ["meteor1.png", "meteor2.png", "meteor3.png", "meteor4.png", "meteor5.png",
               "meteor6.png", "meteor7.png", "meteor8.png", "meteor9.png"]
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)))
    
all_sprites = pygame.sprite.Group()
all_sprites.add(my_player)

explosion_animation_dict = {'large': [], 'small': []}
meteors = pygame.sprite.Group()

boss = pygame.sprite.Group()

def stop_sounds():
    pygame.mixer.music.pause()
    explosions_sounds[0].set_volume(0)
    explosions_sounds[1].set_volume(0)
    shoot_sound.set_volume(0)

def play_sounds():
    pygame.mixer.music.unpause()
    explosions_sounds[0].set_volume(0.2)
    explosions_sounds[1].set_volume(0.2)
    shoot_sound.set_volume(0.2)

def show_opening_screen():
    win.blit(background, (0, 0))
    title = Label(x=250, y=200, text='Space Invaders', color=WHITE, size=65)
    credit = Label(x=250, y=500, text='TekkieUni and MG', color=WHITE, size=25)
    game_instructions = Label(x=250, y=400, text='To move use the arrows, to fire use space.', color=WHITE, size=30)
    start = Button(250, 330, 90, 23, text='Start')
    game_instructions.draw(win)
    start.draw(win)
    credit.draw(win)
    title.draw(win)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if start.is_clicked():
                return False

def game_over(p_message):
    win.blit(background, (0, 0))
    title = Label(x=250, y=200, text='GAME OVER', color=WHITE, size=65)
    title.draw(win)
    start_over = Button(250, 350, 90, 23, text='Start over')
    start_over.draw(win)
    message = Label(x=250, y=280, text=p_message, color=WHITE, size=40)
    message.draw(win)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if start_over.is_clicked():
                return False

def create_meteor():
    meteor = Meteor(win, meteor_images)
    all_sprites.add(meteor)
    meteors.add(meteor)

def create_boss():
    boss = Boss(win, my_boss_img, random.randint(3, 5)
    all_sprites.add(boss)

while boss_clock!= 100:
  for i in range(9):
    img_name = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(explosion_img_dir, img_name)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    
create_boss()
boss_clock = 0

explosions_sounds = []
for sound in ['expl2.wav', 'expl2.wav']:
    explosions_sounds.append(pygame.mixer.Sound(path.join(sound_dir, sound)))
    
def create_explosion(p_explosion_loc, p_explosion_size):
    my_explosion = Explosion(p_explosion_loc, p_explosion_size, explosion_animation_dict[p_explosion_size], explosions_sounds)
    all_sprites.add(my_explosion)
