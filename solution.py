import numpy
import pyrosim.pyrosim as pyrosim

class SOLUTION:
    def __init__(self):
        self.weights = 2 * numpy.random.rand(3, 2) - 1

    def Evaluate(self):

    def Create_World(self):
        pass
        # pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[2,2,z] , size=[length,width,height])
        # pyrosim.End()
     def Create_Robot(self):
         pass
    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        sensor_neurons_list = [0 , 1 , 2]
        currentRow = numpy.array(sensor_neurons_list)
        motor_neurons_list = [3, 4]
        currentColumn = numpy.array(motor_neurons_list)

        for i in currentRow:
            for j in currentColumn:
                pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = random.uniform(-1,1) )

        pyrosim.End()