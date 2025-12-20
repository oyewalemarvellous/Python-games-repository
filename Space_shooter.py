import pgzrun
import random

# --- Game Configuration ---

TITLE = "Space Shooter"
WIDTH, HEIGHT = (600, 600)

# --- Actors & Assets ---

space_craft = Actor("space_craft")
space_craft.pos = (WIDTH/2, 560)

boss = Actor("mother_ship")


# --- Game State Variables ---

lazers = []          # Player lasers
alien_lazer = []     # Alien lasers
boss_lazer = []      # Boss lasers
alien_troops = []    # Alien invaders

score_name = "Scores :"
score = 0
speed = 2
boss_health = 500
game_over = False
is_boss = False


# --- Setup Functions ---

def alien_fleet():
    if not is_boss:
        for i in range(8):      # 8 aliens per row
            for c in range(3):  # 3 rows
                alien = Actor("alien_invader")
                alien.x = 50 + i * 70
                alien.y = 50 + c * 60
                alien_troops.append(alien)

alien_fleet()  # Initial spawn

def final_boss():
    global is_boss, boss
    boss.pos = (WIDTH/2, 100)
    is_boss = True
    boss_shoot()
    clock.schedule_interval(boss_shoot, 1.0)

# --- Movement Functions ---

def boss_movement():
    boss.y += 0.3

def alien_fleet_movement():
    for alien in alien_troops:
        alien.y += speed

clock.schedule_interval(alien_fleet_movement, 0.1)

def space_craft_wallcollision():
    if space_craft.x > WIDTH:
        space_craft.pos = (5, 560)
    if space_craft.x < 0:
        space_craft.pos = (550, 560)

# --- Shooting Functions ---

def on_key_down(key):
    if key == keys.SPACE:
        lazer = Actor("lazer_beam")
        lazers.append(lazer)
        sounds.space_gun.play()
        lazers[-1].x = space_craft.x
        lazers[-1].y = space_craft.y

def alien_shoot():
    if not is_boss and alien_troops:
        shooter = random.choice(alien_troops)
        laser = Actor("blue_lazer_beam")
        laser.pos = (shooter.x, shooter.y)
        alien_lazer.append(laser)
        clock.schedule(alien_shoot, 1.0)

clock.schedule(alien_shoot, 1.0)

def boss_shoot():
    if is_boss:
        ammo = Actor("blue_lazer_beam")
        sounds.alien.play()
        x = random.randint(int(boss.x)-100, int(boss.x)+100)
        ammo.pos = (x, boss.y)
        boss_lazer.append(ammo)

# --- Collision Functions ---

def space_craft_collision():
    global game_over
    for alien in alien_troops:
        if alien.colliderect(space_craft):
            game_over = True
        elif score < 0:
            game_over = True
        elif alien.y ==  600:
            game_over= True 

# --- Drawing Functions ---

def max_score():
    if score > 300:
        screen.clear()
        screen.blit("mission_complete", (0, 0))
        return

def draw():
    space_craft_collision()

    if game_over:
        screen.clear()
        screen.blit("game_over_screen", (0, 0))
        return

    # Background and player
    screen.blit("space_background", (0, 0))
    space_craft.draw()

    # Aliens and lasers
    for alien in alien_troops:
        alien.draw()
    for lazer in lazers:
        lazer.draw()
    for laser in alien_lazer:
        laser.draw()
    for laser in boss_lazer:
        laser.draw()

    # score + boss health
    screen.draw.text(score_name, center=(25, 10))
    screen.draw.text(str(score), center=(65, 10))
    if is_boss and boss_health > 0:
        screen.draw.text("boss_health:", center=(480, 10))
        screen.draw.text(str(boss_health), center=(560, 10))
        boss.draw()

    max_score()

# --- Update Loop ---

def update():
    global is_boss, boss_health, score, speed, game_over

    if game_over:
        return

    # --- Player lasers ---
    for lazer in lazers[:]:
        lazer.y -= 3
        if is_boss and boss.colliderect(lazer):
            lazers.remove(lazer)
            boss_health -= 10
        elif lazer.y < 0:
            lazers.remove(lazer)
        else:
            for alien in alien_troops[:]:
                if alien.colliderect(lazer):
                    lazers.remove(lazer)
                    alien_troops.remove(alien)
                    score += 5

    # --- Alien lasers ---
    for laser in alien_lazer[:]:
        laser.y += 4
        if space_craft.colliderect(laser):
            score -= 5
            alien_lazer.remove(laser)
        elif laser.y > HEIGHT:
            alien_lazer.remove(laser)

    # --- Boss lasers ---
    for laser in boss_lazer[:]:
        laser.y += 4
        if laser.colliderect(space_craft):
            boss_lazer.remove(laser)
            score -= 20

    # --- Collisions with boss ---
    if space_craft.colliderect(boss):
        game_over = True

    # --- Trigger boss fight ---
    if score == 100 and not is_boss:
        final_boss()

    # --- Boss movement ---
    if is_boss:
        boss_movement()
    if boss_health <= 0:
        is_boss = False
        boss_health = 500

    # --- Player movement & wrapping ---
    space_craft_wallcollision()

    # --- Respawn aliens if cleared ---
    if not alien_troops:
        alien_fleet()
        speed += 2
    if speed > 6:
        speed = 6

    # --- Player controls ---
    if keyboard.d:
        space_craft.x += 5
    if keyboard.a:
        space_craft.x -= 5

# --- Run Game ---

pgzrun.go()