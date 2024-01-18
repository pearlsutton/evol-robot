import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for x in range (1000):
    print(x)
    time.sleep(1/6000)
    p.stepSimulation()


p.disconnect()