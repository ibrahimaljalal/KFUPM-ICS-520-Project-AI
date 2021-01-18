import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
import joblib


data=pd.read_csv("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\location_sensor_data.csv")

beacons=data[["Bnw","Bne","Bsw","Bse"]]

Y=data[["Y"]]

#For Y

modelY=LinearRegression()

modelY.fit(beacons,Y)


joblib.dump(modelY, 'C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-localization-Y.sav')


#For Y
modelY=LinearRegression()

modelY.fit(beacons,Y)





##For Y accuracy
beacons_train,beacons_test,Y_train,Y_test=train_test_split(beacons, Y, test_size=0.30)
modelYAcc = LinearRegression()
modelYAcc.fit(beacons_train,Y_train)
Y_predicted=modelYAcc.predict(beacons_test)
Y_acc = r2_score(Y_test, Y_predicted)
print('Accuracy: %.3f' % Y_acc)

