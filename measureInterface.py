from abc import ABC, ABCMeta, abstractmethod

class MeasureInterface(metaclass=ABCMeta): 
    
    @abstractmethod
    def getMeasureDefiniton(self):
        pass

    @abstractmethod
    def getDatasetforMeasure(self):
        pass

    @abstractmethod
    def computeMeasure(self):
        pass

    @abstractmethod 
    def reportMeasureResult(self):
        pass