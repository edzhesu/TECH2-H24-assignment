"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
x= [1,2,3,4,5]
def std_loops(x):
    
    mean_sum = 0
    count = 0
    
    # Calculate the mean
    for xi in x:
        mean_sum += xi
        count += 1
    
    mean = mean_sum / count
    
    variance_sum = 0
    
    
    for xi in x:
        variance_sum += (xi - mean) ** 2
    
    variance = variance_sum / count
    
    
    std_dev = variance ** 0.5  # Square root of variance
    
    # Print the standard deviation
    print(std_dev)
    
std_loops(x)

x= [1,2,3,4,5]
def std_builtin(x):
    import math
    sm=0
    for i in range(len(x)):
       sm+=x[i]
       
    mean = sm/len(x)
   
    deviation_sum = 0
    for i in range(len(x)):
       deviation_sum+=(x[i]- mean)**2
    psd = math.sqrt((deviation_sum)/len(x))
    print(psd)

    
std_builtin(x) 
 
import numpy as np
arr= [1,2,3,4,5]
print(np.std(arr, dtype = np.float64))
    