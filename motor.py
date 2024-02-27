import string
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName: string):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        self.motorValues = self.amplitude * numpy.sin(numpy.linspace(self.frequency*0 + self.offset, self.frequency*2*numpy.pi + self.offset, 1000))


    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = b'self.jointName',
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = 50)