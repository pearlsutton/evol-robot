from solution import SOLUTION
import pybullet as p
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

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
        self.parent.Evaluate("GUI")
