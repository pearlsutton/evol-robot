from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

        # physicsClient = p.connect(p.DIRECT)
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Determining forces that exist in our world.
        p.setGravity(0,0,-9.8)  # Gravity.
        self.planeId = p.loadURDF("plane.urdf")  # Floor.
        self.robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
        p.loadSDF("world.sdf")             # simulate.py tells pybullet to simulate a world stored in world.sdf. Information about our world.

        pyrosim.Prepare_To_Simulate(self.robotId)