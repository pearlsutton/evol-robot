import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

# physicsClient = p.connect(p.DIRECT)
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Determining forces that exist in our world.
# Gravity.
p.setGravity(0,0,-9.8)
# Floor.
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
p.loadSDF("world.sdf")             # simulate.py tells pybullet to simulate a world stored in world.sdf. Information about our world.

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
# targetAngles = numpy.zeros(100)
targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000)) * numpy.pi/4.0

for x in range (1000):
    time.sleep(1/240)
    p.stepSimulation()
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-numpy.pi/4.0, numpy.pi/4.0),
        maxForce = 50)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-numpy.pi/2.0, numpy.pi/2.0),
        maxForce = 50)
    targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000))
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(backLegSensorValues)
    print(frontLegSensorValues)

numpy.save('data/backLegSensorValues.npy', backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/targetAngles.npy', targetAngles, allow_pickle=True, fix_imports=True)
p.disconnect()
