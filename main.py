import cv2
import imageio
import numpy as np
from tqdm import trange
from physics import Body, Space2D
from configs.solar import (
    CELESTIAL_BODIES,
    RADIUS_SCALE_FACTOR,
    TIME_SCALE_FACTOR,
    SPACE_SCALE_FACTOR,
    SCREEN_SIZE,
    VIDEO_SECONDS,
    FPS,
    N_FRAMES,
)


def initialize_bodies():
    return [
        Body(
            np.array(body_info["position"]),
            np.array(body_info["velocity"]),
            body_info["radius"],
            body_info["mass"],
            color=body_info["color"],
        )
        for body_name, body_info in CELESTIAL_BODIES.items()
    ]


def main():
    dt = VIDEO_SECONDS * TIME_SCALE_FACTOR / N_FRAMES  # Time step scaled in seconds
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # type: ignore
    video = cv2.VideoWriter("videos/solar.mp4", fourcc, FPS, (SCREEN_SIZE, SCREEN_SIZE))

    gif_frames = []  # List to store frames for GIF

    space = Space2D()
    bodies = initialize_bodies()
    for body in bodies:
        space.add_body(body)

    for _ in trange(N_FRAMES):
        frame = np.zeros((SCREEN_SIZE, SCREEN_SIZE, 3), dtype=np.uint8)

        for body in space.bodies:
            pixel_position = (
                body.position / SPACE_SCALE_FACTOR
                + np.array([SCREEN_SIZE / 2, SCREEN_SIZE / 2])
            ).astype(int)
            pixel_radius = int((np.log10(body.radius) - 5.5) * RADIUS_SCALE_FACTOR)
            cv2.circle(frame, tuple(pixel_position), pixel_radius, body.color, -1)

        video.write(frame)
        gif_frames.append(frame)  # Append the frame to the list
        space.update(dt)

    video.release()

    # Convert frames to GIF and save it
    imageio.mimsave("videos/solar.gif", gif_frames, fps=FPS)


if __name__ == "__main__":
    main()
