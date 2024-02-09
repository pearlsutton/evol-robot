import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import array

amplitude = numpy.pi/4.0
frequency = 1
phaseOffset = 0

# physicsClient = p.connect(p.DIRECT)
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# Determining forces that exist in our world.
p.setGravity(0,0,-9.8)  # Gravity.
planeId = p.loadURDF("plane.urdf")  # Floor.
robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
p.loadSDF("world.sdf")             # simulate.py tells pybullet to simulate a world stored in world.sdf. Information about our world.

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

targetAngles = numpy.sin(numpy.linspace(frequency * 0 + phaseOffset, frequency * 2*numpy.pi + phaseOffset, 1000)) * amplitude

for x in range (100):
    time.sleep(1/240)
    p.stepSimulation()
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[x],
        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[x],
        maxForce = 500)
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(backLegSensorValues)
    print(frontLegSensorValues)

numpy.save('data/backLegSensorValues.npy', backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('data/targetAngles.npy', targetAngles, allow_pickle=True, fix_imports=True)
p.disconnect()
