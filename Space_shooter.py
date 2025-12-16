import pgzrun
import time
import random

TITLE = "Space Shooter"
WIDTH,HEIGHT=(600,600)

space_craft=Actor("space_craft")
space_craft.pos= (WIDTH/2,560)
lazers=[]
alien_lazer=[]
score_name= "Scores :"
score= 0
speed= 2
boss_health= 500
alien_troops=[]
boss_lazer=[]
game_over = False
is_boss= False
boss= Actor("mother_ship")
# creates boss 
def final_boss():
    global is_boss
    global boss 
    boss.pos= (WIDTH/2,100)
    is_boss= True
    boss_shoot()
# helps boss move
def boss_movement():
    boss.y += 0.3
def alien_fleet():
    if not is_boss:
        for i in range(8):
            for c in range(3):
                alien= Actor("alien_invader")
                alien.x= 50 + i * 70
                alien.y= 50 + c * 60
                alien_troops.append(alien)
alien_fleet()
def space_craft_collision():
    global game_over
    for alien in alien_troops:
        if alien.colliderect(space_craft):
            game_over = True
            """elif alien.y > 600:
            game_over = True """
        elif score < 0:  
            game_over= True 
    
def alien_shoot():
    if not is_boss:
        shooter=random.choice(alien_troops)
        laser=Actor("blue_lazer_beam")
        laser.pos=(shooter.x,shooter.y)
        alien_lazer.append(laser)
        clock.schedule(alien_shoot,1.0)
clock.schedule(alien_shoot,1.0)
def boss_shoot():
    if is_boss:
        ammo = Actor("blue_lazer_beam")
        x=random.randint(int(boss.x)-100,int(boss.x)+100)
        ammo.pos= (x,boss.y)
        boss_lazer.append(ammo)
        clock.schedule(boss_shoot,5.0)

def max_score():
    if score > 300:
        screen.clear()
        screen.blit("mission_complete",(0,0))
        return
def draw():
    space_craft_collision()
    if  game_over:
        screen.clear()
        screen.blit("game_over_screen",(0,0))
        return
    screen.blit("space_background",(0,0))
    space_craft.draw()
    for alien in alien_troops:
        alien.draw()
    for lazer in lazers:
        lazer.draw()
    screen.draw.text(score_name,center=(25,10))
    screen.draw.text(str(score),center=(65,10))
    screen.draw.text(str(boss_health),center= (560,10))
    if is_boss and boss_health  > 0:
        boss.draw()
    for laser in boss_lazer:
        laser.draw()
    max_score()
    for laser in alien_lazer:
        laser.draw()
def alien_fleet_movement():
    for alien in alien_troops:
        alien.y +=speed
clock.schedule_interval(alien_fleet_movement,0.1)
def on_key_down(key):
    if key == keys.SPACE:
        lazer=Actor("lazer_beam")
        sounds.space_gun.play()
        lazers.append(lazer)
        lazers[-1].x=space_craft.x
        lazers[-1].y=space_craft.y
def space_craft_wallcollision():
    if space_craft.x > 600:
        space_craft.pos= (5,560)
    if space_craft.x < 0:
        space_craft.pos= (550,560)
def update():
    global is_boss
    global boss_health
    global score
    global speed
    global game_over

    if  game_over:
        return
    for lazer in lazers:
        lazer.y -=3
        if is_boss:
            if boss.colliderect(lazer):
                lazers.remove(lazer)
                boss_health -= 10
        if lazer.y < 0 and lazer in lazers:
            lazers.remove(lazer)
        for alien in alien_troops:
            if alien.colliderect(lazer) and lazer in lazers:
                lazers.remove(lazer)
                alien_troops.remove(alien)
                score +=2
    for laser in alien_lazer:
        laser.y += 4
        if space_craft.colliderect(laser):
            score-=3
            alien_lazer.remove(laser)

        elif laser.y > HEIGHT:
            alien_lazer.remove(laser)
    for laser in boss_lazer:
        laser.y +=4
        if laser.colliderect(space_craft):
            boss_lazer.remove(laser)
            score -= 50
    if space_craft.colliderect(boss):
        game_over = True
    if score == 50:
        final_boss()
    if is_boss:
        boss_movement()
    if boss_health <= 0:
        is_boss = False 
        boss_health = 500
    

    
    space_craft_wallcollision()
    if not alien_troops:
        alien_fleet()
        speed += 2
    if speed > 6:
        speed = 6
    if keyboard.d:
        space_craft.x += 5
    if keyboard.a:
        space_craft.x -= 5   
pgzrun.go()