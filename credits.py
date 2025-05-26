from ursina import *

app = Ursina()

# Background (same as boss scene)
Entity(model='quad', texture='model/IMG_4376.jpg', scale=100, double_sided=True, position=(0, -10, 100))

# Optional: Fade-in black overlay for cinematic feel
fade_overlay = Entity(parent=camera.ui, model='quad', color=color.black, scale=2)
fade_overlay.fade_out(duration=2)

# Epic background music
music = Audio('assets/victory-shall-reign-inspirationaltriumphant-cue-283320.mp3', autoplay=True, loop=False)

# Cinematic credits text
credits = Text(
    text="""
    ✨ THANK YOU FOR PLAYING ✨

    OUTPOST OMEGA by Ved
      a solo dev project

    ▸ Design & Development: Ved
    ▸ Sound & Music: Freesound, Open License
    ▸ Engine: Ursina & Python

    🌌 May your journeys among the stars continue...

    --- THE END ---
    """,
    origin=(0, 0),
    scale=2,
    line_height=2,
    color=color.cyan,
    background=True,
    background_color=color.rgba(0, 0, 0, 150),
)

credits.y = -1.3  # Start off-screen

def update():
    credits.y += time.dt * 0.2  # scroll speed

    # End the app when the credits scroll past the top
    if credits.y > 1.5:
        application.quit()

app.run()
