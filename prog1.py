from ursina import *
import os
import subprocess
import atexit


app = Ursina()

# Load Space Background
Entity(model='quad', texture='model/IMG_4376.jpg', scale=390, double_sided=True, position=(0, -10, 100))
bg=Entity(model='sphere',texture='model/Nar Shaddaa (Diffuse 4k).png',scale=2,position=(0,-1,-50))

# Load Player Ship
player_ship = Entity(
    model='model/uploads_files_4248875_StarShipReady.obj',
    texture='model/DefaultMaterial_Albedo.png',
    scale=(0.6, 0.6, 0.6),
    position=(0, 0, 40),
    rotation=(0,180,0)
)
decal_ship = Entity(
    model='model/uploads_files_4248875_StarShipReady.obj',
    texture='model/DefaultMaterial_Emissive.png',
    scale=(0.99, 0.99, 0.99),
    position=(0, 0, 0.03),
    parent=player_ship,
   # alpha=0.5
)

# Lighting
DirectionalLight(rotation=(45, -20, 20), shadows=True)

# Camera Setup
camera.fov = 90
camera.position = (0, 2, 30)

# Background Music
cutscene_music = Audio('assets/ambient-soundscapes-007-space-atmosphere-304974.mp3', loop=False, autoplay=True)

# Cutscene Zoom Effect
def update():
    if camera.z > -95:
        camera.z -= time.dt * 1.8

def play_prologue_cutscene():
    fade = Entity(parent=camera.ui, model='quad', color=color.black, scale=2)
    fade.fade_out(duration=2)

    invoke(player_ship.animate_position, (0, 0, 5), duration=7, delay=2)
    invoke(show_story_text_line_by_line, delay=4)

def show_story_text_line_by_line():
    story_lines = [
        "Year 2472...",
        "The stars once promised hope.",
        "Now, they carry death.",
        "",
        "Three solar cycles ago, we intercepted a signal from beyond the Kuiper Belt.",
        "A whisper of something ancient... and hostile.",
        "",
        "Outposts fell silent. No distress calls. No survivors.",
        "Just static.",
        "",
        "Now, only Outpost Omega remains.",
        "Humanity’s final bastion... and its last line of defense.",
        "",
        "You are Commander Riven.",
        "This isn't a recon mission.",
        "This is our last stand."
    ]

    y_position = 0.4
    delay = 0
    for line in story_lines:
        invoke(Func(display_single_line, line, y_position), delay=delay)
        delay += 4

    # Glitch text and then launch game
    invoke(Func(show_glitch_text, "Signal Lost..."), delay=delay + 2)
    
    invoke(application.quit, delay=delay + 5) 
    #invoke(launch_gameplay, delay=delay + 5)

def display_single_line(text, y):
    line = Text(text=text, origin=(0, 0), scale=1.3, y=y, background=True)
    invoke(line.fade_out, duration=2, delay=2)
    invoke(line.disable, delay=4)

def show_glitch_text(text):
    glitch = Text(text=text, origin=(0, 0), scale=2, color=color.red, background=True)
    glitch.animate_color(color.black, duration=0.6)
    invoke(glitch.disable, delay=2)


def fade_to_black():
    black = Entity(parent=camera.ui, model='quad', color=color.clear, scale=2)
    black.animate_color(color.black, duration=1.5)


def run_next_file():
    invoke(fade_to_black, delay= 4)
    subprocess.Popen(['python', 'test.py'])  # or ['python3', 'tes1.py'] depending on OS

atexit.register(run_next_file)


play_prologue_cutscene()
app.run()
