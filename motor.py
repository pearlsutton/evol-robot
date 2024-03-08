import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 50)
        # pyrosim.Set_Motor_For_Joint(
        #     bodyIndex = robot,
        #     jointName = b'Torso_FrontLeg',
        #     controlMode = p.POSITION_CONTROL,
        #     targetPosition = desiredAngle,
        #     maxForce = 50)