import string
import constants as c

class MOTOR:
    def __init__(self, jointName: string):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        pass
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg
    #     pyrosim.Set_Motor_For_Joint(
    #         bodyIndex = self.robot,
    #         jointName = b'Torso_BackLeg',
    #         controlMode = p.POSITION_CONTROL,
    #         targetPosition = c.targetAnglesBackLeg[t],
    #         maxForce = 50)
    #     pyrosim.Set_Motor_For_Joint(
    #         bodyIndex = self.robot,
    #         jointName = b'Torso_FrontLeg',
    #         controlMode = p.POSITION_CONTROL,
    #         targetPosition = c.targetAnglesFrontLeg[t],
    #         maxForce = 50)