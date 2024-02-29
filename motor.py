import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        self.amplitude = c.amplitudeFrontLeg
        self.frequency2 = 0.5 * c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        if (self.jointName == b'Torso_BackLeg'):
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(self.frequency*0 + self.offset, self.frequency*2*numpy.pi + self.offset, 1000))
            self.motorValues2 = self.amplitude * numpy.sin(numpy.linspace(2*self.frequency2*0 + self.offset, 2*self.frequency2*2*numpy.pi + self.offset, 1000))

        elif (self.jointName == b'Torso_FrontLeg'):
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(2*self.frequency*0 + self.offset, 2*self.frequency*2*numpy.pi + self.offset, 1000))
            self.motorValues2 = self.amplitude * numpy.sin(numpy.linspace(self.frequency2*0 + self.offset, self.frequency2*2*numpy.pi + self.offset, 1000))


    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = b'Torso_BackLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 50)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = b'Torso_FrontLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 50)

    def Save_Values(self):
        pass
        numpy.save('data/motorValuesBackLeg.npy', c.newtargetAnglesBackLeg, allow_pickle=True, fix_imports=True)
        numpy.save('data/motorValuesFrontLeg.npy', c.newtargetAnglesFrontLeg, allow_pickle=True, fix_imports=True)