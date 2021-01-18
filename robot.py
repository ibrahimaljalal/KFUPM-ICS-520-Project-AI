from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np


def senseThenUpdateVM(x,y,readUltrasoundSensor,updatedVM):
    
    #N
    if y-1>=0:
        density,reflection=readUltrasoundSensor(x,y-1)
        if density>100 and reflection>100:
            updatedVM[y-1][x]=0
    #NE
    if (y-1>=0 and  x+1<updatedVM.shape[1]):
        density,reflection=readUltrasoundSensor(x+1,y-1)
        if density>100 and reflection>100:
            updatedVM[y-1][x+1]=0
    #E
    if  (x+1<updatedVM.shape[1]):
        density,reflection=readUltrasoundSensor(x+1,y)
        if density>100 and reflection>100:
            updatedVM[y][x+1]=0
    #SE
    if (x+1<updatedVM.shape[1] and y+1<updatedVM.shape[0]):
        density,reflection=readUltrasoundSensor(x+1,y+1)
        if density>100 and reflection>100:
            updatedVM[y+1][x+1]=0
    #S
    if (y+1<updatedVM.shape[0]):
        density,reflection=readUltrasoundSensor(x,y+1)
        if density>100 and reflection>100:
            updatedVM[y+1][x]=0
    
    #SW
    if (y+1<updatedVM.shape[0] and x-1>=0):
        density,reflection=readUltrasoundSensor(x-1,y+1)
        if density>100 and reflection>100:
            updatedVM[y+1][x-1]=0
    #W
    if (x-1>=0):
        density,reflection=readUltrasoundSensor(x-1,y)
        if density>100 and reflection>100:
            updatedVM[y][x-1]=0

    #NW
    if (y-1>=0 and x-1>=0):
        density,reflection=readUltrasoundSensor(x-1,y-1)
        if density>100 and reflection>100:
            updatedVM[y-1][x-1]=0


    
    return updatedVM


def moveOneStep(pathLastX,pathLastY,goalX,goalY,updatedVM):

        
    grid = Grid(matrix=updatedVM)

    start = grid.node(pathLastX,pathLastY)
    end = grid.node(goalX,goalY)


    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, _ = finder.find_path(start, end, grid)

    try:
        return path[1]
    except Exception:
        return None







    