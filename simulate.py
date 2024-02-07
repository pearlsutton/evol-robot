import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

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
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

targetAngles = (numpy.sin(numpy.linspace(0, 2*numpy.pi, 10000)))

for x in range (100):
    time.sleep(1/6000)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-numpy.pi/20.0, numpy.pi/20.0),
        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-numpy.pi/20.0, numpy.pi/20.0),
        maxForce = 500)
    print(backLegSensorValues)
    print(frontLegSensorValues)

numpy.save('data/backLegSensorValues.npy', backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/targetAngles.npy', targetAngles, allow_pickle=True, fix_imports=True)
p.disconnect()
