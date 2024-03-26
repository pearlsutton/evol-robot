import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = 2 * numpy.random.rand(3, 2) - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        # SOLUTION.Create_World(self)
        # SOLUTION.Create_Body(self)
        SOLUTION.Create_Brain(self)
        # print(f"os.system self.myID: {self.myID}")
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFile = f"fitness{str(self.myID)}.txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        # print(f"SELF.FITNESS: {self.fitness}")
        f.close()
        os.system("rm fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pass
        # pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[2,2,z] , size=[length,width,height])
        # pyrosim.End()
    def Create_Body(self):
        pass
        # pyrosim.Start_URDF("body.urdf")
        # pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])
        # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
        # pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length,width,height])
        # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
        # pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
        # pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        sensor_neurons_list = [0 , 1 , 2]
        sensor_neurons_vector = numpy.array(sensor_neurons_list)
        motor_neurons_list = [0, 1]
        motor_neurons_vector = numpy.array(motor_neurons_list)

        for currentRow in sensor_neurons_vector:
            for currentColumn in motor_neurons_vector:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID