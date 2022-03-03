import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import csv

class point():
    def __init__(self, l):
        self.loc = l
        self.v = np.random.rand(2)
        self.l_max = self
        self.g_max = self
        self.acc = 0
        self.val = fun(l)
    
       
    
    def move(self, time_step, s, a1, t):
        l = self.l_max.loc - self.loc
        g = self.g_max.loc - self.loc
        
        
        l = 2 * np.random.rand() * l
         
        g = 2 * np.random.rand() * g
        self.v = a1 * self.v + l + g  
      
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
    for i in range(3):
        for j in range(3):
            x = c[0] + (i - 1) * s
            y = c[1] + (j - 1) * s
            p1 = np.array([x, y])
            Check_Constraints(p1)
            v1 = fun(p1)
            
            if v1 > v:
                v = v1
                b = point(p1)
               
    p.l_max = b
                
    return p.l_max



def main(n):
    points = Generate_init(20)
    
    g = Find_globalmax(points)
    
    L = np.empty(shape = (20, 200))
    
    G = np.empty(shape = (20, 200))
    EL = np.empty(200)
    EG = np.empty(200)
   
    
    ML = np.empty(200)
    MG = np.empty(200)
    for i in range(200):
        
        
        
        for j in range(20):
            p = points[j]
            l = p.loc
            
            lm = p.l_max.val
            gm = p.g_max.val
            
            L[j][i] = lm
            G[j][i] = gm
            
            
        EL[i] = np.std(L[:, i])
        EG[i] = np.std(G[:, i])
        ML[i] = np.mean(L[:, i])
        MG[i] = np.mean(G[:, i])
        
        for p in points:
            p.l_max = Find_lmax(p, A)
            
            
        p2 = Find_globalmax(points)
        t = 1
        for p in points:
            p.g_max = p2
            p = p.move(ts, A, n, t)
            t = t + 1
     
            
      
    return (EL, EG, ML, MG)


ts = 0.1
A = 0

B = main(0.5)

EL = B[0][:50]
EG = B[1][:50]
ML = B[2][:50]
MG = B[3][:50]
        
x = np.arange(50)


plt.errorbar(x, ML, EL, marker='.')
plt.errorbar(x, MG, EG, marker= '.')


plt.show()

# =============================================================================
# EL = B[0]
# EG = B[1]
# ML = B[2]
# MG = B[3]  
#         
# x = np.arange(200)
# 
# 
# 
# 
# plt.errorbar(x, ML, EL, linestyle='None', marker='^')
# plt.errorbar(x, MG, EG, linestyle='None', marker='^')
# 
# 
# plt.show()
# 
# =============================================================================
