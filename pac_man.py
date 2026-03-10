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
        [1,0,0,0,0,0,1,0,1,0,1,0,1,0,1],
        [1,1,1,1,0,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
        [1,0,0,1,1,0,1,1,1,1,0,0,1,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,0,1,0,0,0,0,0,0,1],
        [1,0,0,1,0,0,0,1,0,0,1,0,0,0,1],
        [1,1,1,1,0,1,1,0,0,0,1,0,1,1,1],
        [1,0,1,0,0,0,0,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

size = 20

wall_group = pygame.sprite.Group()


food_group = pygame.sprite.Group()
class Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pygame.draw.circle(wind,green, ( size*x + size//2, size*y +size//2),5 )


for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            pygame.draw.rect(wind, blue,( size*j, size*i, size,size) )
        elif maze[i][j] == 2:
            pygame.draw.rect(wind, green, (size*j,size*i, size,size))

        else:
           dot = Food(j,i)
           food_group.add(dot)

"""class Pac_man(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("pac_man_open.jpg")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)"""

image = pygame.sprite.Group()
#man = Pac_man( 260,260)
#image.add(man)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        """if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                man = pygame.image.load("pac_man_open_left.jpg")
                man.rect.y =
                
    
    keys = pygame.key.get_pressed()"""


    image.draw(wind)
    pygame.display.update()