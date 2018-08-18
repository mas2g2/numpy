from statistics import mode
import numpy as np
from scipy import stats
import os as os
import sys

def calculate_mean(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list of float values")
        return
    else:
        return np.mean(array)

def get_median(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list of float values")
        return
    else:
        return np.median(array)

def find_mode(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list of float values")
        return
    else:
        try:
            mod = mode(array)
        except:
            mod = "No mode"
        return mod

def standard_deviation(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list")
        return
    else:
        return np.std(array)

def variance(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list")
        return
    else:
        return np.var(array)

def sorted_dataset(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list")
        return
    else:
        array.sort()
        return array
def update_mean(prev_mean,array,new_item):
    if isinstance(prev_mean,float) == False:
        print("First parameter needs to be a float value")
    elif isinstance(array,list) == False:
        print("Second parameter needs to be a list")
    elif isinstance(new_item,float) == False:
        print("Last parameter needs to be a float value")
    else:
        total = prev_mean*len(array) + new_item
        array.append(new_item)
        new_mean = total/len(array)
    return new_mean


arg = sys.argv[1:]
array = list()
array_2 = list()
new_list = 0
for i in arg:
    
    if new_list == 0 and i != '/':
        array.append(float(i))
    elif i == '/':
        new_list = 1
    else:
        array_2.append(float(i))

mean = str(calculate_mean(array))

data_analysis_string = ' {\n'+'\t"Data" : '+'"'+str(array)+'",\n'+'\t"Mean" : '+'"'+mean+'",\n'+'\t"Median" : '+'"'+str(get_median(array))+'",\n'+'\t"Mode" : '+'"'+str(find_mode(array))+'",\n'+'\t"Standard Deviation" : '+'"'+str(standard_deviation(array))+'",\n'+'\t"Variance" : '+'"'+str(variance(array))+'",\n'+'\t"Sorted Dataset" : '+'"'+str(sorted_dataset(array))+'",\n'+'\t"Sum" : '+'"'+str(sum(array))+'",\n'+'\t"Number of items" : '+'"'+str(len(array))+'"\n'+'}'
print(data_analysis_string)

from scipy.stats import linregress
if array_2:
    data_analysis_string = ' {\n'+'\t"Data" : '+'"'+str(array_2)+'",\n'+'\t"Mean" : '+'"'+str(calculate_mean(array_2))+'",\n'+'\t"Median" : '+'"'+str(get_median(array_2))+'",\n'+'\t"Mode" : '+'"'+str(find_mode(array_2))+'",\n'+'\t"Standard Deviation" : '+'"'+str(standard_deviation(array_2))+'",\n'+'\t"Variance" : '+'"'+str(variance(array_2))+'",\n'+'\t"Sorted Dataset" : '+'"'+str(sorted_dataset(array_2))+'",\n'+'\t"Sum" : '+'"'+str(sum(array_2))+'",\n'+'\t"Number of items" : '+'"'+str(len(array_2))+'"\n'+'}'
    print(data_analysis_string)
if new_list == 1:
    slope,intercept,corr,p_val,std = linregress(array,array_2)
    linear_regression = '{\n"slope" : "'+str(slope)+'", "intercept" : "'+str(intercept)+'", "correlation coefficient" : "'+str(corr)+'", "p-value" : "'+str(p_val)+'", "standard deviation" : "'+str(std)+'" }'
    print(linear_regression)
