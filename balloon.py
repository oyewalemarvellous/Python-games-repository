import pgzrun
import random

# -- Game Configuration --
TITLE="Pop The Balloon" 
WIDTH,HEIGHT= (600,600)

# -- Game State variable --
balloons=[]
balloon_images=[]

# -- Drawing Function -- 
def draw():
    screen.blit("chopping_board",(0,0))
    for ball in balloons:
        ball.draw()
def balloons_movement():
    ball= Actor(random.randint(balloon_images))
    ball.y= HEIGHT
    ball.x= random.randint(50,550)
    balloons.append(ball)
##def on_mouse_down():
  ##  if yellow_balloon.collidepoint(pos):
        
for ball in balloons:
    animate(ball, y=100, duration=3)

# -- Run Game --
pgzrun.go()