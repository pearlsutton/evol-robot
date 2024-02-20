import string
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class SENSOR:
    def __init__(self, linkName: string):
        self.linkName = linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self):
        self.values = c.backLegSensorValues[self.linkName] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
