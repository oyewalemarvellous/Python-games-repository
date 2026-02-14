import pygame 
import random
import time
pygame.init()

s = pygame.display.set_mode((500,500))
fruit = pygame.image.load("star.jpg")
catcher = pygame.image.load("space_craft_up.jpg")
background = pygame.image.load("snake_background.jpg")
game_over = pygame.image.load("game_over_screen.jpg")
active = False 

font = pygame.font.Font(None,30)
score = 0
angle = 0

catcher_x = 250
catcher_y = 450
catcher_rect = catcher.get_rect()

def fruit_movement():
    global fruit_x,fruit_y
    fruit_x = random.randint(10,450)
    fruit_y = random.randint(10,450)

fruit_movement()
fruit_rect = fruit.get_rect()

last_time = 0

while True:
    text = font.render("Score : " + str(score),True,"white")
    current_time = pygame.time.get_ticks()
    if current_time - last_time > 3000:
        fruit_movement()
        last_time = current_time
        score -= 1
    if score < 0:
        s.blit(game_over,(0,0))
        pygame.display.update()
        time.sleep(4.0)
        break

    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            catcher_x -= 20
            catcher = pygame.image.load("space_craft_left.jpg")
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            catcher_x += 20
            catcher = pygame.image.load("space_craft_right.jpg")
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            catcher_y -= 20
            catcher = pygame.image.load("space_craft_up.jpg")
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            catcher_y += 20
            catcher = pygame.image.load("space_craft_down.jpg")
        if catcher_x > 500:
            catcher_x = 440
        if catcher_x < 0:
            catcher_x = 40
        if catcher_y > 440:
            catcher_y = 440
        if catcher_y < 0:
            catcher_y = 40
    
    catcher_rect.topleft = (catcher_x,catcher_y)
    fruit_rect.topleft = (fruit_x,fruit_y)

    if catcher_rect.colliderect(fruit_rect):
        score += 2
        fruit_movement()

    s.blit(background,(0,0))
    s.blit(text,(10,10))
    s.blit(fruit,(fruit_x,fruit_y))
    s.blit(catcher,(catcher_x,catcher_y))
    pygame.display.update()