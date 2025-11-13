import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="Alien invasion."
message=""
score= "score"
scores= 0
Alien=Actor("alien_man")
def draw():
    screen.fill("black") # pyright: ignore[reportUndefinedVariable]
    Alien.draw()
    screen.draw.text(message,center=(WIDTH/2,50)) # pyright: ignore[reportUndefinedVariable]
    screen.draw.text(score,center=(50,5))
    screen.draw.text(str(scores),center=(50,50)) # pyright: ignore[reportUndefinedVariable]
def alien_position():
    Alien.x=random.randint(90,490)
    Alien.y=random.randint(90,490)
def on_mouse_down(pos):
    global message
    global scores
    if Alien.collidepoint(pos):
        alien_position()
        message="good shot"
        scores +=1
    else:
        message="bad shot "
        scores -=2

pgzrun.go()
