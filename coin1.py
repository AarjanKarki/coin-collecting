import pgzrun
from time import time
from random import randint
WIDTH=500
HEIGHT=500
TITLE='coincollecting'
game_over=False
velocity=5
timer=0
#creating actors
coin=Actor('coin_gold')
bomb=Actor('bomb')
robot=Actor('robot_idle')
bg=Actor('grass')

def start():
    global game_over, timer, velocity
    game_over=False
    velocity=5
    timer=0
#set initial positions
    robot.pos=WIDTH//2, HEIGHT//2
    move_bomb()
    move_coin()

def move_coin():
    coin.x=randint(20,WIDTH-20)
    coin.y=randint(20,HEIGHT-20)
    while coin.colliderect(bomb) or coin.colliderect(robot):
        coin.x=randint(20,WIDTH-20)
        coin.y=randint(20,HEIGHT-20) 
def move_bomb():
    bomb.x=randint(20,WIDTH-20)
    bomb.y=randint(20,HEIGHT-20)
    while bomb.colliderect(coin) or bomb.colliderect(robot):
        bomb.x=randint(20,WIDTH-20)
        bomb.y=randint(20,HEIGHT-20) 


def draw():
    global time, game_over, velocity
    screen.clear()
    bg.draw()
    coin.draw()
    bomb.draw()
    robot.draw()

def update():
    #while left arrow key pressed
    if keyboard.LEFT and robot.left>0:
    #show left facing image
        robot.image='robot_left'
        robot.x=robot.x-velocity
    elif keyboard.RIGHT and robot.right<WIDTH:
        robot.image='robot_right'
        robot.x+=velocity
    if keyboard.UP and robot.top>0:
    #show right facing image
        robot.image='robot_left'
        robot.y=robot.y-velocity
    elif keyboard.DOWN and robot.bottom<HEIGHT:
        robot.image='robot_right'
        robot.y=robot.y+velocity
    if robot.colliderect(coin):
        sounds.find_money.play()
        move_coin()
    if robot.colliderect(bomb):
        sounds.find_money.play()
        move_bomb()

def on_key_up(key):
    if key==keys.LEFT or keys==keys.RIGHT:
        robot.image='robot_idle'










start()
pgzrun.go()