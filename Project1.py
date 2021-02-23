# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:00:04 2021

@author: pooja
"""

from helpers import matrix_to_lst, get_path
from queue_ll import Queue
import copy


def main():
    
    begin = [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]
           
    
    end = [[ 1, 2, 3, 4], 
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 0]]
    
    # call to bfs
    bfs(begin,end) 
    
    return None




def bfs(start,goal):
    # dimension of the square puzzle
    n = len(start)
    
    # offsets for movements in the list
    offsets = {
    "right": 1,
    "left": -1,
    "up": -n,
    "down": n
    }

    # converting matrix to string
    start_state = "".join(matrix_to_lst(start))
    goal_state = "".join(matrix_to_lst(goal))
    
    queue = Queue()
    queue.enqueue(start_state)
    predecessors = {start_state: None}
    
    
    while not queue.is_empty():
        
        # pop off first state in the queue
        current_state = queue.dequeue()
        
        # check if it is the goal itself
        if current_state == goal_state:
            return get_path(predecessors, start_state, goal_state)
    
        
        current_state_lst = list(current_state)  # convert string to list, because swap is not possible on strings(immutable)
        blank_pos = current_state_lst.index('A') # find position of blank tile
        
        
        for direction in ["up", "right", "down", "left"]:
            current_copy = copy.deepcopy(current_state_lst) # deepcopy to protect current_state_lst itself from modification
            new_blank_pos = blank_pos + offsets[direction]
            
            if new_blank_pos >= 0 and new_blank_pos < n**2 : # check for valid location before swapping tile
                current_copy[blank_pos], current_copy[new_blank_pos] = current_copy[new_blank_pos], current_copy[blank_pos] # swap operation
                neighbour = "".join(current_copy) # convert to string
                            
            else: 
                continue # if invalid location, continue to next direction
            
            
            if neighbour not in predecessors: 
                queue.enqueue(neighbour) # add neighbour to exploration queue
                predecessors[neighbour] = current_state # add neighbour to the parent-child dictionary for backtracking

    return None
    
    
if __name__ == "__main__":
    main()