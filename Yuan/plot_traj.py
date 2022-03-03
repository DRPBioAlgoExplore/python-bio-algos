import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import csv

class point():
    def __init__(self, l):
        self.loc = l
        self.v = np.random.randn(2)
        self.l_max = self
        self.g_max = self
        self.acc = 0
        self.val = fun(l)
    
       
    
    def move(self, time_step, s, a1, t):
        l = self.l_max.loc - self.loc
        g = self.g_max.loc - self.loc
        
        
        l = 2 * np.random.rand() * l
         
        g = 2 * np.random.rand() * g
        self.v = a1 * self.v + (1-a1)* (l + g)  
      
        loc = self.loc + self.v * time_step
        
            
        self.loc = Check_Constraints(loc)
        self.val = fun(self.loc)
        
        return self
        
    
def fun(p):
    x = p[0]
    y = p[1]
    return (x*y+.5*(1-x)*y)*np.sin(3*np.pi*x)*np.sin(3*np.pi*y)

def Generate_init(n):
    np.random.seed()
    list_of_points = np.random.rand(n,2)
    l = []
    for p in list_of_points:
        l.append(point(p))

    return l

    
def Check_Constraints(p):
    i = 0
    while i < 2:
        if p[i] > 1:
            p[i] = 1

        if p[i] < 0:
            p[i] = 0
        i = i + 1
    return p

def Find_globalmax(points):
    g_max = points[0].g_max
    m = g_max.val
    
    for p in points:
        
       
        if p.l_max.val > m:
            m = p.l_max.val
            g_max = p.l_max
            
    
    
    return g_max


def Find_lmax(p, s):
    c = p.loc
    v = p.val
    b = p
    if p.val > p.l_max.val:
        p.l_max = b
                
    return p.l_max


def main(n):
    points = Generate_init(50)
    
    g = Find_globalmax(points)
    X = []
    Y = []
    for p in points:
        X.append([])
        Y.append([])
    for i in range(500):
        
        
        for j in range(50):
            p = points[j]
            l = p.loc
            X[j-1].append(l[0])
            Y[j-1].append(l[1])
            
       
        for p in points:
            p.l_max = Find_lmax(p, A)
            
            
        p2 = Find_globalmax(points)
        t = 1
        for p in points:
            p.g_max = p2
            p = p.move(ts, A, n, t)
            t = t + 1
            
   
      
    return (X, Y)

A = 0.00001
ts = 0.1


for i in range(1):
    
    B = main(0.9)
    x = B[0]
    y = B[1]
    for j in range(20):
        x1 = x[j]
        y1 = y[j]
               
        plt.plot(x1, y1)

    plt.show