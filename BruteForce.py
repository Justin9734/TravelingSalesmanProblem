from math import sqrt
import itertools

def FindDistance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def BruteForceSolution(points):
    paths = itertools.permutations(points)
    best_distance = float("inf")
    best_route = None
    distances_checked = 0

    for path in paths:
        distance = 0
        for i in range(len(path) - 1):
            distances_checked += 1
            distance += FindDistance(path[i], path[i+1])
        distance += FindDistance(path[-1], path[0])

        if distance < best_distance:
            best_distance = distance
            best_route = path

    print("Distances checked:", distances_checked)
    return [best_distance, best_route]
