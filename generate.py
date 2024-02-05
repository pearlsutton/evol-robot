import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[2,2,z] , size=[length,width,height])
    pyrosim.End()
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-1,0,-.5] , size=[length,width,height])

    pyrosim.Send_Joint( name = "BackLeg_FrontLeg" , parent= "BackLeg" , child = "FrontLeg" , type = "revolute", position = [-.5,0,-.5])
    pyrosim.Send_Cube(name="FrontLeg", pos=[1.5,0,0] , size=[length,width,height])

    pyrosim.End()

Create_World()
Create_Robot()


