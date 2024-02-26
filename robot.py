from sensor import SENSOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

class ROBOT:
    def __init__(self):
        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    # def Prepare_To_Act(self):
        # self.sensors = {}
        # for linkName in pyrosim.linkNamesToIndices:
        #     self.sensors[linkName] = SENSOR(linkName)