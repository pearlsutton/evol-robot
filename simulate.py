import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Determining forces that exist in our world.
# Gravity.
p.setGravity(0,0,-9.8)
# Floor.
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")  # simulate.py tells pybullet to simulate a robot stored in body.urdf.
p.loadSDF("world.sdf")             # simulate.py tells pybullet to simulate a world stored in world.sdf. Information about our world.

for x in range (1000):
    print(x)
    time.sleep(1/60)
    p.stepSimulation()

p.disconnect()