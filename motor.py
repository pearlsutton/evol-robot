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
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        self.amplitude = c.amplitudeFrontLeg
        self.frequency2 = 2*c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        self.motorValues = self.amplitude * numpy.sin(numpy.linspace(self.frequency*0 + self.offset, self.frequency*2*numpy.pi + self.offset, 1000))
        self.motorValues2 = self.amplitude * numpy.sin(numpy.linspace(self.frequency2*0 + self.offset, self.frequency2*2*numpy.pi + self.offset, 1000))


        # if (self.jointName == "Torso_BackLeg"):
        #     self.motorValuesBackLeg = self.amplitude * numpy.sin(numpy.linspace(self.amplitudeBackLeg*0 + self.offset, self.amplitudeBackLeg*2*numpy.pi + self.offset, 1000))
        #     self.motorValuesFrontLeg = self.amplitude * numpy.sin(numpy.linspace(self.amplitudeBackLeg*0 + self.offset, self.amplitudeBackLeg*2*numpy.pi + self.offset, 1000))
        # elif (self.jointName == "Torso_FrontLeg"):
        #     self.motorValuesBackLeg = self.amplitude * numpy.sin(numpy.linspace(self.amplitudeFrontLeg*0 + self.offset, self.amplitudeFrontLeg*2*numpy.pi + self.offset, 1000))
        #     self.motorValuesFrontLeg = self.amplitude * numpy.sin(numpy.linspace(self.amplitudeFrontLeg*0 + self.offset, self.amplitudeFrontLeg*2*numpy.pi + self.offset, 1000))


    def Set_Value(self, robot, t):
            print("Set_Value() called")
            self.motorValues[t] = pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot,
                jointName = b'Torso_BackLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.motorValues[t],
                maxForce = 50)
            self.motorValues2[t] = pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot,
                jointName = b'Torso_FrontLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.motorValues2[t],
                maxForce = 50)

    def Save_Values(self):
        pass
        numpy.save('data/motorValuesBackLeg.npy', c.newtargetAnglesBackLeg, allow_pickle=True, fix_imports=True)
        numpy.save('data/motorValuesFrontLeg.npy', c.newtargetAnglesFrontLeg, allow_pickle=True, fix_imports=True)