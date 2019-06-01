
# coding: utf-8

# In[10]:


#Discrete Time Markov Chain Model + Visualization - iGEM 2019 
#Zachary Manesiotis 

import numpy as np 
import matplotlib.pyplot as plt
from math import * 

P = np.array([[0.8, 0.1, 0.1], [0.5, 0.3, 0.2], [0.3, 0.2, 0.5]]) #transition matrix of probability distribution 
S_t = np.array([0.3, 0.5, 0.2]) #initial state vector 
sol = S_t
for i in range(1000): #reach steady state after long time
    sol = np.matmul(sol, P) 
    plt.plot(sol)

print(sol)
plt.xlabel("Time")
plt.ylabel("Probability")
plt.show() 


'''
Enzyme pathway: indole-3-acetic acid pathway (creates auxin, IAAH and IAAM are the two enzymes that are attatched to the TALs) 
'''

