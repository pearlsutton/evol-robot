import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

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
backLegSensorValues = numpy.zeros(10000)


for x in range (10000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegSensorValues)

numpy.save('backLegSensorValues.npy', backLegSensorValues)
p.disconnect()
