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
fruits=[]

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
        fruit.draw()
        
def apple_positon():
    apple=Actor("apple")
    apple.x=random.randint(10,450)
    apple.y=random.randint(0,10)
    fruits.append(apple)
    clock.schedule(apple_positon,random.randint(1,4))
def orange_positon():
    orange=Actor("orange")
    orange.x=random.randint(10,450)
    orange.y=random.randint(0,10)
    fruits.append(orange)
    clock.schedule(orange_positon,random.randint(1,4))        
def update():
    global score
    global score_name
    for fruit in fruits[:]:
        fruit.y += 2
        if fruit.y > 600:
            fruits.remove(fruit)
        collision = basket.colliderect(fruit)
        if collision:
            fruits.remove(fruit)
            score +=1
    if keyboard.d:
        basket.x +=6
    elif keyboard.a:
        basket.x -=6
    

clock.schedule(apple_positon,2)    
clock.schedule(orange_positon,4)



pgzrun.go()
