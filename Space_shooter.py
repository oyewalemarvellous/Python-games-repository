import pgzrun
import time
import random

TITLE = "Space Shooter"
WIDTH,HEIGHT=(600,600)

space_craft=Actor("space_craft")
space_craft.pos= (WIDTH/2,560)
lazers=[]

alien_troops=[]
def alien_fleet():
    for i in range(8):
        for c in range(3):
            alien= Actor("alien_invader")
            alien.x= 50 + i * 70
            alien.y= 50 + c * 60
            alien_troops.append(alien)
alien_fleet()
def draw():
    screen.blit("space_background",(0,0))
    space_craft.draw()
    for alien in alien_troops:
        alien.draw()
def alien_fleet_movement():
    for alien in alien_troops:
        alien.y +=2
clock.schedule_interval(alien_fleet_movement,0.1)
def on_key_down(key):
    if key == keys.SPACE:
        lazer=Actor("lazer_beam")
        lazers.append(lazer)
        lazers[-1].x=space_craft.x
        lazers[-1].y=space_craft.y
def update():
    for lazer in lazers[:]:
        lazer.y -=3
        
    if keyboard.d:
        space_craft.x += 5
    if keyboard.a:
        space_craft.x -= 5   

pgzrun.go()