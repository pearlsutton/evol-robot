import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import array
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()

simulation.RUN()

# # physicsClient = p.connect(p.DIRECT)
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# # # Determining forces that exist in our world.
# p.setGravity(0,0,-9.8)  # Gravity.
# planeId = p.loadURDF("plane.urdf")  # Floor.
# robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
# p.loadSDF("world.sdf")             # simulate.py tells pybullet to simulate a world stored in world.sdf. Information about our world.
#
# pyrosim.Prepare_To_Simulate(robotId)

# for x in range (1000):
#     time.sleep(1/240)
#     p.stepSimulation()
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_BackLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = c.targetAnglesBackLeg[x],
#         maxForce = 50)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_FrontLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = c.targetAnglesFrontLeg[x],
#         maxForce = 50)
#     c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     # print(backLegSensorValues)
#     # print(frontLegSensorValues)
#
# numpy.save('data/backLegSensorValues.npy', c.backLegSensorValues, allow_pickle=True, fix_imports=True)
# numpy.save('data/frontLegSensorValues.npy', c.frontLegSensorValues, allow_pickle=True, fix_imports=True)
#
# numpy.save('data/targetAnglesBackLeg.npy', c.targetAnglesBackLeg, allow_pickle=True, fix_imports=True)
# numpy.save('data/targetAnglesFrontLeg.npy', c.targetAnglesFrontLeg, allow_pickle=True, fix_imports=True)
#
# p.disconnect()
