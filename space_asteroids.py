import pygame
import random
pygame.init()

s = pygame.display.set_mode((500,500))

background =  pygame.image.load("space_background.jpg")
ship = pygame.image.load("space_craft.jpg")
rock = pygame.image.load("star.jpg")

score = 0
angle = 0

ship_rect = ship.get_rect()
rock_rect = rock.get_rect()

rock_y = random.randint(10,15)
rock_x = random.randint(10,480)

font = pygame.font.Font(None,30)

ship_x = 250
ship_y = 250

while True:
    text = font.render("score : " + str(score),True,"white")

    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            ship_x -=15
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            ship_x +=15
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            ship_y -=15
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            ship_y +=15

    rock_y += 0.1
    ship_rect.topleft = (ship_x,ship_y)
    rock_rect.topleft = (rock_x,rock_y)

    if ship_rect.colliderect(rock_rect) or rock_y > 500:
        print("you have been hit")
        score += 2
        scale_rock = pygame.transform.scale(rock,(70,70))
        s.blit(scale_rock,(rock_x,rock_y))
        """pygame.display.update()"""
        rock_y = 10
        rock_x = random.randint(10,480)
    s.blit(background,(0,0))
    s.blit(text,(10,10))
    s.blit(ship,(ship_x,ship_y))
    angle += 3
    rock = pygame.transform.rotate(rock,angle)
    s.blit(rock,(rock_x,rock_y))
    
    pygame.display.update()