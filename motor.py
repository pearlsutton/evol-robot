import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        print("MOTOR constructor")
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        # print("prepare_to_act() called")
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        self.motorValues = self.amplitude * numpy.sin(numpy.linspace(self.frequency*0 + self.offset, self.frequency*2*numpy.pi + self.offset, 1000))


# if (self.jointName == "Torso_BackLeg"):
        #     self.motorValues = self.amplitude * numpy.sin(numpy.linspace((self.frequency*0)/2 + self.offset, ((self.frequency*2)/2)*numpy.pi + self.offset, 1000))
        # else:
        #     self.motorValues = self.amplitude * numpy.sin(numpy.linspace((self.frequency*0)/2 + self.offset, ((self.frequency*2)/2)*numpy.pi + self.offset, 1000))

    def Set_Value(self, robot, t):
        print("Set_Value() called")
        self.motorValues[t] = pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = 50)

    def Save_Values(self):
        numpy.save('data/motorValuesBackLeg.npy', c.newtargetAnglesBackLeg, allow_pickle=True, fix_imports=True)
        numpy.save('data/motorValuesFrontLeg.npy', c.newtargetAnglesFrontLeg, allow_pickle=True, fix_imports=True)