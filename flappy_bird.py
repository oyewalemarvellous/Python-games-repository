import pygame,time,random

pygame.init()

width = 800
height = 400

wind = pygame.display.set_mode((800, 400))
bg_img = pygame.image.load("flappy_bird_background.jpg")
bg = pygame.transform.scale(bg_img, (800, 400))

bird = pygame.image.load("flappy_bird_up.jpg")
bird_x = 15
bird_y = height/2
bird_rect = bird.get_rect()

pipe_up = pygame.image.load("pipe_up.jpg")
pipe_x = 400
pipe_y = 277
pipe_down = pygame.image.load("pipe_down.jpg")
pipe_down_y = -135
pipe_list = []


font = pygame.font.Font(None, 30)

score = 0
game_over = False
timer = 0

i = 0

def createpipe():
    global pipe_gap,rect_2

    y = random.randint(200,300)
    rect = pipe_up.get_rect(topleft = (800,y))
     
    pipe_gap = 150 
    rect_2 = pipe_down.get_rect(bottomleft = (800,y - pipe_gap))
    
    pipe_list.append(rect)
    pipe_list.append(rect_2)



while True:

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

    wind.blit(bg, (i, 0))
    wind.blit(bg, (width + i, 0))
    if i <= -width:
        wind.blit(bg , (width + i, 0))
        i = 0 
 
    i -= 0.1

    text = font.render("Score : " + str(score),True,"white")

    bird_y += 0.1
    bird_rect.topleft = (bird_x, bird_y)

    timer += 1
    if timer > 120:
        createpipe()
        timer = 0

    count = 0

    for p in pipe_list:
        p.x -=1
        if count % 2 == 0:
            wind.blit(pipe_up,p)
        else:
            wind.blit(pipe_down,p)
        
        count += 1
        

        if bird_rect.colliderect(p):
            game_over = True 
        
        if p.x == bird_x :
            score += 2

    if game_over == True or bird_y > height or bird_y < 0:
        """game_over_bg = pygame.image.load("gameoverscreen.jpg")
        go = pygame.transform.scale(game_over_bg, (800,500))
        wind.blit(go, (0,0))
        pygame.display.update()
        break """
        pygame.time.wait(5000)
    wind.blit(text, (10, 10))
    wind.blit(bird, (bird_x, bird_y))
    pygame.display.update()





