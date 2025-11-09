import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="Alien invasion."
message=""
Alien=Actor("alien_man")
def draw():
    screen.fill("black")
    Alien.draw()
    screen.draw.text(message,center=(WIDTH/2,50))

def alien_position():
    Alien.x=random.randint(90,490)
    Alien.y=random.randint(90,490)
def on_mouse_down(pos):
    global message
    if Alien.collidepoint(pos):
        alien_position()
        message="good shot"
    else:
        message="bad shot "

pgzrun.go()
