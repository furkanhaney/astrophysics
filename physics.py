import numpy as np
from tqdm import trange


class Body:
    def __init__(
        self,
        position: np.ndarray,
        velocity: np.ndarray,
        radius: float,
        mass: float,
        color=(0, 255, 0),
    ):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.mass = mass
        self.color = color


class Space2D:
    def __init__(self):
        self.bodies = []
        self.G = 6.67430e-11

    def gravitational_force(self, body1, body2):
        r = body2.position - body1.position
        r_mag = np.linalg.norm(r)
        r_hat = r / r_mag
        force_mag = self.G * body1.mass * body2.mass / (r_mag**2)
        return force_mag * r_hat

    def total_force(self, body):
        net_force = np.zeros(2)
        for other_body in self.bodies:
            if body != other_body:
                net_force += self.gravitational_force(body, other_body)
        return net_force

    def update(self, dt):
        for body in self.bodies:
            net_force = self.total_force(body)
            acceleration = net_force / body.mass
            body.velocity += acceleration * dt
            body.position += body.velocity * dt

    def add_body(self, body):
        self.bodies.append(body)
