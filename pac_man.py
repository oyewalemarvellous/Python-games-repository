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

start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()
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
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("brick.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

food_group = pygame.sprite.Group()

class Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pac_man_ghost.png")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

    def movement(self):
        direction = random.randint(1,4)
        if direction == 1:
            self.rect.x -= 20
            collide_ghost = pygame.sprite.spritecollide(self, wall_group, False)
            for j in collide_ghost:
                self.rect.x += 20
                break
        elif direction == 2:
            self.rect.x += 20
            collide_ghost = pygame.sprite.spritecollide(self, wall_group, False)
            for j in collide_ghost:
                self.rect.x -= 20
                break
        elif direction == 3:
            self.rect.y -= 20
            collide_ghost = pygame.sprite.spritecollide(self, wall_group, False)
            for j in collide_ghost:
                self.rect.y += 20
                break 
        elif direction == 4:
            self.rect.y += 20
            collide_ghost = pygame.sprite.spritecollide(self, wall_group, False)
            for j in collide_ghost:
                self.rect.y -= 20
                break
        

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

ghost_group = pygame.sprite.Group()
images = pygame.sprite.Group()
ghost = Ghost(100,100)
ghost_2 = Ghost(240,100)
ghost_3 = Ghost(240,200)
ghost_group.add([ghost, ghost_2, ghost_3])





man = Pac_man( 260,260)
images.add(man)
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 0:
            food = Food(j * 20,i * 20)
            food_group.add(food)
            images.add(food)
food_group.draw(wind)
pygame.display.update()

for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:
                wall = Walls(j * 20,i * 20)
                wall_group.add(wall)
                images.add(wall)
    
running = True


while running:
    current_time = pygame.time.get_ticks()
    wind.fill((0, 0, 0))
   
    images.draw(wind)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                man.rect.x -= 20
                collide_wall = pygame.sprite.spritecollide(man, wall_group, False )
                for i in collide_wall:
                    man.rect.x += 20
                    break
                man.change_image("pac_man_open_left.jpg")

            if event.key == pygame.K_RIGHT  :
                man.rect.x += 20
                collide_wall = pygame.sprite.spritecollide(man, wall_group, False )
                for i in collide_wall:
                    man.rect.x -= 20
                    break
                man.change_image("pac_man_open_right.jpg")

            if event.key == pygame.K_UP:
                man.rect.y -= 20
                collide_wall = pygame.sprite.spritecollide(man, wall_group, False )
                for i in collide_wall:
                    man.rect.y += 20
                    break
                man.change_image("pac_man_open_up.jpg")

            if event.key == pygame.K_DOWN:
                man.rect.y += 20
                collide_wall = pygame.sprite.spritecollide(man, wall_group, False )
                for i in collide_wall:
                    man.rect.y -= 20
                    break
                man.change_image("pac_man_open_down.jpg")

        collide_food = pygame.sprite.spritecollide(man, food_group, True )

        for k in collide_food :
            food_group.remove(k)
    ghost_group.draw(wind)

    if current_time - start_time > 500:
        ghost.movement() 
        ghost_2.movement()
        ghost_3.movement()
        start_time = current_time  

    images.draw(wind)
    pygame.display.update()