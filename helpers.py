# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:38:29 2021

@author: pooja
"""
import numpy as np
import sys

def matrix_to_lst(mat):    
    
    # converting to 1D list 
    flatlist = np.array(mat).reshape(-1) 
    
    # replacement dictionary
    repl = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P'}
    
    # forming the character list
    result =[repl[item] for item in flatlist]
    
    return result



def get_path(predecessors, start, goal):
    current = goal # current node is goal
    path = []
    while current != start: # continue this loop till start node, because it has no parent
        path.append(current) # append current node to path
        current = predecessors[current] # make its parent the current node
    path.append(start)
    path.reverse() 
    
    print_path(path)
    return None



def print_path(path):
    
    
    # replacement dictionary to print path
    print_repl = {'A': 0 , 'B': 1,'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15}
    # Save a reference to the original standard output
    original_stdout = sys.stdout 
    with open('bfs.txt', 'w') as f:
        # Change the standard output to the file we created.
        sys.stdout = f 
        
        for step in path:
            
            letterlist = list(step) # convert string to list 
            numlist = np.array([print_repl[item] for item in letterlist]) # map letters to numbers, convert list to numpy array
            nummat = numlist.reshape(4,4) # convert the numpy array to matrix
            print(nummat) 
            print() 
        # Reset the standard output to its original value  
        sys.stdout = original_stdout 
        
    return None
        
        
        
