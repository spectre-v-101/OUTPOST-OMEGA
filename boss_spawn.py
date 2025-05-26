from ursina import *
import math
import subprocess,atexit

app = Ursina()
#DirectionalLight(rotation=(45,0,0), shadows=True)
bg_mus=Audio('assets/the-glorious-army-cinematic-epic-battle-music-warhammer-inspired-155892.mp3', loop=True, autoplay=True,volume=1)
# Background: Sky from your image file
background = Entity(
    model='quad',
    texture='model/IMG_4376.jpg', 
     # Sky backdrop
    scale=300,
    double_sided=True,
    position=(0, 0, 100)  # Keep it far behind
)
spaceship = Entity(
    #model='model/uploads_files_4254779_StarShip2.obj',
    model='model/uploads_files_4248875_StarShipReady.obj',
    #model="Cube",
    #model='model/3d-model.obj',
    #model='model/uploads_files_311613_UAV+Trident.obj',
    
    texture='model/DefaultMaterial_Albedo.png',
    #texture='model/UAV Trident_military_albedo.tga',
    #texture='model/fmx1.png',
    #color=color.azure,
   # scale=4,
    scale=0.15,
    position=(0, 0,-10),          # Start at origin
    rotation=(0,0,0),          # Face forward +Z
    collider='box',
    double_sided=False

    
)
#spaceship.exhaust_pulse()=0
spaceship.collider_scale=Vec3(0.0000001,0.0000001,0.0000001)

planet_model=Entity(
    model='model/earth.obj',   # or .glb
    #texture='model/Earth_Col_6K.png',
    texture='model/moon_preview_7.jpg',  # optional
    #texture='model/IMG_4376.jpg',
    scale=20 ,                        # adjust scale to fill background
    position=(0, -10, 95),
   # rotation=(-20,10,15) ,      
   #      # position behind camera
    rotation=(-10,0,15) ,           # position behind camera
    
    double_sided=True                 # render both sides
)
asteroid1=Entity(
    model='sphere',   # or .glb
    #texture='model/Asteroid2c_Color_1K.png', 
    texture='model/Nar Shaddaa (Diffuse 4k).png', # optional
    scale=4,                         # adjust scale to fill background
    position=(10, 1, 55),
    #rotation=(180,20,0),                       # position behind camera
    double_sided=True                 # render both sides
)
asteroid2=Entity(
    model='sphere',   # or .glb
    texture='model/Asteroid2c_Color_1K.png',  # optional
    scale=2,                         # adjust scale to fill background
    position=(12, 4.5, 55),
    #rotation=(180,20,0),                       # position behind camera
    double_sided=True                 # render both sides
)
asteroid3=Entity(
    model='sphere',   # or .glb
    texture='model/Asteroid2c_Color_1K.png',  # optional
    scale=1,                         # adjust scale to fill background
    position=(14, -3, 55),
    #rotation=(180,20,0),                       # position behind camera
    double_sided=True                 # render both sides
)

decal2 = Entity(
   # model='model/obj.obj',
  
   # model='model/uploads_files_4254779_StarShip2.obj',
    model='model/uploads_files_4248875_StarShipReady.obj',
    parent=spaceship,
    #texture='model/Spaceship_nmap_2_Tris.jpg',  # or your transparent decal image
    #texture='model/Material.001_Emissive_blue.jpg',
    texture='model/DefaultMaterial_Metallic.png',
    
    scale=0.99,
    position=(0,0,0),  # The position you want the decal
    rotation=(0,0,0),
    #billboard=True,  # Optional: always face the camera
    #color=color.blue,
    double_sided=True
)
decal3 = Entity(
   # model='model/obj.obj',
  
   # model='model/uploads_files_4254779_StarShip2.obj',
    model='model/uploads_files_4248875_StarShipReady.obj',
    parent=spaceship,
    #texture='model/Spaceship_nmap_2_Tris.jpg',  # or your transparent decal image
    #texture='model/Material.001_Emissive_blue.jpg',
    texture='model/DefaultMaterial_Emissive.png',
    
    scale=0.99,
    position=(0,0,-0.1),  # The position you want the decal
    rotation=(0,0,0),
    #billboard=True,  # Optional: always face the camera
    #color=color.blue,
    double_sided=True,
    alpha=0.7
)
# Boss model (use your actual model file if available)
boss = Entity(
    model='model/uploads_files_4104447_+ufo+.obj',
    texture='model/fmx1.jpg',
   # color=color.black33,
    scale=1.5,
    position=(20, 100, 50),   # Starts far in Z
    enabled=False
)

# Emissive decal for glow effect
boss_glow = Entity(
    #model='model/uploads_files_4248875_StarShipReady.obj',
    #texture='model/DefaultMaterial_Emissive.png',
    scale=0.61,
    position=(0, 0, 0),
    parent=boss,
    double_sided=True,
    color=color.white,
    alpha=0.7
)

# White flash for hyperdrive warp effect
flash = Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=2,
    alpha=0,
    z=-1
)

# Camera setup
camera.fov = 90
camera.position = (0, 3, -2)
t = 0
bg_music = Audio('assets/time-travel-83472.mp3', loop=False, autoplay=False,volume=1.5)
def play_hyperdrive_cutscene():
    # White flash to simulate hyper entry
    def warp_flash():
        flash.alpha = 1
        flash.fade_out(duration=0.3)

    # Boss appears and warps forward
    def spawn_boss():
        boss.enabled = True
        boss.animate_position((0, 2, 5), duration=1.5, curve=curve.out_expo)

    invoke(warp_flash, delay=1.0)
    invoke(spawn_boss, delay=1.2)
    invoke(bg_music.play,delay=1.2)
def run_next_file():
    #invoke(fade_to_black, delay= 4)
   
    subprocess.Popen(['python', 'Boss_fight.py']) 
    application.quit() # or ['python3', 'tes1.py'] depending on OS




    
def float_boss():
    boss.y = 2+math.sin(time.time() * 2) * 0.3
    spaceship.y=math.sin(time.time() * 2) * 0.3
    #camera.animate('fov', 120, duration=3)
    if camera.z > -17.3:
        camera.z -= time.dt * 1.8
    else:
        invoke(run_next_file,delay=10)
    
        
play_hyperdrive_cutscene()
#atexit.register(run_next_file)
boss.update = float_boss



# Floating effect for boss ship after arrival
  # Smooth float motion
#update()

app.run()
