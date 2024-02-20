import pybullet as p

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")       # Floor.
        p.loadSDF("world.sdf")                        # Tells pybullet to simulate a world stored in world.sdf. Information about our world.
