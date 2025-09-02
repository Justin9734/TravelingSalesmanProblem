from math import *
import itertools

def FindDistance(point1, point2): # idc abt lambda
    distance = sqrt(abs(point1[0]-point2[0])**2 + abs(point1[1]-point2[1])**2)
    return distance

def BruteForceSolution(points):
    paths = itertools.combinations(points, len(points))
    distances = []
    for path in paths:
        distance = 0
        for point in range(0, len(path)):
            try:
                distance += FindDistance(path[point], path[point+1])
            except:
                pass
        distances.append(distance)
    return [min(distances), paths[distances.index(min(distances))]]
        