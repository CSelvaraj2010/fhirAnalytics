import os
from random import random
import pandas
from measureInterface import MeasureInterface 


# The Barthel ADL Index is an ordinal scale used to measure performance in activities of daily living (ADL).  
class BarthelADLIndex():

    twoADLScoreList: list[int] = [0, 5]
    threeADLScoreList: list[int] = [0, 5, 10]
    fourADLScoreList: list[int] = [0, 5, 10, 15]

    def __init__(self):
        
        self.name = "barthelADLIndex"
        self.description = "Barthel ADL Index"
        self.version = "1.0.0"
        self.author = "Charles Selvaraj"
        self.email = "charlesselvaraj@live.com"        
        self.organization = "CC Analytics"

    def getMeasureDefiniton(self):
        pass
        
    def getDatasetforMeasure(self):
        return 

    def computeIndex(self):

        print("Compute Barthel Index")

        patientsDF = self.loadPatientData()
        patientsDF = self.generatePatientDataWithADL(patientsDF) 
                
        patientsDF = self.computeADLScore(patientsDF)
        patientsDF = self.computeADLIndex(patientsDF)         
        self.adlSummaryForPatientData(patientsDF)
        
        print(patientsDF.head())

    def adlSummaryForPatientData(self, patientsDF):
            
        print("ADL Summary for Patient Data") 
        print(patientsDF.groupby(['BarthelIndex']).sum())
        

    def loadPatientData(self):

        print("Load Patient Data")
        
        patientsFilePath = os.path.join(os.path.dirname(__file__) , "../data/patients.csv")
        patientsDF = pandas.read_csv(patientsFilePath)
        
        return patientsDF

    def computeADLIndex(self, patientsDF):
        
        score = patientsDF['BarthelScore'].values[0]

        if score >=80:            
            patientsDF['BarthelIndex'] = "Independent"
        if score >=60:
            patientsDF['BarthelIndex'] = "Minimally dependent"
        if score >=40:
            patientsDF['BarthelIndex'] = "Very dependent"
        if score >=20:
            patientsDF['BarthelIndex'] = "Partially dependent"            
        if score < 20:
            patientsDF['BarthelIndex'] = "Totally dependent" 
        
        return patientsDF

    def computeADLScore(self, patientsDF):  

        columnsToSum = ['CC_Barthel_Feeding','CC_Barthel_Bathing'
                        ,'CC_Barthel_Grooming','CC_Barthel_Dressing'
                        ,'CC_Barthel_BowelControl','CC_Barthel_BladderControl'
                        ,'CC_Barthel_ToiletUse','CC_Barthel_Transfer'
                        ,'CC_Barthel_Mobility','CC_Barthel_Stairs']

        patientsDF['BarthelScore']=patientsDF[columnsToSum].sum(axis=1)    
        
        return patientsDF
        
    def generatePatientDataWithADL(self, patientsDF):

        patientsDF['CC_Barthel_Feeding'] = self.threeADLScoreList[int(random() * 3)]
        patientsDF['CC_Barthel_Bathing'] = self.twoADLScoreList[int(random() * 2)]
        patientsDF['CC_Barthel_Grooming'] = self.twoADLScoreList[int(random() * 2)]
        patientsDF['CC_Barthel_Dressing'] = self.threeADLScoreList[int(random() * 3)]
        patientsDF['CC_Barthel_BowelControl'] = self.threeADLScoreList[int(random() * 3)]
        patientsDF['CC_Barthel_BladderControl'] = self.fourADLScoreList[int(random() * 4)]
        patientsDF['CC_Barthel_ToiletUse'] = self.threeADLScoreList[int(random() * 3)]
        patientsDF['CC_Barthel_Transfer'] = self.fourADLScoreList[int(random() * 4)]
        patientsDF['CC_Barthel_Mobility'] = self.fourADLScoreList[int(random() * 4)]
        patientsDF['CC_Barthel_Stairs'] = self.threeADLScoreList[int(random() * 3)]

        return patientsDF

    def reportMeasureDefiniton(self):
        pass


if __name__ == '__main__':
    BarthelADLIndex();