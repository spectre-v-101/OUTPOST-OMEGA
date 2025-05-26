from ursina import *
import random

app = Ursina()
import subprocess
# Sky background
Entity(model='quad', texture='model/IMG_4376.jpg', scale=300, double_sided=True, position=(0, -10, 100))

# Boss ship
boss_ship = Entity(
    model='model/uploads_files_4104447_+ufo+.obj',
    texture='model/fmx1.jpg',
    scale=0.8,
    position=(0, 0, 10),
)

camera.position = (0, 2, -2)
camera.fov = 90

exploded_parts = []
explosion_sound = Audio('assets/large-underwater-explosion-190270.mp3', autoplay=False)
bg=Audio('assets/victory-shall-reign-inspirationaltriumphant-cue-283320.mp3',autoplay=False)  # show victory text

parts_spawned = False
victory_text = Text(
    text='VICTORY',
    scale=4,
    color=color.cyan,
    enabled=False,
    origin=(0,0),
    background=True,
    background_color=color.black33
)

def boss_disintegration_cutscene():
    invoke(explosion_sound.play, delay=0.8)

    # Flash effect
    flash = Entity(model='quad', parent=camera.ui, color=color.white, scale=2)
    flash.fade_out(duration=1)
    destroy(flash, delay=1)

    # Shake effect
    def shake():
        camera.position += Vec3(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), 0)
    for i in range(10):
        invoke(shake, delay=0.05 * i)

    # Hide the original boss ship
    invoke(boss_ship.disable, delay=1)

    # Spawn parts
    invoke(spawn_exploding_parts, delay=1)

def spawn_exploding_parts():
    global parts_spawned
    parts_spawned = True

    for _ in range(1000):
        part = Entity(
            model='cube',
            color=color.white.tint(-0.2),
            scale=Vec3(0.2),
            position=boss_ship.position + Vec3(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)),
            rotation=Vec3(random.uniform(0,360), random.uniform(0,360), random.uniform(0,360))
        )
        part.velocity = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)) * 4
        part.rotation_speed = Vec3(random.uniform(-200, 200), random.uniform(-200, 200), random.uniform(-200, 200))
        exploded_parts.append(part)
k=0
def update():
    global k
    if parts_spawned:
        for part in exploded_parts[:]:  # iterate over a copy because we'll remove parts
            part.position += part.velocity * time.dt
            part.rotation += part.rotation_speed * time.dt
            part.scale *= 0.95
            k+=1
            if part.scale.x < 0.01:
                destroy(part)
                exploded_parts.remove(part)

        if len(exploded_parts) == 0 and k!=0:
            #victory_text.enabled = True
            #bg.play()
            
            subprocess.Popen(['python', 'credits.py']) 
            application.quit()
            #bg=Audio('assets/victory-shall-reign-inspirationaltriumphant-cue-283320.mp3',autoplay=True)  # show victory text

# Start cutscene
boss_disintegration_cutscene()

app.run()
