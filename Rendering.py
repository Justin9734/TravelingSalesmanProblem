import matplotlib.pyplot as plt
from BruteForce import BruteForceSolution
from random import randint
points = []
for x in range(0, 10):
    points.append([random.randint(0,1000),random.randint(0,1000)])
solution = BruteForceSolution(points)
def plotPoints(points):
