import pgzrun
import random 

WIDTH=500
HEIGHT=400

def draw():

    screen.fill("green")
    w=100
    h=50
    for i in range(15):
        rect=Rect((0,0),(w,h))
        rect.center=(WIDTH/2,HEIGHT/2)
        screen.draw.rect(rect,"black")
        h+=20
        w-=10

pgzrun.go()
