import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy', mmap_mode=None, allow_pickle=False)
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy', mmap_mode=None, allow_pickle=False)
targetAngles = numpy.load('data/targetAngles.npy', mmap_mode=None, allow_pickle=False)


# print(backLegSensorValues)
# print(frontLegSensorValues)
print(targetAngles)

# matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg Sensor Values', linewidth = 2.5)
# matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg Sensor Values')
matplotlib.pyplot.plot(targetAngles, label='Target Angles')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()


