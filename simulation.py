from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c

class SIMULATION:
    def __init__(self):
        # self.physicsClient = p.connect(p.DIRECT)
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # Determining forces that exist in our world.
        p.setGravity(0,0,-9.8)  # Gravity.

        # self.planeId = p.loadURDF("plane.urdf")  # Floor.
        # self.robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
        # p.loadSDF("world.sdf")             # simulate.py tells pybullet to simulate a world stored in world.sdf. Information about our world.

        # pyrosim.Prepare_To_Simulate(self.robotId)

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def RUN(self):
        for x in range (1000):
            print(x)
            time.sleep(1/240)
            p.stepSimulation()
        # pyrosim.Set_Motor_For_Joint(
        #     bodyIndex = robotId,
        #     jointName = b'Torso_BackLeg',
        #     controlMode = p.POSITION_CONTROL,
        #     targetPosition = c.targetAnglesBackLeg[x],
        #     maxForce = 50)
        # pyrosim.Set_Motor_For_Joint(
        #     bodyIndex = robotId,
        #     jointName = b'Torso_FrontLeg',
        #     controlMode = p.POSITION_CONTROL,
        #     targetPosition = c.targetAnglesFrontLeg[x],
        #     maxForce = 50)
        # c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        # c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        # print(backLegSensorValues)
        # print(frontLegSensorValues)
