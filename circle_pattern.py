import pgzrun
import random

WIDTH= 500
HEIGHT= 500

def draw():
    screen.fill("skyblue") # pyright: ignore[reportUndefinedVariable]
    radius=40
    screen.draw.circle((WIDTH/2,HEIGHT/2),radius,"black") # pyright: ignore[reportUndefinedVariable]
pgzrun.go()