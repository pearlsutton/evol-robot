import random
import pyrosim.pyrosim as pyrosim
import numpy

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
    pass

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    sensor_neurons_list = [0 , 1 , 2]
    sensor_neurons_vector = numpy.array(sensor_neurons_list)
    motor_neurons_list = [3, 4]
    motor_neurons_vector = numpy.array(motor_neurons_list)

    for i in sensor_neurons_vector:
        for j in motor_neurons_vector:
            pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = random.random() )

    pyrosim.End()

Create_World()
Create_Robot()
Generate_Body()
Generate_Brain()


