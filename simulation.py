from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data

class SIMULATION:
    def __init__(self):
        # self.physicsClient = p.connect(p.DIRECT)
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)  # Gravity.

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def RUN(self):
        for t in range (1000):
            # print(t)
            time.sleep(1/90000)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)