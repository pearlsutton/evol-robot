from solution import SOLUTION
import pybullet as p
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.nextAvailableID = 0
        self.parents = {}
        for key in range(0, c.populationSize):
            self.parents[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        # print(self.parents)


    def Evolve(self):
        for key in self.parents:
            self.parents[key].Start_Simulation("GUI")
        for key in self.parents:
            self.parents[key].Wait_For_Simulation_To_End()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # self.Print()
        # self.Select()

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

        for key in self.children:
            print(f"self.children[key]: {self.children[key]}")
        exit()


    # for key in range(0, c.populationSize):
    #     self.parents[key] = SOLUTION(self.nextAvailableID)
    #     self.nextAvailableID += 1

        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID(self.nextAvailableID)
        # print("self.nextAvailableID: " + self.nextAvailableID)
        # self.nextAvailableID += 1


    def Mutate(self):
        self.child.Mutate()

    def Evaluate(self):
        pass

    def Print(self):
        print(f"Parent Fitness: {self.parent.fitness} Child Fitness: {self.child.fitness}")

    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        pass
        # self.parent.Evaluate("GUI")