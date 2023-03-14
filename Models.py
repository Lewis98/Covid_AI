# = = = = = = = = = = #
#        CELL 1       #
# = = = = = = = = = = #

import numpy as np
import pandas as pd

import pickle #Load dataset

#sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#Models
from sklearn.linear_model import LogisticRegression
from sklearn import svm



# = = = = = = = = = = #
#        CELL 2       #
# = = = = = = = = = = #

#Importing the Dataset

#Set filepath to directory containing images
DF = r'.\\Xray_data.p' # REQUIRED - Filepath to pickled dataset generated from Img_conversion.py

DF = open(DF, "rb")

#Create array to store images
Xray_data = pickle.load(DF)



# = = = = = = = = = = #
#        CELL 3       #
# = = = = = = = = = = #

#Instantiating models and split data into testing and training sets


LR = LogisticRegression(max_iter=1000)
SV = svm.SVC(kernel='linear')

X_train, X_test, Y_train, Y_test = train_test_split(Xray_data["data"], Xray_data["targets"], 
                                                    test_size=0.4, shuffle=True, random_state=2)



# = = = = = = = = = = #
#        CELL 4       #
# = = = = = = = = = = #

#Logistic regression fitting and evaluation

LR.fit(X_train, Y_train)


Y_train_pred = LR.predict(X_train)
Y_test_pred = LR.predict(X_test)
print("Model Accuracy: {:.3f}".format(accuracy_score(Y_test, Y_test_pred)))



# = = = = = = = = = = #
#        CELL 5       #
# = = = = = = = = = = #

#Logistic regression fitting and evaluation

SV.fit(X_train, Y_train)


Y_train_pred = SV.predict(X_train)
Y_test_pred = SV.predict(X_test)
print("Model Accuracy: {:.3f}".format(accuracy_score(Y_test, Y_test_pred)))