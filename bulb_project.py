import pygame
pygame.init()
screen = pygame.display.set_mode ((200,200))
screen.fill((255,255,255))
image=pygame.image.load("bulb.jpg")
pygame.display.update()
while True:
    event = pygame.event.poll()
    if event.type == pygame. MOUSEBUTTONDOWN:
        image=pygame.image.load("bulb.jpg")
        screen.blit(image, (0,0))
        pygame.display.update()
    elif event.type == pygame. MOUSEBUTTONUP:
        image=pygame.image.load("bulb2.jpg")
        screen.blit (image, (0,0))
        pygame.display.update()