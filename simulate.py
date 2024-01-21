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
# Information about our world.
p.loadSDF("boxes.sdf")

for x in range (1000):
    print(x)
    time.sleep(1/60)
    p.stepSimulation()

p.disconnect()