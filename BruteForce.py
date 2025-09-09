from math import sqrt
import itertools

def FindDistance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def BruteForceSolution(points):
    start = points[0]
    other_points = points[1:]

    paths = itertools.permutations(other_points)
    best_distance = float("inf")
    best_route = None
    distances_checked = 0

    for perm in paths:
        path = (start,) + perm
        distance = 0
        for i in range(len(path) - 1):
            distances_checked += 1
            distance += FindDistance(path[i], path[i+1])
            print("\r Distances Checked:" + str(distances_checked), end = "", flush=True)
        distances_checked += 1
        distance += FindDistance(path[-1], path[0])
        print("\r Distances Checked:" + str(distances_checked), end="", flush=True)

        if distance < best_distance:
            best_distance = distance
            best_route = path

    return [best_distance, best_route]
