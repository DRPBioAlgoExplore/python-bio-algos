# Table of Contents
- [Hill Climbing](#hillclimbing)
- [Predator Prey \[Coming Soon\]](#predprey)

<div id='hillclimbing'/>

## Hill Climbing Challenge
In `hillclimbing.py` there are a couple functions that have various local maxima.
The challenge, however, is to find a global maximum within a region.

Some terminology:
- Objective function (fitness function): the function

#### Tasks
1. **(NEW)** Write a particle swarm optimizer for the hill climbing challenge.
    - Should accept an initial population of points, an objective (fitness) function to maximize, constraints on the domain, and a number of iteration to run.
    - Ideas for data to report: for every time step, record the global maximum found by the swarm so far, the average fitness of the swarm, the location of the best value so far, the centroid of the swarm.
    - Graph or display the data you report to see what is happening.
    - Experiment with parameters for the system:
        - Number of particles
        - Distribution of random numbers
        - etc.
    - See Recommended Readings.
2. **(NEW)** Write a genetic algorithm to find a global maximum.
    - Identify what "organisms" are in this context.
    - Determine what data structure will be useful for encoding this organism's "genome".
    - Pick a method for selecting the surviving population that will make it to the next round of evaluation.
    - Decide how reproduction will occur, using mutations and crossover (optional).
    - See Recommended Readings.

#### Recommended Reading
*Biologically Inspired Optimization Methods: An Introduction* (in the Dropbox)
 - Chapter 3, pgs. 40-59 (can skip the 'Biological Background' if somewhat familiar, stop at 'Properties of Genetic algorithms')
 - Chapter 5, pgs. 120-129 (info for optimization scheme starts in 5.2)


<div id='predprey'/>

## Predator Prey Challenge

**(COMING SOON)**
