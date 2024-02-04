import numpy as np
from matplotlib import pyplot as plt

from interaction import Interaction

point_number = 20
ax_range = 50
alpha = 0.5
cal_matrix = np.array([[alpha, alpha - 2, 2 - alpha, -alpha],
                       [-alpha, 3 - 2 * alpha, alpha - 3, 2 * alpha],
                       [0, alpha, 0, -alpha],
                       [0, 0, 1, 0]])

interaction = Interaction(point_number, ax_range)
interaction.set()
point_list = interaction.get()
fig, ax = plt.subplots()
ax.set_xlim(0, ax_range)
ax.set_ylim(0, ax_range)
plt.gca().set_aspect('equal')


def fitting(P0, P1, P2, P3):
    cofactor = np.dot(cal_matrix, np.array([P0, P1, P2, P3]))
    t_values = np.linspace(0, 1, 100)
    points = []
    for t in t_values:
        T = np.array([t ** 3, t ** 2, t, 1])
        point = np.dot(T, cofactor)
        points.append(point)
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x, y, color="red")


for i in range(len(point_list)):
    #ax.scatter(point_list[i][0], point_list[i][1], s=5)
    ax.text(point_list[i][0], point_list[i][1] + ax_range / 50, str(i + 1), ha='center')

for i in range(len(point_list) - 1):
    if i == 0:
        fitting(point_list[0], point_list[0], point_list[1], point_list[2])
    elif i == len(point_list) - 2:
        fitting(point_list[i - 1], point_list[i], point_list[i + 1], point_list[i + 1])
    else:
        fitting(point_list[i - 1], point_list[i], point_list[i + 1], point_list[i + 2])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Function')
plt.grid(True)
plt.show()
