# Tait Weicht, 2022
# A module with a classic hills and valleys optimization problem.
# Use
#   import sys
#   sys.path.append('<this directory's name>')
#   import fivepeaks
# to import it!
#
# Goal: find the maximum!

import numpy as np

# Find the maximum in the square [0,1]x[0,1].
# There are 5 peaks, 4 valleys!
def fivepeaks(x, y):
  return (x*y+.5*(1-x)*y)*np.sin(3*np.pi*x)*np.sin(3*np.pi*y)

# Find the maximum in this terrain
def ravine(x, y):
  return (1-x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

def rosenbrock(x, y):
  return 20-(1-x**2)-2*(y-x**2)**2
