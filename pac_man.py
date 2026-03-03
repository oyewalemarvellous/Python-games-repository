import pygame,time,random,turtle

pygame.init()

WIDTH = 300
HEIGHT = 300

wind = pygame.display.set_mode((WIDTH,HEIGHT))
wind.fill("black")

black = (0, 0, 0)
green = (21, 250, 5)
blue = (7, 36, 250)
yellow = (238, 242, 5)

maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,0,1,0,1,1,0,1,1],
        [1,0,0,0,0,0,1,0,1,0,1,0,0,0,1],
        [1,0,0,0,0,0,1,0,1,0,1,0,1,1,1],
        [1,1,1,1,0,0,1,0,1,0,1,0,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
        [1,0,0,1,1,0,1,1,1,1,0,0,1,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,0,1,0,0,0,0,0,0,1],
        [1,0,0,1,0,0,0,1,0,0,1,0,0,0,1],
        [1,1,1,1,0,1,1,0,0,0,0,1,1,1,1],
        [1,0,1,0,0,0,0,1,0,1,1,0,0,0,1]]
size = 20
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            pygame.draw.rect(wind, blue,( size*j, size*i, size,size) )

        else:
            pygame.draw.circle(wind, green, ( size*j + size//2, size*i +size//2),5 )
class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
"""class Pac_man(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

image = pygame.sprite.Group()
man = Pac_man("pac_man_open.jpg", 350,300)
image.add(man)"""

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    


    """image.draw(wind)"""
    pygame.display.update()