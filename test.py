from ursina import *
from ursina.audio import Audio
import random,subprocess

app = Ursina()
#def start_gameplay():
#bg_music = Audio('assets/z-battle-227609.mp3', loop=True, autoplay=True)
bg_music = Audio('assets/the-glorious-army-cinematic-epic-battle-music-warhammer-inspired-155892.mp3', loop=True, autoplay=True,volume=1.5)
shoot_sound = Audio('assets/attack-laser-128280.wav', autoplay=False)
explosion_sound = Audio('assets/explosion-307469.wav', autoplay=False,volume=1)
window.color = color.black
enemy_shoot_sound=Audio('assets/boomerang-128276.wav', autoplay=False,volume=0.25)
# Starfield background

#DirectionalLight(rotation=(0,0,0), shadows=True)




# Spaceship entity

 # soft warm yellow

# Optional: add some ambient light with a softer yellow tint

#directional_light = DirectionalLight()
#directional_light.color = color.rgb(20, 40, 100) 
#ddddadirectional_light.color = color.rgb(255, 230, 150) 
#directional_light.color = color.rgb(500, 500, 500)
#DirectionalLight(y=2, z=3, shadows=True)
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
    scale=0.35,
    position=(0, 0,0),          # Start at origin
    rotation=(0,0,0),          # Face forward +Z
    collider='box',
    double_sided=False

    
)
#spaceship.exhaust_pulse()=0
spaceship.collider_scale=Vec3(0.0000001,0.0000001,0.0000001)
decal = Entity(
   # model='model/obj.obj',
  
   # model='model/uploads_files_4254779_StarShip2.obj',
    #model='model/uploads_files_4248875_StarShipReady.obj',
    parent=spaceship,
    #texture='model/Spaceship_nmap_2_Tris.jpg',  # or your transparent decal image
    #texture='model/Material.001_Emissive_blue.jpg',
    #texture='model/DefaultMaterial_Roughness.png',
    
    scale=0.9968,
    position=(0,0,0),  # The position you want the decal
    rotation=(0,0,0),
    #billboard=True,  # Optional: always face the camera
    #color=color.blue,
    double_sided=True
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
glow_pulse_time = 0
background_model = Entity(
    model='quad',
       # or .glb
    #model='',
    #texture='model/moon_preview_7.jpg',  # optional
    texture='model/IMG_4376.jpg',
    #texture='model/outer-space-background.jpg',
    scale=190 , 
    #scale=50   ,                    # adjust scale to fill background
    position=(0, -30,150),            # position behind camera
    double_sided=True                 # render both sides
)
bg2= Entity(
    #model='quad',
       # or .glb
    #model='',
    #texture='model/moon_preview_7.jpg',  # optional
    #texture='model/IMG_4376.jpg',
    #texture='model/outer-space-background.jpg',
    scale=100 , 
    #scale=50   ,                    # adjust scale to fill background
    position=(50, -10,150),            # position behind camera
    double_sided=True                 # render both sides
)
bg3= Entity(
    #model='quad',
       # or .glb
    #model='',
    #texture='model/moon_preview_7.jpg',  # optional
    #texture='model/IMG_4376.jpg',
    #texture='model/outer-space-background.jpg',
    scale=100 , 
    #scale=50   ,                    # adjust scale to fill background
    position=(-50, -80,140),            # position behind camera
    double_sided=True                 # render both sides
)
bg4= Entity(
    #model='quad',
       # or .glb
    #model='',
    #texture='model/moon_preview_7.jpg',  # optional
    #texture='model/IMG_4376.jpg',
    #texture='model/outer-space-background.jpg',
    scale=100 , 
    #scale=50   ,                    # adjust scale to fill background
    position=(50, -80,140),            # position behind camera
    double_sided=True                 # render both sides
)
#Sky(texture='model/outer-space-background.jpg',scale=10000)
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
background_model_2=Entity(
    model='model/spaceship.obj',   # or .glb
    texture='model/Spaceship_color_4.jpg',  # optional
    scale=1,                         # adjust scale to fill background
    position=(-10, 1, 55),
    rotation=(180,20,0),                       # position behind camera
    double_sided=True  ,
   # collider='box'               # render both sides
)
bg_decal=Entity(
    model='model/spaceship.obj',
    texture='model/Intergalactic Spaceship_emi.jpg',
  
   # model='model/uploads_files_4254779_StarShip2.obj',
    #model='model/uploads_files_4248875_StarShipReady.obj',
    parent=background_model_2,
    #texture='model/Spaceship_nmap_2_Tris.jpg',  # or your transparent decal image
    #texture='model/Material.001_Emissive_blue.jpg',
    #texture='model/DefaultMaterial_Metallic.png',
    
    scale=1.001,
    position=(0,0,0),  # The position you want the decal
    rotation=(0,0,0),
    #billboard=True,  # Optional: always face the camera
    #color=color.blue,
    double_sided=True
)
bg_decal3=Entity(
    model='sphere',
    #texture='model/Intergalactic Spaceship_emi.jpg',
  
   # model='model/uploads_files_4254779_StarShip2.obj',
    #model='model/uploads_files_4248875_StarShipReady.obj',
    parent=background_model_2,
    #texture='model/Spaceship_nmap_2_Tris.jpg',  # or your transparent decal image
    #texture='model/Material.001_Emissive_blue.jpg',
    #texture='model/DefaultMaterial_Metallic.png',
    color=color.red,
    scale=0.2,
    position=(0,0,3),  # The position you want the decal
    rotation=(0,0,0),
    #billboard=True,  # Optional: always face the camera
    #color=color.blue,
    double_sided=True
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

# Initial camera position behind spaceship (negative Z), slightly above Y
camera.position = spaceship.position + Vec3(0, 5, -20)
camera.look_at(spaceship.position)

class Obstacle(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            #model='model/Spaceship.obj',
            model='model/uploads_files_4254779_StarShip2.obj',
            #texture="model/Spaceship_color_4.jpg",
            #model="Cube",
            texture='model/Material.001_Base_red.jpg',
            #color=color.red,
            scale=(0.12,0.12,0.12),
            rotation=(0,180,0),
            collider='box',
            **kwargs
        )
        self.collider_scale = Vec3(0.0000001, 0.0000001, 0.0000001)
        
        # Add a visual decal (e.g., bullet mark or scorch)
        self.decal = Entity(
            parent=self,
            #model='quad',
            model='model/uploads_files_4254779_StarShip2.obj',
            texture='model/Material.001_Emissive.jpg',
            #texture='assets/decal_bullet_hole.png',  # <- make sure this image exists
            scale=0.997,
            #position=Vec3(0, 0, 0),  # Slightly in front of the ship
            #rotation_x=90,
            #billboard=True,  # Makes it always face the camera
            color=color.white,
        )

        

obstacles = []

def spawn_obstacle():
    x = random.uniform(-8, 8)
    y = random.uniform(-4, 4)
    z = spaceship.z + 50
    obstacle = Obstacle(position=(x, y, z))
    obstacles.append(obstacle)

for _ in range(10):
    spawn_obstacle()

#
bullets = []
print("hellow", spaceship.forward)
speed = 15
score=0
# HUD elements
score_text = Text(text='Score: 0', position=(-0.78, 0.35), scale=1.5, color=color.white, parent=camera.ui)
health_bar = Entity(model='quad', color=color.green, scale=(0.4, 0.03), position=(-0.58, -0.44), parent=camera.ui)
Health_text=Text(text='Health:', position=(-0.78, -0.38), scale=1.5, color=color.white, parent=camera.ui)
ammo_text = Text(text='Ammo: ∞', color=color.violet,position=(0.7, -0.45), origin=(0, 0), scale=1.5)
crosshair = Entity(model='quad', color=color.white, scale=(0.01, 0.01), parent=camera.ui)
# Horizontal line
crosshair_h = Entity(
    parent=camera.ui,
    model='quad',
    color=color.green,
    scale=(0.03, 0.005),  # width, height
    position=(0, 0)
)

# Vertical line
crosshair_v = Entity(
    parent=camera.ui,
    model='quad',
    color=color.green,
    scale=(0.005, 0.03),
    position=(0, 0)
)
def perform_roll():
    target = Vec3(spaceship.rotation_x, spaceship.rotation_y, spaceship.rotation_z + 360)
    
    spaceship.animate('rotation', target, duration=1, curve=curve.linear)
    decal.animate( 'rotation', target, duration=1, curve=curve.linear)
def input(key):
    if key == 'z':
        perform_roll()
    if key == 'space':
        fire_bullet()
    

        

cylinder = Cylinder(radius=0.15, height=5, direction=(0,0,1) )
cylinder2=Cylinder(radius=0.15, height=5, direction=(0,0,1) )
def fire_bullet():
    shoot_sound.play()
    bullet = Entity(
        model=cylinder,
        color=color.green,
        scale=0.3,
        position=spaceship.position + Vec3(0.5 , 0, 2),
        collider='box'
    )
    bullets.append(bullet)
    bullet2=Entity(
        model=cylinder2,
        color=color.green ,
        scale=0.3,
        position=spaceship.position + Vec3(-0.5, 0, 2),
       collider='box'

    )
    bullets.append(bullet2)
enemies=  []
enemy_bullets = []
cylinder3 = Cylinder(radius=0.15, height=2, direction=(0,0,-1) )
def enemy_shoot(enemy):
    enemy_shoot_sound.play()
    bullet = Entity(
        model='Sphere',
        color=color.red,
        scale=(0.1,0.1,1.2),
        position=enemy.position + Vec3(0, 0, -1),  # towards player
        collider='box'
    )
    bullet.direction = Vec3(0, 0, -1)  # enemy shoots backward (toward player)
    enemy_bullets.append(bullet)

def create_explosion(position):
    for _ in range(20):  # Number of particles
        p = Entity(
            model='sphere',
            color=color.orange,
            scale=0.2,
            position=position,
            add_to_scene_entities=False
        )
        # Assign random direction and speed
        p.velocity = Vec3(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)) * 4

        def update_particle(p=p):
            p.position += p.velocity * time.dt
            p.scale *= 0.9  # Shrink
            p.color = color.rgba(p.color.r, p.color.g, p.color.b, p.color.a - time.dt * 2)
            if p.scale.x < 0.05:
                destroy(p)

        p.update = update_particle
        p.enabled = True
        scene.entities.append(p)
player_health = 10000  # out of 100
def update_health_bar():
    # Scale based on current health
    health_bar.scale_x = 0.4 * (player_health / 10000)
    
    # Change color dynamically
    if player_health > 60/100*10000:
        health_bar.color = color.green
    elif player_health > 30/100*10000:
        health_bar.color = color.orange
    else:
        health_bar.color = color.red
from ursina.prefabs.ursfx import ursfx

def spawn_engine_flame():
    p1 = Entity(
        model='sphere',
        scale=0.05,
        color=color.cyan,
        position=decal3.world_position+Vec3(-0.3,0,-2),
        add_y=random.uniform(-0.01, 0.01),
        add_x=random.uniform(-0.01, 0.01),
        alpha=0.6
    )
    p2=Entity(
        model='sphere',
        scale=0.05,
        color=color.cyan,
        position=decal3.world_position+Vec3(0.3,0,-2),
        add_y=random.uniform(-0.01, 0.01),
        add_x=random.uniform(-0.01, 0.01),
        alpha=0.6
    )
    p1.animate_position(p1.position + Vec3(0, -0.1, -0.2), duration=0.05, curve=curve.linear)
    p1.fade_out(duration=0.05)
    destroy(p1, delay=0.4)
    p2.animate_position(p2.position + Vec3(0, -0.1, -0.2), duration=0.05, curve=curve.linear)
    p2.fade_out(duration=0.05)
    destroy(p2, delay=0.4)
#obstacles.append(background_model_2)
objective_goal = 50
enemies_destroyed = 0
objective_text = Text(text='OBJECTIVE: Destroy 50 Enemy Ships', position=(-0.78, 0.48), scale=1.3, color=color.cyan, parent=camera.ui)
def run_next_file():
    #invoke(fade_to_black, delay= 4)
    
    subprocess.Popen(['python', 'boss_spawn.py']) 
    application.quit()
def update():
    global speed,score,player_health,enemies_destroyed,objective_goal
    global score
    spawn_engine_flame()
    # Sample game logic: increase score over time
    #background_model.rotation_y += time.dt * 2
    speed+=time.dt*0.5
    score += time.dt * 10
    score_text.text = f'Score: {int(score)}'
    global glow_pulse_time
    glow_pulse_time += time.dt * 5
    #decal3.alpha = 0.5 + 0.4 * math.sin(glow_pulse_time)
    # Move spaceship left/right with A/D or arrow keys
    if held_keys['a'] or held_keys['left arrow']:
        spaceship.x -= time.dt * 10
        #decal.x-=time.dt * 10
    if held_keys['d'] or held_keys['right arrow']:
        spaceship.x += time.dt * 10
        #decal.x+=time.dt * 10
    # Move spaceship up/down with W/S
    if held_keys['w']:
        spaceship.y += time.dt * 10
        #decal.y+=time.dt * 10
    if held_keys['s']:
        spaceship.y -= time.dt * 10
        #decal.y-=time.dt * 10
    if held_keys['f']:
        spaceship.z+=time.dt*10

    # Limit movement range (adjust limits as needed)
    spaceship.x = clamp(spaceship.x, -10, 10)
    #decal.x=clamp(decal.x, -5, 5)
    spaceship.y = clamp(spaceship.y, -5, 5) 
     # added y limits so ship doesn't fly off
    #decal.y=clamp(decal.y, -5, 5)
    # Initialize roll attribute if it doesn't exist
    if not hasattr(spaceship, 'current_roll'):
        spaceship.current_roll = 0
        decal.current_roll=0

    max_roll_angle = 20  # max roll degrees

    # Determine target roll based on horizontal input
    if held_keys['a'] or held_keys['left arrow']:
        target_roll = -max_roll_angle
    elif held_keys['d'] or held_keys['right arrow']:
        target_roll = max_roll_angle
    else:
        target_roll = 0

    # Smoothly interpolate current roll toward target_roll
    spaceship.current_roll = lerp(spaceship.current_roll, target_roll, 5 * time.dt)
    #decal.current_roll=lerp(decal.current_roll, target_roll, 5 * time.dt)
    # Apply roll (rotation around Z axis)
    # Keep original pitch (x) and yaw (y), just update roll (z)
    spaceship.rotation = (spaceship.rotation.x, spaceship.rotation.y, spaceship.current_roll)
   # decal.rotation=(decal.rotation.x, decal.rotation.y, decal.current_roll)
    # Move obstacles towards spaceship
        # Bullet movement and collision
    for obstacle in obstacles:
        obstacle.z -= time.dt * 15#speed
        if obstacle.z < spaceship.z - 5:
            destroy(obstacle)
            obstacles.remove(obstacle)
            spawn_obstacle()
    for enemy in obstacles:
        if random.random() < 0.05:  # 1% chance per frame
             enemy_shoot(enemy)
             
    for e_bullet in enemy_bullets[:]:
        e_bullet.position += e_bullet.direction * time.dt * 50

        if e_bullet.z < spaceship.z - 5:
           destroy(e_bullet)
           enemy_bullets.remove(e_bullet)
           continue

        if e_bullet.intersects(spaceship).hit:
            explosion_sound.play()
            create_explosion(spaceship.position)
            destroy(e_bullet)
            enemy_bullets.remove(e_bullet)
            player_health -= 5
            update_health_bar()
        # Optional: Add health or game over logic here

    for bullet in bullets[:]:
        bullet.z += time.dt * 100

        # Destroy bullet if it goes out of range
        if bullet.z > spaceship.z + 70 :
            bullets.remove(bullet)
            destroy(bullet)
            continue

        # Check collision with enemies
        for enemy in enemies[:]:
            if bullet.intersects(enemy).hit:

                destroy(enemy)
                enemies.remove(enemy)
                
                destroy(bullet)
                bullets.remove(bullet)
                break  # Exit to avoid modifying list during loop

        # Check collision with obstacles
        for obstacle in obstacles[:]:
            if bullet in bullets and bullet.intersects(obstacle).hit:
                create_explosion(obstacle.position)
                destroy(obstacle)
                obstacles.remove(obstacle)
                spawn_obstacle()  # optionally replace destroyed obstacle
                destroy(bullet)
                bullets.remove(bullet)
                
                explosion_sound.play()
                enemies_destroyed += 1
                objective_text.text = f'Enemies Destroyed: {enemies_destroyed}/{objective_goal}'
        
                if enemies_destroyed >= objective_goal:
                    objective_text.text = 'Objective Complete!'
                    #for i in range(10000000000):{}
                    run_next_file()

                    

            # You can trigger next level or message here

                break

    if player_health <= 0:
        print("Game Over")
        application.quit()
    

    # Collision detection
    for obstacle in obstacles:
        if spaceship.intersects(obstacle).hit:
            player_health -= 5
            update_health_bar()
            #print("Collision! Game Over")
           # application.quit()
    
    # Camera smoothly follows spaceship from behind and above
    sway_amount = 0.2
    sway_x = math.sin(time.time() * 5) * sway_amount * (spaceship.x / 5)
    sway_y = math.cos(time.time() * 4) * sway_amount * (spaceship.y / 3)

    desired_cam_pos = spaceship.position + Vec3(sway_x, 5 + sway_y, -20)

    # Smoothly move camera
    camera.position = lerp(camera.position, desired_cam_pos, 4 * time.dt)

    # Tilt camera based on horizontal ship movement
    tilt_angle = clamp(-spaceship.x * 5, -15, 15)
    camera.rotation = (tilt_angle, 180, 0)

    # Keep camera looking at the ship
    camera.look_at(spaceship.position)

    
app.run()
