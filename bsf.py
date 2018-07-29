from statistics import mode
import numpy as np
from scipy import stats
import os as os
import sys
print(sys.argv[0])
print(len(sys.argv))
def calculate_mean(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list")
        return
    else:
        return np.mean(array)

def get_median(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list")
        return
    else:
        return np.median(array)

def find_mode(array):
    if isinstance(array,list) == False:
        print("First parameter needs to be a list")
        return
    else:
        mode = mode(array)
        return mode

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

array = list()

text_file = input("Enter a text file (*.txt) with only float values: ")
yes_or_no = input("Do you wish to enter another text file?(Enter 'yes' or 'no') ")
if yes_or_no == 'yes':
    try:
        text_file_2 = input("Enter a text file (*.txt) with only float values: ")
    except FileNotFoundError:
        print("Error: No such file or folder in this directory")
if os.path.getsize(text_file) > 0:
    try:
        with open(text_file,"r") as f1:
            for line in f1:
                array.append(float(line.strip()))
        mean = str(calculate_mean(array))
        print(array)
        data_analysis_string = ' {\n'+'\t"File" : '+'"'+text_file+'",\n'+'\t"Mean" : '+'"'+mean+'",\n'+'\t"Median" : '+'"'+str(get_median(array))+'",\n'+'\t"Mode" : '+'"'+str(find_mode(array))+'",\n'+'\t"Standard Deviation" : '+'"'+str(standard_deviation(array))+'",\n'+'\t"Variance" : '+'"'+str(variance(array))+'",\n'+'\t"Sorted Dataset" : '+'"'+str(sorted_dataset(array))+'",\n'+'\t"Sum" : '+'"'+str(sum(array))+'",\n'+'\t"Number of items" : '+'"'+str(len(array))+'"\n'+'}'
        print(data_analysis_string)
        new_file = input("Enter a JSON file(*.json) where you would like to enter updated information: ")
        analysis_data = 
        try:
            if os.path.getsize(new_file) > 0:
                print("Notify! Text file : '",new_file,"', is not empty.")
                output_file = open(new_file,"a")
                output_file.write(data_analysis_string)
                output_file.close()
            else:
                print("Warning! Text file: '",new_file,"', is empty.")
                output_file = open(new_file,"w")
                output_file.write(data_analysis_string)
                output_file.close()
        except FileNotFoundError:
            print("Creating new file ",new_file,"... ")
            output_file = open(new_file,"w+")
            output_file.write(data_analysis_string)
            output_file.close()
    except FileNotFoundError:
        print("ERR:File was not found in this directory.")
else:
    print("ERR:File is empty")
