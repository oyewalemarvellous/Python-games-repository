import pgzrun
import random
WIDTH=600
HEIGHT=400

TITLE= "Shooting star"

star= Actor("star")
star_2=Actor('star')
star_3=Actor("red_star")
star_4=Actor("black_star")
stars=[star,star_2,star_3,star_4]
star.x= random.randint(0,600)
star_2.x= random.randint(0,600)
star_3.x=random.randint(0,600)
star_4.x=random.randint(0,600)
def draw():
    screen.blit("space_background",(0,0))
    for star in stars:
        star.draw()
    
def update():
    for star in stars:
        star.y +=3
        star.x -=3
   
    
pgzrun.go()