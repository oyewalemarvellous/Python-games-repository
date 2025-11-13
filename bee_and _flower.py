import pgzrun
import random

WIDTH=600
HEIGHT=500

Bee=Actor("pixel_bee")
flower=Actor("flower")
Bee.pos= (0,50)
flower.pos= (300,400)
gameover= False

def draw():
    screen.blit("field_background",(0,0))
    Bee.draw()
    flower.draw()
    if gameover:
        screen.fill("red")
def flower_position():
    flower.x=random.randint(10,590)
    flower.y=random.randint(400,495)
def update():
    if keyboard.left:
        Bee.x -=2
    elif keyboard.right:
        Bee.x +=2
    elif keyboard.up:
        Bee.y -=2
    elif keyboard.down:
        Bee.y +=2
    flower_collective=Bee.colliderect(flower)
    if flower_collective:
        flower_position()
def timeup():
    global gameover
    gameover= True
clock.schedule(timeup,60.0)

pgzrun.go()
