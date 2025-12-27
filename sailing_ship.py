import pgzrun

WIDTH,HEIGHT= 600,600

ship= Actor("pirate_ship")
ship.pos=(20,100)
ship.angle=20
def draw():
    screen.blit("sea",(0,0))
    ship.draw()
def ship_down():
    animate(ship, y= 150,angle= ship.angle + 40, duration= 1, on_finished=ship_up)
def ship_up():
    animate(ship, y = 80, angle= ship.angle -40  ,duration= 1, on_finished=ship_down)
ship_up()

def update():
    ship.x += 1
    if ship.x > 600:
        ship.x = 20

pgzrun.go()