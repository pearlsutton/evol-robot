import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        pass
        numpy.save('data/SensorValuesBackLeg.npy', c.newbackLegSensorValues, allow_pickle=True, fix_imports=True)
        numpy.save('data/SensorValuesFrontLeg.npy', c.newfrontLegSensorValues, allow_pickle=True, fix_imports=True)
