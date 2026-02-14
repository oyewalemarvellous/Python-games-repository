import pygame,time 

pygame.init()
width = 500
height = 400
s = pygame.display.set_mode((width , height))
background = pygame.image.load("flappy_bird_background.jpg")

bird = pygame.image.load("flappy_bird_up.jpg")
bird_down = pygame.image.load("flappy_bird_down.jpg")

pipe_up = pygame.image.load("pipe_up.jpg")
pipe_down = pygame.image.load("pipe_down.jpg")

bird_y = 15
bird_x = height/2
bird_rect = bird.get_rect()

pipe_y = 200
pipe_x = 400
pipe_rect = pipe_up.get_rect()

def pipe():
    global pipe_x,pipe_y
    s.blit(pipe_up,(pipe_x,pipe_y))
    pipe_rect.topleft = (pipe_x,pipe_y)
    
while True:

    s.blit(background , (0 , 0))
    event = pygame.event.poll()
    bird_y += 0.2
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            bird_y -= 30
            bird =  pygame.image.load("flappy_bird_up.jpg")
            s.blit(bird,(bird_x,bird_y))
    else:
        bird = pygame.image.load("flappy_bird_down.jpg")
        s.blit(bird,(bird_x,bird_y))
    bird_rect.topleft = (bird_x,bird_y)
    pipe_x -= 0.2
    pipe_rect.topleft = (pipe_x,pipe_y)
    if bird_rect.colliderect(pipe_rect):
        print("hit")
        break
    s.blit(pipe_up,(pipe_x,pipe_y))
    pygame.display.update()
