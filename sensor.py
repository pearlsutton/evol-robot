import string
import numpy


class SENSOR:
    def __init__(self, linkName: string):
        self.linkName = linkName
        self.values = numpy.zeros(1000)
        print(self.values)
