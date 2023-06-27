import os
from random import random
import pandas

from measureInterface import MeasureInterface

class OccupancyMetric(MeasureInterface):
    
    def __init__(self):
        
        self.name = "OccupancyMetric"
        self.description = "Calculate Overall Occupancy"
        self.version = "1.0.0"
        self.author = "Charles Selvaraj"
        self.email = "charlesselvaraj@live.com"
        self.organization = "CC Analytics"

    def getMeasureDefiniton(self):
        pass

    def reportMeasureDefiniton(self):
        pass

    def getDatasetforMeasure(self):
        pass

    def computeMeasure(self):
        pass

if __name__ == '__main__':
    OccupancyMetric();