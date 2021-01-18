from random import randint
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from copy import deepcopy
from math import sqrt
'''
This class simulates a real navigation environments.
It creates artificial obstecles and provide sensing information.
'''
matrix = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
roomCount = 4
obstcleCount =50
obstcleEnabled=True
objectsNames=['Watch','Ball','Book','Phone']

class EnvironmentSimulator:
    def DisplaySolution(self):
        print('Start point is ',self.start)
        for i in range(0,len(self.rooms)):
            print("Room ",i+1,': ',self.objects[i])

    def getRoomCoordinates(self):
        return self.rooms

    def getVM(self):
        return self.VM
    
    def __distance(self,x1,y1,x2,y2):
        return sqrt((x1-x2)**2+(y1-y2)**2)

    def __drawRoom(self, map, r, i):
        door = randint(1,4)
        if door != 1:
            map[r[1]+1][r[0]]=0
        else:
            map[r[1]+1][r[0]]=1
            map[r[1]+2][r[0]]=1
        if door != 2:
            map[r[1]][r[0]+1]=0
        else:
            map[r[1]][r[0]+1]=1
            map[r[1]][r[0]+2]=1
        if door != 3:
            map[r[1]-1][r[0]]=0
        else:
            map[r[1]-1][r[0]]=1
            map[r[1]-2][r[0]]=1
        if door != 4:
            map[r[1]][r[0]-1]=0
        else:
            map[r[1]][r[0]-1]=1
            map[r[1]][r[0]-2]=1

        map[r[1]+1][r[0]+1]=0
        map[r[1]+1][r[0]-1]=0
        map[r[1]-1][r[0]+1]=0
        map[r[1]-1][r[0]-1]=0
        map[r[1]][r[0]]=i
        

    def __dimensions(self, map):          #computes the dimensions of the map
        for row in map:
            length=len(map)
            width=len(row)
            break
        return length, width

    def __distance_enough(self, x,y,points):
        for p in points:
            if self.__distance(x,y,p[0],p[1]) <= sqrt(2):
                return False
        return True


    def __generateObstcles(self, map):   # places random obstcles in the map
        map_with_obstcles = deepcopy(map)
        self.length, self.width=self.__dimensions(map_with_obstcles)
        
        if obstcleEnabled:
            obstclePoints = set()
            while len(obstclePoints) < obstcleCount:
                x = randint(0,self.width-1)
                y = randint(0,self.length-1)
                obstclePoints.add((x,y))

            for obs in obstclePoints:
                map_with_obstcles[obs[1]][obs[0]]=0
            
        self.roomPoints = set()
        while len(self.roomPoints) < roomCount:
            x = randint(2,self.width-3)
            y = randint(2,self.length-3)
            self.roomPoints.add((x,y))
        i=1
        for rom in self.roomPoints:
            self.rooms.append(rom)
            self.__drawRoom(map_with_obstcles, rom, i)
            i=i+1
            
        start_set= False
        while not start_set:
            x = randint(0,self.width-1)
            y = randint(0,self.length-1)
            if self.__distance_enough(x,y,self.roomPoints.union(obstclePoints)):
                start_set = True
                self.start = (x,y)

        return Grid(matrix=map_with_obstcles)

    def __generateObjects(self):
        obj = objectsNames.copy()
        while len(obj) != 0:
            j = randint(0,len(obj)-1)
            self.objects.append(obj[j])
            obj.pop(j)

    
    def printRealMap(self):            # print map with Obstacles
        print(self.RM.grid_str(show_weight=True))

    def __init__(self):
        self.rooms = []
        self.objects = []
        self.VM = Grid(matrix=matrix)
        self.RM = self.__generateObstcles(matrix)
        self.__generateObjects()
        #self.diagonal_movement=DiagonalMovement.always

    
    def readLocationSensor(self):
        x,y=self.start[0],self.start[1]
        maxVal=400
        maxDistance = self.__distance(0,0,25,20)
        bnw = maxVal*(1-self.__distance(x,y,0,0)/maxDistance)
        bne = maxVal*(1-self.__distance(x,y,25,0)/maxDistance)
        bsw = maxVal*(1-self.__distance(x,y,0,20)/maxDistance)
        bse = maxVal*(1-self.__distance(x,y,25,20)/maxDistance)
        return bnw,bne,bsw,bse
    
    def readUltrasoundSensor(self, x, y):

        den_centre1 = 20
        den_centre2 = 120

        ref_centre1 = 65
        ref_centre2 = 200
        #print(self.RM.node(x,y).walkable)
        #print(self.RM.node(x,y).weight)
        if self.RM.node(x,y).walkable:
            d = den_centre1+randint(-20,20)
            r = ref_centre1+randint(-40,40)
        else:
            d = den_centre2+randint(-20,20)
            r = ref_centre2+randint(-40,40)

        return d,r

    def readCameraSensor(self, x, y):              #returns sensing information for location (x,y)
        loc = self.rooms.index((x,y))
        obj = self.objects[loc]
        bor_centre1 = 20
        bor_centre2 = 80
        bor_centre3 = 130
        bor_centre4 = 180

        col_centre1 = 200
        col_centre2 = 300
        col_centre3 = 400
        col_centre4 = 500
        print(obj)
        if obj == 'Watch':
            b = bor_centre1+randint(-20,20)
            c = col_centre1+randint(-40,40)

        elif obj == 'Book':
            b = bor_centre2+randint(-20,20)
            c = col_centre2+randint(-40,40)
        
        elif obj == 'Ball':
            b = bor_centre3+randint(-20,20)
            c = col_centre3+randint(-40,40)

        elif obj == 'Phone':
            b = bor_centre4+randint(-20,20)
            c = col_centre4+randint(-40,40)
        
        return b,c
