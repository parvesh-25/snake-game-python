
#1 import
from unittest import TextTestRunner
import pygame
import sys
import random
import time

# inisialisasi pygame
pygame.init()

# 3
# lebar display x = 600, y = 400
display_x = 600
display_y = 400

#4 inisialisasi display
game_display= pygame.display.set_mode((display_x, display_y))
#5 judul game
pygame.display.set_caption('game ular')


# 5 variabel warna 
blue = pygame.Color(82, 178, 207)
prussian_blue = pygame.Color(0, 44, 83)
cream = pygame.Color(237, 230, 211)
red = pygame.Color(255,105,97)

# ganti warna background
game_display.fill(cream)

# font
message_font = pygame.font.SysFont('ubuntu',60)
score_font = pygame.font.SysFont('ubuntu', 20)

# variabel snake

snake_pos = [100, 50]
snake_body = [[100,50],[80,50],[70,50]]
change_to = 'RIGHT'
direction = "RIGHT"

# food
food_pos = [random.randrange(1, display_x //10)*10, random.randrange(1, display_y //10)*10]
food_spawn = True

# score
score =0

# game over funct
def game_over():
    game_over_surface = message_font.render('Antum Kalah', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (display_x/2, display_y/4)
    game_display.fill(prussian_blue)
    game_display.blit(game_over_surface, game_over_rect)
   
    pygame.display.flip()
    time.sleep(2)
   
    pygame.quit()

# show score funct
def show_score():
    score_surface = score_font.render('Your poin:' + str(score), True, blue)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (270, 10)
    game_display.blit(score_surface, score_rect)
    pygame.display.flip()


# running game
while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
        
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"

            if event.key == pygame.K_UP:
                change_to = "UP"
           
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"

    game_display.fill(cream) 

    # create snake
    for pos in snake_body:
        pygame.draw.ellipse(game_display, blue,pygame.Rect(pos[0], pos[1], 10, 10))
    snake_body.insert(0, list(snake_pos[:]))

    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"

    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    # snake run
    if direction == "RIGHT":
        snake_pos[0] += 10
    
    if direction == "LEFT":
        snake_pos[0] -=10

    if direction == "UP":
        snake_pos[1] -= 10

    if direction == "DOWN":
        snake_pos[1] += 10

    # draw food
    pygame.draw.rect(game_display, red, pygame.Rect(food_pos[0], food_pos[1], 10,10))

    # ular makan
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
        score += 1

    else:
        snake_body.pop()

    # food spawn
    if not food_spawn:

        food_pos = [random.randrange(1, display_x //10)*10, random.randrange(1, display_y//10)*10]
    food_spawn = TextTestRunner

    # show score
    show_score()

    # game over
    if snake_pos[0] > display_x or snake_pos[0] < 0 or snake_pos[1] > display_y or snake_pos[1] < 0:
        game_over()

    
    pygame.time.Clock().tick(10)
    pygame.display.update()
