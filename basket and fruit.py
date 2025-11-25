import pgzrun
import random
import time
#screen
WIDTH=600
HEIGHT=600
#basket and fruits
basket=Actor("basket")
apple=Actor("apple")
orange= Actor("orange")
fruits=[orange,apple]
score_name="Score:"
score = 0
#position basket
basket.pos= (WIDTH/2,560)
def draw():
    screen.blit("field_background",(0,0))
    screen.draw.text(score_name,center=(25,10))
    screen.draw.text(str(score),center=(55,10))
    basket.draw()
    for fruit in fruits:
        time.sleep(5)
        fruit.draw()
        
def fruit_positon():
    for fruit in fruits:
        fruit.x=random.randint(10,450)
        fruit.y=random.randint(0,10)
        
def update():
    global score
    global score_name
    for fruit in fruits:
        fruit.y += random.randint(1,5)
        if fruit.y > 600:
            fruit_positon()
            collision = basket.colliderect(fruit)
            if collision:
                fruit_positon()
                score +=1
    if keyboard.d:
        basket.x +=4
    elif keyboard.a:
        basket.x -=4
    

    



pgzrun.go()
