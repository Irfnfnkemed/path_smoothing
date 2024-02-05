from Catmull_Rom import Catmull_Rom

point_number = 20
ax_range = 50
alpha = 0.5

curve = Catmull_Rom(point_number, ax_range, alpha)
curve.set()
curve.fit_curve()
