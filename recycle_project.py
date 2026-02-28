import pygame,time,random
from pygame.locals import *

pygame.init()

wind = pygame.display.set_mode((800,600))
bg_img = pygame.image.load("renewable.jpg")
bg = pygame.transform.scale(bg_img, (800,600))

score = 0

font = pygame.font.SysFont("Times new roman",20)

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.jpg")
        self.image = pygame.transform.scale(self.image,(45,51))
        self.x = 10
        self.y = 30
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

class Recyclables(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image) 
        self.image = pygame.transform.scale(self.image, (31,41))
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
recycle_group = pygame.sprite.Group()
recycle_img = ["paper_bag.jpg","pencil.jpg","box.jpg"]
none_recycle_group = pygame.sprite.Group()

for j in range (10):
    plastic = None_recyclables()
    plastic.rect.y = random.randint(20,550)
    plastic.rect.x = random.randint(20,750)
    none_recycle_group.add(plastic)
    all_images.add(plastic)

for i in range(34):
    waste = Recyclables(random.choice(recycle_img))
    waste.rect.x = random.randint(20,750)
    waste.rect.y = random.randint(20,550)
    recycle_group.add(waste)
    all_images.add(waste)



clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    score_text = font.render("Score : " + str(score), True, "white")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        bin.rect.y += 10
    if keys[pygame.K_w]:
        bin.rect.y -= 10 
    if keys[pygame.K_a]:
        bin.rect.x -= 10
    if keys[pygame.K_d]:
        bin.rect.x += 10
    
    collide_recycle = pygame.sprite.spritecollide(bin,recycle_group, True)
    collide_nonerecycle = pygame.sprite.spritecollide(bin, none_recycle_group, True)

    for k in collide_recycle:
        score += 1 
    for k in collide_nonerecycle:
        score -= 1

    wind.blit(bg, (0,0))
    all_images.draw(wind)
    wind.blit(score_text, (10,10))
    pygame.display.update()       
        