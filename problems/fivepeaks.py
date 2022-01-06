# Tait Weicht, 2022
# A module with a classic hills and valleys optimization problem.
# Use
#   import sys
#   sys.path.append('<this directory's name>')
#   import fivepeaks
# to import it!
#
# Goal: find the maximum in [0,1]x[0,1] for this function

from math import pi
import matplotlib.pyplot as plt
import numpy as np

# Find the height at a point
# (in a unit square [0,1]x[0,1] there are 5 peaks, 4 valleys)
def height(x, y):
  return (x*y+.5*(1-x)*y)*np.sin(3*np.pi*x)*np.sin(3*np.pi*y)

# Visualizes the terrain (credit to https://stackoverflow.com/questions/33282368/plotting-a-2d-heatmap-with-matplotlib for heatmap code)
def view():
  y, x = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
  z = eval(x, y)
  z = z[:-1, :-1]
  z_min, z_max = -np.abs(z).max(), np.abs(z).max()

  fig, ax = plt.subplots()
  c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
  fig.colorbar(c, ax=ax)

  plt.show()

print(eval())


