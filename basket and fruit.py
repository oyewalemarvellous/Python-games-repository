import pgzrun
import random
import time
#screen
WIDTH=600
HEIGHT=600
#basket actor
basket=Actor("basket")
#list
fruits=[]
fruit_images=["apple","pear","orange"]
bombs=[]
#score
score_name="Score:"
score = 0
#basket poition
speed= 2
basket.pos= (WIDTH/2,560)
#functions
def draw():
    screen.blit("field_background",(0,0))
    screen.draw.text(score_name,center=(25,10))
    screen.draw.text(str(score),center=(65,10))
    basket.draw()
    for fruit in fruits:
        fruit.draw()
    for explosion in bombs:
        explosion.draw()
    if score < 0:
            screen.clear()
            screen.blit("game_over_screen",(0,0))
              

def change_speed():
    global speed
    speed += 2
    clock.schedule(change_speed,30)  

def fruit_positon():
    fruit=Actor(random.choice(fruit_images))
    fruit.x=random.randint(10,450)
    fruit.y=random.randint(0,10)
    fruits.append(fruit)
    clock.schedule(fruit_positon,random.randint(1,2)) 
def  bomb_position():
    bomb=Actor("bomb")
    bomb.x=random.randint(10,450)
    bomb.y=random.randint(0,10)
    bombs.append(bomb)
    clock.schedule(bomb_position,random.randint(15,30)) 

def update():
    global score
    global score_name
    
    for fruit in fruits[:]:
        fruit.y += speed
        if fruit.y > 600:
            fruits.remove(fruit)
            score -= 1
        collision = basket.colliderect(fruit)
        if collision:
            fruits.remove(fruit)
            score +=1
    for bomb in bombs[:]:
        bomb.y +=2
        if bomb.y > 600:
            bombs.remove(bomb)
        impact= basket.colliderect(bomb)
        if impact:
            bombs.remove(bomb)
            score -= 3
        
    if keyboard.d:
        basket.x +=6
    elif keyboard.a:
        basket.x -=6
    
    

clock.schedule(fruit_positon,2)    
clock.schedule(bomb_position,30)
clock.schedule(change_speed,30)



pgzrun.go()
