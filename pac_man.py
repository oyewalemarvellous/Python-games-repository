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

class Walls(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super().__init__()
        self.image = pygame.draw.rect(wind, color, (size * x, size *y, size,size))

food_group = pygame.sprite.Group()

class Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pygame.draw.circle(wind,green, ( size*x + size//2, size*y +size//2),5 )

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            wall_group.add(Walls(j,i,blue))
        elif maze[i][j] == 2:
            wall_group.add(Walls(j,i,green))
        else:
           food_group.add(Food(j,i))

class Pac_man(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("pac_man_open_left.jpg")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

    def change_image(self,image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (20,20))

images = pygame.sprite.Group()


man = Pac_man( 260,260)
images.add(man)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                man.change_image("pac_man_open_left.jpg")
                man.rect.x -= 5
                images.empty()
                images.add(man)
            if event.key == pygame.K_RIGHT  :
                man.change_image("pac_man_open_right.jpg")
                man.rect.x += 5
                images.empty()
                images.add(man)
            if event.key == pygame.K_UP:
                man.change_image("pac_man_open_up.jpg")
                man.rect.y -= 5
                images.empty()
                images.add(man)
            if event.key == pygame.K_DOWN:
                man.change_image("pac_man_open_down.jpg")
                man.rect.y -= 5
                images.empty()
                images.add(man) 

    images.draw(wind)
    pygame.display.update()