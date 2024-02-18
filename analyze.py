import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy', mmap_mode=None, allow_pickle=False)
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy', mmap_mode=None, allow_pickle=False)

targetAnglesFrontLegValues = numpy.load('data/targetAnglesBackLeg.npy', mmap_mode=None, allow_pickle=False)
targetAnglesBackLegValues = numpy.load('data/targetAnglesFrontLeg.npy', mmap_mode=None, allow_pickle=False)

# print(backLegSensorValues)
# print(frontLegSensorValues)
# print(targetAngles)

# matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg Sensor Values', linewidth = 2.5)
# matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg Sensor Values')

matplotlib.pyplot.plot(targetAnglesFrontLegValues, label='BackLeg Target Angles', linewidth = 2.5)
matplotlib.pyplot.plot(targetAnglesBackLegValues, label='FrontLeg Target Angles')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()


