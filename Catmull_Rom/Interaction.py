from matplotlib import pyplot as plt


class Interaction:
    def __init__(self, num=10, ax_range=50):
        self.point_list = []
        self.fig, self.ax = plt.subplots()
        self.ax_range = ax_range
        self.ax.set_xlim(0, ax_range)
        self.ax.set_ylim(0, ax_range)
        plt.gca().set_aspect('equal')
        self.remind = self.ax.text(0.0, -self.ax_range / 10, "Click the mouse to confirm " + str(num) + " more points.")
        self.tar_num = num
        self.now_num = 0

    def set(self):
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        plt.grid(True)
        plt.show()

    def get(self):
        return self.point_list

    def on_click(self, event):
        if event.xdata is not None and event.ydata is not None:
            self.now_num += 1
            self.remind.remove()
            self.remind = self.ax.text(0.0, -5.0, "Click the mouse to confirm " + str(self.tar_num - self.now_num) + " more points.")
            self.point_list.append((event.xdata, event.ydata))
            self.draw_point(event.xdata, event.ydata)
            if self.now_num == self.tar_num:
                plt.close('all')

    def draw_point(self, pos_x, pos_y):
        self.ax.scatter(pos_x, pos_y, s=10)
        self.ax.text(pos_x, pos_y + self.ax_range / 50, str(self.now_num), ha='center')
        plt.draw()
