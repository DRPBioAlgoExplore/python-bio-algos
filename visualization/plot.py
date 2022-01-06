import matplotlib.pyplot as plt
import numpy as np

# Visualizes function via a heatmap (credit to https://stackoverflow.com/questions/33282368/plotting-a-2d-heatmap-with-matplotlib for heatmap code)
def heatmap(func, x_min, x_max, y_min, y_max):
  y, x = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
  z = func(x, y)
  z = z[:-1, :-1]
  z_max = np.abs(z).max()
  z_min = -z_max

  fig, ax = plt.subplots()
  c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
  fig.colorbar(c, ax=ax)
  return fig
