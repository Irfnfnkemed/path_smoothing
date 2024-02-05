import numpy as np
from matplotlib import pyplot as plt

from Interaction import Interaction


class Bezier_Curve:
    def __init__(self, point_number=20, ax_range=50):
        self.fig = None
        self.ax = None
        self.point_list = None
        self.ax_range = ax_range
        self.interaction = Interaction(point_number, ax_range)

    def set(self):
        self.interaction.set()

    def fit_curve(self):
        self.point_list = self.interaction.get()
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, self.ax_range)
        self.ax.set_ylim(0, self.ax_range)
        plt.gca().set_aspect('equal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Bezier Curve')
        plt.grid(True)
        for i in range(int(len(self.point_list) / 3)):
            self.ax.scatter(self.point_list[3 * i + 2][0], self.point_list[3 * i + 2][1], s=5)
            self.ax.text(self.point_list[3 * i + 2][0], self.point_list[3 * i + 2][1] + self.ax_range / 50, str(i + 1), ha='center')
            self.ax.scatter(self.point_list[3 * i][0], self.point_list[3 * i][1], s=3)
            self.ax.scatter(self.point_list[3 * i + 1][0], self.point_list[3 * i + 1][1], s=3)
            self.ax.plot([self.point_list[3 * i][0], self.point_list[3 * i + 1][0]], [self.point_list[3 * i][1], self.point_list[3 * i + 1][1]], linestyle='dashed', linewidth=1)
        for i in range(int(len(self.point_list) / 3) - 1):
            self.piecewise_fitting(3 * i + 2, 3 * i + 1, 3 * i + 3, 3 * i + 5)
        plt.show()

    def piecewise_fitting(self, i0, i1, i2, i3):
        cofactor = np.array([self.point_list[i0], self.point_list[i1], self.point_list[i2], self.point_list[i3]])
        t_values = np.linspace(0, 1, 100)
        points = []
        for t in t_values:
            T = np.array([((1 - t) ** 3), 3 * t * ((1 - t) ** 2), 3 * (t ** 2) * (1 - t), (t ** 3)])
            point = np.dot(T, cofactor)
            points.append(point)
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        plt.plot(x, y, color="red")
