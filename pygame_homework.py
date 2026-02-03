import pygame
pygame.init()

screen = pygame.display.set_mode((200,200))
screen.fill((45,68,14))
runner = pygame.image.load("boy_1.jpg")
pygame.display.update()
while True:
        screen.fill((45,68,14))
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            print("hello")
            if event.key == pygame.K_SPACE:
                print("space")
                runner = pygame.image.load("boy_2.jpg")
                screen.blit(runner,(0,0))
                pygame.display.update()
        elif event.type == pygame. KEYUP:
            if event.key == pygame.K_SPACE:
                print("hi")
                runner = pygame.image.load("boy_1.jpg")
                screen.blit(runner,(0,0))
                pygame.display.update()   
     