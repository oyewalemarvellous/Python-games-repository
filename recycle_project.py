import pygame,time
from pygame.locals import *

pygame.init()

wind = pygame.display.set_mode((800,600))
bg_img = pygame.image.load("renewable.jpg")
bg = pygame.transform.scale(bg_img, (800,600))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.jpg")
        self.image = pygame.transform.scale(self.image,(45,51))
        self.rect = self.image.get_rect()

class Recyclables(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image) 
        self.image = pygame.transform.scale(31,41)
        self.rect = self.image.get_rect()

class None_recyclables(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic_bag.jpg")
        self.image = pygame.transform.scale(self.image,(31,41))
        self.rect = self.image.get_rect()

bin = Bin()

all_images = pygame.sprite.Group()
all_images.add(bin)
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        bin.rect.y += 10
    if keys[pygame.K_w]:
        bin.rect.y -= 10 
    if keys[pygame.K_a]:
        bin.rect.x -= 10
    if keys[pygame.K_d]:
        bin.rect.x += 10

    wind.blit(bg, (0,0))
    all_images.draw(wind)

    pygame.display.update()       
        