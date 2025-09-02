import matplotlib.pyplot as plt
from BruteForce import BruteForceSolution
from random import randint
points = []
for x in range(0, 10):
    points.append([randint(0,1000),randint(0,1000)])
solution = BruteForceSolution(points)
def plotPoints(points):
