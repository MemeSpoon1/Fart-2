import pygame
from pygame import mixer
import random

pygame.init()

# Icon
icon = pygame.image.load("./Other/icon.png")
pygame.display.set_icon(icon)

# Screen size
screen = pygame.display.set_mode((800, 600))

# Window name
pygame.display.set_caption("fart 2")

# Sprite loading and location
playerImg = pygame.image.load('./Sprites/Player.png')
playerX = 370
playerY = 480
playerX_change = 0

spriteImg = pygame.image.load("./Sprites/sprite.png")
spriteX = 372
spriteY = 430
spriteX_change = 0

bulletImg = pygame.image.load("./Sprites/bullet.png")
bulletX = 104
bulletY = -178
bulletx_change = 0
bulletY_change = 0
bullet_state = "ready"

enemyImg = pygame.image.load("./Sprites/enemy.png")
enemyX = random.randint(0, 800)
enemyY = 50
enemyX_change = 4
enemyY_change = 2

background = pygame.image.load("./Sprites/background.png")

# Sprite rendering
def player(x, y):
    screen.blit(playerImg, (x, y))

def sprite(x, y):
    screen.blit(spriteImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 7, y + 10))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Music
mixer.music.load("./Music/megalovania.mp3")
mixer.music.play(-1)

# Sounds
    
# Game loop
running = True
while running:
    screen.fill((0, 255, 0))
    screen.blit(background,(0,0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
            if event.key == pygame.K_LEFT:
                spriteX_change = -7
            if event.key == pygame.K_RIGHT:
                spriteX_change = 7
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)

    playerX += playerX_change
    spriteX += spriteX_change
    enemyX += enemyX_change

    # Window collision
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    if spriteX <= 0:
        spriteX = 0
    elif spriteX >= 768:
        spriteX = 768

    if enemyX <= 0:
        enemyX_change = 4
    elif enemyX >= 736:
        enemyX_change = -4
    
    # Bullet config
    if bulletY <=0 :
        bulletY = -178
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

     
    player(playerX, playerY)
    sprite(spriteX, spriteY)
    enemy(enemyX, enemyY)
    pygame.display.update()





