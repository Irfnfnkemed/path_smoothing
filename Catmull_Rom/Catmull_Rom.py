import numpy as np
from matplotlib import pyplot as plt

from Interaction import Interaction


class Catmull_Rom:
    def __init__(self, point_number=20, ax_range=50, alpha=0.5):
        self.fig = None
        self.ax = None
        self.point_list = None
        self.ax_range = ax_range
        self.cal_matrix = np.array([[alpha, alpha - 2, 2 - alpha, -alpha],
                                    [-alpha, 3 - 2 * alpha, alpha - 3, 2 * alpha],
                                    [0, alpha, 0, -alpha],
                                    [0, 0, 1, 0]])
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
        plt.title('Catmull Rom')
        plt.grid(True)
        for i in range(len(self.point_list)):
            self.ax.scatter(self.point_list[i][0], self.point_list[i][1], s=5)
            self.ax.text(self.point_list[i][0], self.point_list[i][1] + self.ax_range / 50, str(i + 1), ha='center')
        for i in range(len(self.point_list) - 1):
            if i == 0:
                self.piecewise_fitting(0, 0, 1, 2)
            elif i == len(self.point_list) - 2:
                self.piecewise_fitting(i - 1, i, i + 1, i + 1)
            else:
                self.piecewise_fitting(i - 1, i, i + 1, i + 2)
        plt.show()

    def piecewise_fitting(self, i0, i1, i2, i3):
        cofactor = np.dot(self.cal_matrix, np.array([self.point_list[i0], self.point_list[i1], self.point_list[i2], self.point_list[i3]]))
        t_values = np.linspace(0, 1, 100)
        points = []
        for t in t_values:
            T = np.array([t ** 3, t ** 2, t, 1])
            point = np.dot(T, cofactor)
            points.append(point)
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        plt.plot(x, y, color="red")
