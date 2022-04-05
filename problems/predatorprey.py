import numpy as np


class Jellyfish:
    power = 10.0
    turn_lerp = .5
    friction = .9

    def __init__(self, pos, vel, dir, rs, an, resp) -> None:
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.heading = dir
        self.radii = rs
        self.angles = an
        self.responses = resp
        n = rs.shape[0]
        self.bins = np.r_[0:n]**2  # self.radii.size

    # Flee returns a generator object we want to be able to run indefinitely
    def flee(self, turtle, timestep: float):
        while True:
            # compute a response
            dirs = self.angles + self.heading
            dists = turtle.pos[0] * np.cos(dirs) + turtle.pos[1] * np.sin(dirs)
            bin_code = dists < self.radii
            number = np.sum(self.bins * bin_code)
            resp = self.responses[number]
            # correctly turn toward target angle
            cooldown = np.linalg.norm(resp[0:2])/Jellyfish.power
            self.vel += resp[0:2]
            self.move(resp[2], timestep)
            while cooldown > 0:
                yield
                self.move(resp[2], timestep)
                cooldown -= timestep

    def move(self, timestep):
        # Apply friction and move
        self.vel *= (Jellyfish.friction ** timestep)
        self.pos += self.vel * timestep
        # Snap safety
        if self.vel[0]*self.vel[0] + self.vel[1]*self.vel[1] < 1e-16:
            return
        # Rotate toward the direction of movement
        gap = np.arctan2(self.vel[0], self.vel[1]) - self.heading
        if gap >= np.pi:
            gap -= 2*np.pi
        elif gap <= -np.pi:
            gap += 2*np.pi
        self.heading += Jellyfish.turn_lerp * timestep * gap
        if self.heading >= 2*np.pi:
            self.heading -= 2*np.pi

    def draw(self, app):
        app.pushMatrix()
        app.translate(self.pos[0], self.pos[1])
        app.rotate(self.heading)
        app.noStroke()
        app.fill(0, 0, 255)
        app.rect(0, 0, 45, 30)
        app.fill(0, 128, 255)
        # x direction will be direction of travel
        app.rect(10, 0, 10, 10)
        app.popMatrix()


class Turtle:
    maxvel = 4

    def __init__(self, pos, vel, params: list) -> None:
        self.pos = pos
        self.vel = vel
        self.accum = 0
        self.deriv = 0
        [self.prop, self.integ, self.deriv] = params

    def pursue(self, jelly: Jellyfish, timestep: float):
        while True:
            yield 0

    def draw(self, app):
        app.pushMatrix()
        app.translate(self.pos[0], self.pos[1])
        app.rotate(self.heading)
        app.stroke(0, 0, 255)
        app.ellipse(0, 0, 30, 45)
        app.popMatrix()


# See how long the jellyfish survives the turtle
def duel(turtle, jellyfish, timestep, max_time, referee,
         situate=None, display=None):
    if situate is not None:
        situate(jellyfish, turtle)
    score = -1
    flight = jellyfish.flee(turtle, timestep)
    pursuit = turtle.pursue(jellyfish, timestep)
    caught = False
    while not caught and score < max_time:
        flight.next()
        pursuit.next()
        if display is not None:
            display(jellyfish, turtle)
        caught = referee(turtle, jellyfish)
        score += 1
    flight.close()
    pursuit.close()
    return score * timestep
