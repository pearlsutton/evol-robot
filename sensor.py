import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class SENSOR:
    def __init__(self, linkName):
        print("SENSOR constructor")
        self.linkName = linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save('data/SensorValuesBackLeg.npy', c.backLegSensorValues, allow_pickle=True, fix_imports=True)
        numpy.save('data/SensorValuesFrontLeg.npy', c.frontLegSensorValues, allow_pickle=True, fix_imports=True)
