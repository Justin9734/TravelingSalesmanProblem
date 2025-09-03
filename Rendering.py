import matplotlib.pyplot as plt
from BruteForce import BruteForceSolution
from random import randint

points = [[randint(0, 1000), randint(0, 1000)] for _ in range(10)]

distance, route = BruteForceSolution(points)

def plotRoute(route, title="TSP Route"):
    x = [p[0] for p in route] + [route[0][0]]
    y = [p[1] for p in route] + [route[0][1]]

    plt.figure(figsize=(10,10))
    plt.plot(x, y, c="blue", linewidth=2, marker="o", label="Route")

    for i, (px, py) in enumerate(route):
        plt.text(px+10, py+10, str(i), fontsize=12, color="red")

    plt.title(title)
    plt.legend()
    plt.show()

plotRoute(route, title=f"Brute Force TSP (Distance={distance:.2f})")

print("Best route:", route)
print("Distance:", distance)
