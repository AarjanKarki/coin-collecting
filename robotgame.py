import pgzrun
from time import time
WIDTH=500
HEIGHT=500
TITLE='coincollecting'
game_over=False
velocity=5
time=0
#creating actors
coin=Actor('coin_gold')
bomb=Actor('bomb')
robot=Actor('robot_idle')
bg=Actor=('grass')

def draw():
    global time, game_over, velocity
    screen.clear()
    screen.blit(bg)
    coin.draw()
    bomb.draw()
    robot.draw()







pgzrun.go()