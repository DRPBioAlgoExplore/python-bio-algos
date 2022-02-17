# The solution initiates with an initial population P; an objective 
# function f; (constraints [c_1, c_2, ...]); and maximum iterations N_0.

import random
import numpy as np

class Point:
    def __init__(self, location, l_max, g_max):
        self.loc = location
        self.l_max = l_max
        self.g_max = g_max

    def move(self): 
        
        
        l = self.l_max - self.loc
        g = self.g_max - self.loc
        v = self.loc

        for i in range(2):
            l[i] = 2 * np.random.rand() * l[i]
            
            g[i] = 2 * np.random.rand() * g[i]
            
            v[i] = v[i] + l[i] + g[i]
            
        v = Check_Constraints(v)
            
        return v


def fun(p):
    x = p[0]
    y = p[1]
    return (x*y+.5*(1-x)*y)*np.sin(3*np.pi*x)*np.sin(3*np.pi*y)


def Generate_init(n):
    list_of_points = np.random.rand(n,2)

    return list_of_points


def Find_Global_Max(list_of_points):
    m = fun(list_of_points[0])
    pt = 0
    for p in list_of_points:
        a = Find_Max(p)
        if a[0] > m:
            m = a[0]
            pt = a[1]

    return (m, pt)

def Find_Max(current_place): 
    # Takes a point, and check for the values 0.0000005 away from that point.
    # update maximun values and max place along the way
    # return max value amd max place

    c = current_place
    i = len(current_place)
    max_place = current_place
    max_val = fun(current_place)

    while i > 0:
        for j in range(3):
            c[i - 1] = c[i - 1] + (j-1) / 1e-06
            
            c = Check_Constraints(c)
            
            if fun(c) > max_val:
                    max_val = fun(c)
                    max_place = c    

        i -= 1
        
    return (max_val,  max_place)


def Check_Constraints(p):
    i = 0
    while i < 2:
        if p[i] > 1:
            p[i] = 1

        if p[i] < 0:
            p[i] = 0
        i = i + 1
    return p


def main():
    points = Generate_init(100)
    i = 0
    g = Find_Global_Max(points)
    for i in range(10):

        for p in points:
            l = Find_Max(p)
            
            p1 = Point(p, l[1], g[1])
            
            p = p1.move()
            
            g = Find_Global_Max(points)
            

        i = i + 1

    return g[0]


L = []
for i in range(1000):
    A = main()
    L.append(A)
    i = i-1

plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# Plot Histogram on x
x = L
plt.hist(x, bins=50)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');

