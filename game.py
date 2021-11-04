import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 0)
pygame.display.set_caption("python game")

#### ----- placing icon-----
icon = pygame.image.load("image/space.png")
pygame.display.set_icon(icon)

### -----placing background image------
background = pygame.image.load("image/spaceplanet.png")

####--------placing image------
playerimg = pygame.image.load("image/space-invaders.png")
playerx = 400
playery = 500
player_changex = 0

###----placing enemy-------
enemyimg = []
enemyx = []
enemyy = []
enemy_changex = []
enemy_changey = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load("image/alien.png"))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(0, 300))
    enemy_changex.append(1)
    enemy_changey.append(40)

###----placing bullet-------
bulletimg = pygame.image.load("image/bullet.png")
bulletx = 0
bullety = 500
bullet_changex = 0
bullet_changey = 5
bullet_state = "start"

####--------score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textx = 10
texty = 10

####----game 0ver-----
over_font = pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    score = font.render("score : "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if (distance < 27):
        return True
    else:
        return False


run = True
while run:
    ### ----RGB--(red,green,blue)-----
    screen.fill((0, 50, 100))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        ##  ---defining key functions for player img---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_changex = -2
            if event.key == pygame.K_RIGHT:
                player_changex = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "start":
                    bulletx = playerx
                    bullet(bulletx, bullety)

        ### -----defining keys when released -----
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_changex = 0

    playerx += player_changex
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    for i in range(num_of_enemy):
        ##game over------
        if enemyy[i] > 450:
            for i in range(num_of_enemy):
                enemyy[i] = 2000
            game_over_text()
            break

        enemyx[i] += enemy_changex[i]
        if enemyx[i] <= 0:
            enemy_changex[i] = 1
            enemyy[i] += enemy_changey[i]
        elif enemyx[i] >= 736:
            enemy_changex[i] = -1
            enemyy[i] += enemy_changey[i]

        ## ----collision ----
        coll = collision(enemyx[i], enemyy[i], bulletx, bullety)
        if coll:
            bullety = 480
            bullet_state = "start"
            score_value += 1
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(0, 300)
        enemy(enemyx[i], enemyy[i], i)

    ###------fire
    if bullety <= 0:
        bullety = 480
        bullet_state = "start"

    if bullet_state == "fire":
        bullet(bulletx, bullety)
        bullety -= bullet_changey

    player(playerx, playery)
    show_score(textx,texty)
    pygame.display.update()
    
 Thank you
