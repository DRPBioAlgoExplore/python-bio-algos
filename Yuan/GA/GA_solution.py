import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 10 # number of cities
m = 15 # number of population

# Generate cities
City = np.random.rand(n, 2)
for c in City:
    x1 = c[0]
    y1 = c[1]
           
    plt.plot(x1, y1, 'go--', markersize=5)

plt.show()


# Generate initial population
P = np.mgrid[0:m, 0:n][1]

for p in P:
    x = []
    y = []
    np.random.shuffle(p)
  
    for i in range(n):
        x.append(City[p[i]][0])
        y.append(City[p[i]][1])
        
    plt.plot(x, y, alpha = 0.2)
plt.show()
    
    
def distance(P):
    D = []
    for p in P:
        d = 0
        
        for i in range(n-1):
            d += np.linalg.norm(City[p[i+1]]-City[p[i]])
            
        D.append(d)
    return np.array(D)


def score(D):
    s = []
    for d in D:
        a = math.exp(-d)
        s.append(a)
        
    return np.array(s)

# Reproduction Methods
# 1. transposition
def mutation1(p):
    i = np.random.randint(0, n-1)
    
    a = p[i]
    b = p[i+1]
    p2 = p
    p2[i+1] = a
    p2[i] = b
    return p2

# 2. shuffle
def mutation2(p):
    i = np.random.randint(0, n-3)
    
    np.random.shuffle(p[i:i+3])
    return p
    
    

# Selection Methods
# 1. Roulette Wheel
def rw(S):
    a = np.random.uniform(0, sum(S))
    index = 0
    for b in S:
        a -= b
        if a <= 0:
            return index
        
        else:
            index += 1
            
# 2. Tournament

   

    

def reproduction(P):
    P2 = []
    for i in range(m):
        j = np.random.randint(0, m)
        k = np.random.rand()
        
        if k <= 0.05:
            p2 = mutation1(P[j])
                
        if 0.05 < k <= 0.1:
            p2 = mutation2(P[j])
                
        else:
            p2 = P[j]
                
        P2.append(p2)
        P2.append(P[i])
    return P2


def select(P2, S):
    P3 = P
    for i in range(m):
        P3[i] = P2[rw(S)]
        
    return P3


def main(iter):
    D = []
    S = []
    for i in range(iter): # number of generations
        P2 = reproduction(P)        
        
        D2 = distance(P2)
        S2 = score(D2)
        P3 = select(P2, S2)
        d = distance(P3)
        s = score(d)
        D.append(d)
        S.append(s)
        
        for p in P3:
            x = []
            y = []
          
            for i in range(n):
                x.append(City[p[i]][0])
                y.append(City[p[i]][1])
                
            plt.plot(x, y, alpha = 0.2)
        plt.show()
    return (D, S)

iter = 100

R = main(iter)
D = R[0]
S = R[1]

X = np.arange(iter)

D_std = np.empty(iter)
D_mean = np.empty(iter)
S_std = np.empty(iter)
S_mean = np.empty(iter)

for i in range(iter):
    D_std[i] = np.std(D[i])
    D_mean[i] = np.mean(D[i])
    S_std[i] = np.std(S[i])
    S_mean[i] = np.mean(S[i])

plt.errorbar(X, D_mean, D_std)
plt.show()

plt.errorbar(X, S_mean, S_std)


plt.show()

main()
