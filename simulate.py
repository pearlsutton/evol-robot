import pybullet as p
import time

physicsClient = p.connect(p.GUI)

# Determining forces that exist in our world. Gravity.
p.setGravity(0,0,-9.8)
# Information about our world.
p.loadSDF("box.sdf")

for x in range (1000):
    print(x)
    time.sleep(1/60)
    p.stepSimulation()


p.disconnect()