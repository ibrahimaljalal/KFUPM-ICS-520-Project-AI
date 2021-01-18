import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data=pd.read_csv("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\object_sensor_data.csv")

X=data[["border","color"]]
Y=data[["label"]].values.ravel()

modelObjects = RandomForestClassifier()

modelObjects.fit(X,Y)

joblib.dump(modelObjects, 'C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-objects.sav')

#For accuracy
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)
modelAcc=RandomForestClassifier()
modelAcc.fit(X_train,Y_train)
Y_predicted = modelAcc.predict(X_test)
Y_acc=r2_score(Y_test, Y_predicted)
print('Accuracy: %.3f' % Y_acc)
