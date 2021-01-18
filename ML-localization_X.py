import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
import joblib


data=pd.read_csv("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\location_sensor_data.csv")

beacons=data[["Bnw","Bne","Bsw","Bse"]]

X=data[["X"]]

#For X
modelX=LinearRegression()

modelX.fit(beacons,X)

joblib.dump(modelX, 'C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-localization-X.sav')



##For X accuracy 
beacons_train,beacons_test,X_train,X_test=train_test_split(beacons, X, test_size=0.30)

modelXAcc = LinearRegression()
modelXAcc.fit(beacons_train,X_train)
X_predicted=modelXAcc.predict(beacons_test)
X_acc = r2_score(X_test, X_predicted)
print('Accuracy: %.3f' % X_acc)




