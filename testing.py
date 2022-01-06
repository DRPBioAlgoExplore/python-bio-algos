import sys
import matplotlib.pyplot as plt
sys.path.append('problems')
sys.path.append('visualization')
from hillclimbing import fivepeaks, ravine, rosenbrock
import plot


# fig = plot.heatmap(ravine, -3, 3, -3, 3)
# plt.show()

# fig = plot.heatmap(ravine, -3, 3, -3, 3)
# plt.show()

fig = plot.heatmap(rosenbrock, -1, 3, -2, 2)
plt.show()
