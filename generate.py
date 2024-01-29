import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5


# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box2", pos=[x,y,z+1] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box3", pos=[x,y,z+2] , size=[length,width,height])


for i in range (10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,(z+i)] , size=[length,width,height])
    length = length * .90
    width = width * .90
    height = height * .90

pyrosim.End()