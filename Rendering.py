import matplotlib.pyplot as plt
import matplotlib.animation as animation
from BruteForce import BruteForceSolution
from random import randint
print("Testing")
points = [[randint(0, 1000), randint(0, 1000)] for i in range(10)]

distance, route = BruteForceSolution(points)

def animateRoute(route, distance, title="Animated TSP Route"):
    x = [p[0] for p in route] + [route[0][0]]
    y = [p[1] for p in route] + [route[0][1]]

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.scatter([p[0] for p in route], [p[1] for p in route], c="red", s=100, label="Points")

    start = route[0]
    ax.scatter(start[0], start[1], c="green", s=150, zorder=3, label="Start")
    ax.text(start[0] + 10, start[1] + 10, "Start", fontsize=12, color="green", weight="bold")

    for i, (px, py) in enumerate(route[1:], start=1):
        ax.text(px + 10, py + 10, str(i), fontsize=12, color="red")

    line, = ax.plot([], [], c="blue", linewidth=2, marker="o", label="Route")

    ax.set_title(f"{title} (Distance={distance:.2f})")
    ax.legend()

    def update(num):
        line.set_data(x[:num+1], y[:num+1])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(x), interval=800, blit=True, repeat=False)
    plt.show()

animateRoute(route, distance)
print("Best route:", route)

