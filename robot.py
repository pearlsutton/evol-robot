from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

class ROBOT:
    def __init__(self):
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for i in self.motors:
            self.motors[i].Set_Value(self.robotId, t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()