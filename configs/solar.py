CELESTIAL_BODIES = {
    "Sun": {
        "radius": 6.9634e8,
        "mass": 1.989e30,
        "charge": 0,
        "position": [0.0, 0.0],
        "velocity": [0.0, 0.0],
        "color": (0, 255, 255),
    },
    "Earth": {
        "radius": 6.371e6,
        "mass": 5.972e24,
        "charge": 0,
        "position": [1.496e11, 0.0],
        "velocity": [0.0, 2.978e4],
        "color": (255, 0, 0),
    },
    "Mercury": {
        "radius": 2.4397e6,
        "mass": 3.285e23,
        "charge": 0,
        "position": [57.9e9, 0.0],
        "velocity": [0.0, 47.9e3],
        "color": (128, 128, 128),
    },
    "Venus": {
        "radius": 6.0518e6,
        "mass": 4.867e24,
        "charge": 0,
        "position": [108.2e9, 0.0],
        "velocity": [0.0, 35.0e3],
        "color": (255, 192, 203),
    },
    "Mars": {
        "radius": 3.3895e6,
        "mass": 6.4171e23,
        "charge": 0,
        "position": [227.9e9, 0.0],
        "velocity": [0.0, 24.1e3],
        "color": (0, 0, 255),
    },
}

# Display Constants
RADIUS_SCALE_FACTOR = 20
TIME_SCALE_FACTOR = 1e6
SPACE_SCALE_FACTOR = 3e8
SCREEN_SIZE = 2048
VIDEO_SECONDS = 3
FPS = 30
N_FRAMES = VIDEO_SECONDS * FPS
