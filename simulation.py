from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c

class SIMULATION:
    def __init__(self):

        # # self.physicsClient = p.connect(p.DIRECT)
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # Determining forces that exist in our world.
        p.setGravity(0,0,-9.8)  # Gravity.

        self.world = WORLD()
        self.robot = ROBOT()

        # self.robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
        # pyrosim.Prepare_To_Simulate(self.robotId)


    def __del__(self):
        p.disconnect()

    def RUN(self):
        for t in range (1000):
            print(t)
            time.sleep(1/240)
            p.stepSimulation()
            self.robot.Sense(t);
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot,
            jointName = b'Torso_BackLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = c.targetAnglesBackLeg[t],
            maxForce = 50)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot,
            jointName = b'Torso_FrontLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = c.targetAnglesFrontLeg[t],
            maxForce = 50)
        c.backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        c.frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")