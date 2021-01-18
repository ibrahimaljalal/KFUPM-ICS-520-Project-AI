import robot

import EnvironmentSimulator as E
import joblib
import numpy as np
import copy

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

modelX=joblib.load("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-localization-X.sav")
modelY=joblib.load("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-localization-Y.sav")
kmeans=joblib.load("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-obstacles.sav")
modelObjects=joblib.load("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-objects.sav")

es=E.EnvironmentSimulator()


rooms=es.getRoomCoordinates()

vm=es.getVM()

updatedVM=copy.deepcopy(E.matrix)

updatedVM=np.array(updatedVM)

bnw,bne,bsw,bse = es.readLocationSensor()




es.DisplaySolution()

es.printRealMap()





#Solutions
#############################################################################################
#############################################################################################



#For localization:
#############################################################################################
#For x and y coordinates (we could compare with the es.DisplaySolution())
#Note: because of the rounding the accuracy is less than 99%
print("\n")
beacons=np.array([bnw,bne,bsw,bse])
beacons=beacons.reshape(1,-1)

x=modelX.predict(beacons)
y=modelY.predict(beacons)


x=int(round(x[0][0]))
y=int(round(y[0][0]))


print("For localization:")
print("_______________________________________")

print("Actual values:")
print("Refer to es.DisplaySolution() results")

print("\n")
print("Solution:")

print("x = "+str(x)+"   y = "+str(y))
print("_______________________________________")
print("\n")
#############################################################################################





#For obstacle detection:
#############################################################################################
print("For obstacle detection:")
print("_______________________________________")

#We could compare from this output or from the first point in the es.printRealMap() function
print("Actual Result:")
print("Refer to es.DisplaySolution() results for point (0,0) (upper left)")


# We do not know which cluster represents zero or one
# But if we did not change the the .sav file then it will not change
# I will make sure that the obstical is zero
print("\n")


#Note: I have made this function to nor print the result (I changed the EnvironmentSimulator.py library)
density,reflection = es.readUltrasoundSensor(0,0) 
print("Solution:")
print("For point (0,0):")
if density>100 and reflection>100: #I know because I have drown the scattered graph
    print("There is an obstical")
    print(int(kmeans.predict([[density,reflection]])))
else:
    print("There is no obstical")
    print(int(kmeans.predict([[density,reflection]])))
print("_______________________________________")
print("\n")
#############################################################################################





#For rooms:
#############################################################################################
print("For rooms:")
print("_______________________________________")
# 1 = Watch
# 2 = Book
# 3 = Ball
# 4 = Phone
objects={1:"Watch",2:"Book",3:"Ball",4:"Phone"}

print("Actual valuse:")
print("Room 1:")
border1,color1 = es.readCameraSensor(rooms[0][0],rooms[0][1])
print("Room 2:")
border2,color2 = es.readCameraSensor(rooms[1][0],rooms[1][1])
print("Room 3:")
border3,color3 = es.readCameraSensor(rooms[2][0],rooms[2][1])
print("Room 4:")
border4,color4 = es.readCameraSensor(rooms[3][0],rooms[3][1])

print("\n")
print("Solution:")
print("There is a "+objects[int(modelObjects.predict([[border1,color1]]))]+" in Room 1")
print("There is a "+objects[int(modelObjects.predict([[border2,color2]]))]+" in Room 2")
print("There is a "+objects[int(modelObjects.predict([[border3,color3]]))]+" in Room 3")
print("There is a "+objects[int(modelObjects.predict([[border4,color4]]))]+" in Room 4")
print("_______________________________________")
#############################################################################################





#For Navigation
#############################################################################################

allActualPath=[]



start=[(x,y),(rooms[0][0],rooms[0][1]),(rooms[1][0],rooms[1][1]),(rooms[2][0],rooms[2][1])]
end=[(rooms[0][0],rooms[0][1]),(rooms[1][0],rooms[1][1]),(rooms[2][0],rooms[2][1]),(rooms[3][0],rooms[3][1])]



pathExistes=True


for i in range(len(rooms)):
    actualPath=[]
    actualPath.append(start[i])

    endPath=[]
    endPath=end[i]

    while True:
            
        updatedVM=robot.senseThenUpdateVM(actualPath[-1][0],actualPath[-1][1],es.readUltrasoundSensor,updatedVM)
        nextPosition = robot.moveOneStep(actualPath[-1][0],actualPath[-1][1],endPath[0],endPath[1],updatedVM)
        if nextPosition !=None:
            actualPath.append(nextPosition)
            if actualPath[-1]==endPath:
                break


        else:
            pathExistes=False
            break


    allActualPath.append(actualPath[:])

    grid = Grid(matrix=updatedVM)

    startPoint = grid.node(start[i][0],start[i][1]) 
    endPoint = grid.node(end[i][0],end[i][1]) 

    print("\n")
    print("Path graph to room number "+str(i+1))
    print(grid.grid_str(path=actualPath, start=startPoint, end=endPoint))


    if pathExistes ==True:
        print("Path to Room "+str(i+1)+" is:")
        print(str(actualPath))

    else:
        print("The robot couldn't reach Room "+str(i+1)+" ,but this is the path it took:")
        print(str(actualPath))
        break





allPath=[]
for i in range(len(allActualPath)):
    for j in range(len(allActualPath[i])):
     allPath.append(allActualPath[i][j])





theStart=grid.node(start[0][0],start[0][1])
theEnd=grid.node(end[len(rooms)-1][0],end[len(rooms)-1][1])

print("\n")
if pathExistes ==True:
    print("The robot successfully reached all the rooms. This is the whole path graph:")
    print(grid.grid_str(path=allPath, start=theStart, end=theEnd))
    print("This is the whole path:")
    print(allPath)

else:
    print("The robot couldn't reached all the rooms. This is the whole path graph:")
    print(grid.grid_str(path=allPath, start=theStart, end=theEnd))
    print("This is the whole path :")
    print(allPath)

#############################################################################################





