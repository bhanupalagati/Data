"""
created on Sun Mar  4 17:40:55 2018

@author: bhanupalagati
"""

# we are using pickle to predict data
from sklearn import model_selection
import pickle
import pandas as pd
import numpy as np
def prediction():
    test_verify = pd.read_csv('gender_submission.csv')
    y_test = test_verify.iloc[:,[1]].values
    filename = 'titanic_randomForest.sav'
    #X_test = np.array((892),(3),(34.5),(0),(0),(7.83),(0),(1),(0),(1),(0))
    X_test = np.array([[892,3,34.5,0,0,7.83,0,1,0,1,0]])
    loaded_model = pickle.load(open(filename,'rb'))
    y_pred = loaded_model.predict(X_test)
    print(y_pred)

prediction()
