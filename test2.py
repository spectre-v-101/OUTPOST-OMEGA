from ursina import *
import os
import sys
import subprocess

app = Ursina()
bg_music = Audio('assets/cinematic-space-drone-10623.mp3', loop=True, autoplay=True,volume=1.5)
# Background
background = Entity(model='quad', texture='model/IMG_4376.jpg', scale=25, z=10)
bg=Entity(model='sphere',texture='model/Nar Shaddaa (Diffuse 4k).png',scale=2,position=(0,-1,9))
from math import sin
camera.fov=90
camera.position=(0,0,0)
def update():
    camera.y = 2 + sin(time.time() * 0.8) * 0.3  # Smooth floating effect
    camera.rotation_x = sin(time.time() * 0.5) * 2
    camera.x= 2+ cos(time.time() * 0.8) * 0.3  # Slight tilt for cinematic feel

# Title
title = Entity(
    #text='OUTPOST OMEGA',
    model='quad',
    texture='model/text-1748111766078.png',
    #origin=(0, 0,2),
    scale=(6,1,1),
    position=(2,4,5)
    #position=camera.position+Vec3(0,0,3)
    #color=color.white,
    #y=0.3,
    #shadow=True
)

# Button actions
def start_game():
    #os.system(f'{sys.executable} prog1.py') 
    subprocess.Popen(['python', 'prog1.py']) # Launch intro
    application.quit()  # Close the menu

def quit_game():
    application.quit()

# Buttons
play_button = Button(
    text='PLAY',
    scale=(0.6, 0.1),
    y=0,
    text_color=color.violet,
    on_click=start_game
)

quit_button = Button(
    text='EXIT',
    scale=(0.6, 0.1),
    y=-0.15,
    text_color=color.red,
    on_click=quit_game
)
#update()
app.run()
