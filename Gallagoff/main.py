import pgzrun

TITLE= 'Welcome to Gallagoff'
WIDTH= 750
HEIGHT= 750

game_over = False
score = 0
enemy = []
bullets = []
ship = Actor('ship')

ship.x=375
ship.y=650
for x in range(5):
    for y in range(5):
        bug = Actor('bug')
        bug.x = 100+ x*100
        bug.y = 100+ y*50
        enemy.append(bug)


def draw():
    global bullets, ship
    screen.fill('Black')
    ship.draw()
    for b in bullets:
        b.draw()

    for e in enemy:
        e.draw()



def update():
    if keyboard.left and ship.x > 0:
        ship.x= ship.x-7.5
    if keyboard.right and ship.x < 750:
        ship.x= ship.x+7.5
    for b in bullets:
        b.y= b.y-15
    for e in enemy:
        e.y= e.y+0.5

def on_key_down(key):
    global bullets, ship
    if key == keys.SPACE:
        bullet = Actor('bullet')
        bullet.x = ship.x
        bullet.y = ship.y
        bullets.append(bullet)
    




pgzrun.go()