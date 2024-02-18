import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import array

amplitudeBackLeg = numpy.pi/4.0
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

amplitudeFrontLeg = numpy.pi/4.0
frequencyFrontLeg = 10
phaseOffsetFrontLeg = numpy.pi/4.0

# physicsClient = p.connect(p.DIRECT)
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# Determining forces that exist in our world.
p.setGravity(0,0,-9.8)  # Gravity.
planeId = p.loadURDF("plane.urdf")  # Floor.
robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
p.loadSDF("world.sdf")             # simulate.py tells pybullet to simulate a world stored in world.sdf. Information about our world.

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(numpy.linspace(frequencyBackLeg*0 + phaseOffsetBackLeg, frequencyBackLeg*2*numpy.pi + phaseOffsetBackLeg, 1000))
targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(numpy.linspace(frequencyFrontLeg*0 + phaseOffsetFrontLeg, frequencyFrontLeg*2*numpy.pi + phaseOffsetFrontLeg, 1000))

for x in range (1000):
    time.sleep(1/240)
    p.stepSimulation()
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesBackLeg[x],
        maxForce = 20)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesFrontLeg[x],
        maxForce = 20)
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # print(backLegSensorValues)
    # print(frontLegSensorValues)

numpy.save('data/backLegSensorValues.npy', backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues, allow_pickle=True, fix_imports=True)

numpy.save('data/targetAnglesBackLeg.npy', targetAnglesBackLeg, allow_pickle=True, fix_imports=True)
numpy.save('data/targetAnglesFrontLeg.npy', targetAnglesFrontLeg, allow_pickle=True, fix_imports=True)

p.disconnect()
