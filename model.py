# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:47:39 2020

@author: katie
"""


import random
import operator
import matplotlib.pyplot

# Set parameters.
num_of_agents = 10
num_of_iterations = 100

agents = []

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents.append([random.randint(0,99),random.randint(0,99)])
        print(agents)

# Make agents move a step.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.randint(0, 99) < 0.5:
            agents[i][0] += 1
        else:
            agents[i][0] -= 1
            print(agents)

# Print the x, y locations.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        print("agents[" + str(i) + "] y =", agents[i][0], "x =", agents[i][1])

# Put the locations on a graph.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])

# Show the locations on a graph.
matplotlib.pyplot.show()









# matplotlib.pyplot.ylim(0, 99)
# matplotlib.pyplot.xlim(0, 99)
# matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
# matplotlib.pyplot.show()
      



# Print max y coordinate.
# print(max(agents))

# Print max x coordinate.
# print(max(agents, key=operator.itemgetter(1)))

# Work out pythagorian distance.
# y_diff = (agents[0][0]-agents[1][0])
# y_diffsq = y_diff*y_diff

# x_diff = (agents[0][1]-agents[1][1])
# x_diffsq = x_diff*x_diff

# sum = y_diffsq + x_diffsq

# answer = sum**0.5

# print (answer)

