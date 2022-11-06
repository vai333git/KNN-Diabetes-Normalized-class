# here all the functions will be written
import pickle
import json
import config
import numpy as np

class Diabetes():
    def __init__(self,Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):

        self.Glucose                   = Glucose
        self.BloodPressure             = BloodPressure
        self.SkinThickness             = SkinThickness
        self.Insulin                   = Insulin
        self.BMI                       = BMI
        self.DiabetesPedigreeFunction  = DiabetesPedigreeFunction
        self.Age	                   = Age


    def load_model(self):
        print('we are in load_module_function')
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
        
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    
    def Normalize(self,array):     
        list1 = []
        diff_arr = max(array) - min(array)
        for i in array:
            var = ((i - min(array))/diff_arr)
            list1.append(var)
        Normalized_arr = np.asarray(list1)
        return Normalized_arr
    
    def get_predicted_outcome(self):
        self.load_model()
##################################################################################
        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age

        test_array_normalized = self.Normalize(test_array)

        print('test_array_normalized is :' , test_array_normalized)
        a=str(int(np.around(self.model.predict([test_array_normalized]),0)))
        predicted_outcome = self.json_data['Diabetes'][a]

        return predicted_outcome

        

        	
        	
        	
        	
        	
        	
        	