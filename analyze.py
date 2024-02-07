import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy', mmap_mode=None, allow_pickle=False)
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy', mmap_mode=None, allow_pickle=False)

print(backLegSensorValues)
print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg Sensor Values')
matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg Sensor Values')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
