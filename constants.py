import numpy

# Back leg
amplitudeBackLeg = numpy.pi/6
frequencyBackLeg = 18
phaseOffsetBackLeg = 0

# Front leg
amplitudeFrontLeg = -numpy.pi/4
frequencyFrontLeg = 18
phaseOffsetFrontLeg = numpy.pi/4

# Sensor values
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

newbackLegSensorValues = numpy.zeros(1000)
newfrontLegSensorValues = numpy.zeros(1000)

# Angle values
targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(numpy.linspace(frequencyBackLeg*0 + phaseOffsetBackLeg, frequencyBackLeg*2*numpy.pi + phaseOffsetBackLeg, 1000))
targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(numpy.linspace(frequencyFrontLeg*0 + phaseOffsetFrontLeg, frequencyFrontLeg*2*numpy.pi + phaseOffsetFrontLeg, 1000))


newtargetAnglesBackLeg = amplitudeBackLeg * numpy.sin(numpy.linspace(frequencyBackLeg*0 + phaseOffsetBackLeg, frequencyBackLeg*2*numpy.pi + phaseOffsetBackLeg, 1000))
newtargetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(numpy.linspace(frequencyFrontLeg*0 + phaseOffsetFrontLeg, frequencyFrontLeg*2*numpy.pi + phaseOffsetFrontLeg, 1000))
