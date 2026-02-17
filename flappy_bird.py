import pygame,time,random 

pygame.init()

width = 800
height = 500
wind = pygame.display.set_mode((800, 500))
bg_img = pygame.image.load("flappy_bird_background.jpg")
bg = pygame.transform.scale(bg_img, (800, 500))

bird = pygame.image.load("flappy_bird_up.jpg")
bird_x = 15
bird_y = height/2
bird_rect = bird.get_rect()

pipe = pygame.image.load("pipe_up.jpg")
pipe_x = 730
pipe_y = 277
pipe_rect = pipe.get_rect()
pipe_gap = 150 
pipe_list = []

font = pygame.font.Font(None, 30)

score = 0

game_over = False
running = True

i = 0

def createpipe():
    global pipe_x,pipe_y
    pipes = wind.blit(pipe, (pipe_x,pipe_y))
    pipe_list.append(pipes)
    print(pipe_list)

while True:

    text = font.render("Score : " + str(i),True,"white")

    wind.blit(bg, (i, 0))
    wind.blit(bg, (width + i, 0))
    if i <= -width:
        wind.blit(bg , (width + i, 0))
        i = 0 
 
    i -= 0.1

    bird_y += 0.1
    
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            bird_y -= 20
            bird = pygame.image.load("flappy_bird_down.jpg")
            wind.blit(bird, (bird_x,bird_y))
            pygame.display.update()
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            bird = pygame.image.load("flappy_bird_up.jpg")
            wind.blit(bird,(bird_x,bird_y))
            pygame.display.update()

    createpipe()
    for pipe in pipe_list:
        pipe.x -= 0.1
        

    pipe_rect.topleft = (pipe_x,pipe_y)
    bird_rect.topleft = (bird_x, bird_y)

    if bird_rect.colliderect(pipe_rect):
        print("hit")
        game_over = True 

    if game_over == True or bird_y > height or bird_y < 0:
        game_over_bg = pygame.image.load("gameoverscreen.jpg")
        go = pygame.transform.scale(game_over_bg, (800,500))
        wind.blit(go, (0,0))
        pygame.display.update()
        pygame.time.wait(5000)
        break 
 
    wind.blit(text, (10, 10))
    wind.blit(bird, (bird_x, bird_y))
    pygame.display.update()
