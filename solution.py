import numpy
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self):
        self.weights = 2 * numpy.random.rand(3, 2) - 1

    def Evaluate(self):
        SOLUTION.Create_World(self)
        SOLUTION.Create_Robot(self)
        SOLUTION.Create_Brain(self)
        os.system("python3 simulate.py")
    def Create_World(self):
        pass
        # pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[2,2,z] , size=[length,width,height])
        # pyrosim.End()
    def Create_Robot(self):
         pass
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

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