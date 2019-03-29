from __future__ import print_function
from SearchAlgorithms.ClassicSearchAlgorithms import *
from copy import deepcopy
import numpy as np
import sys

class Problem():
    chess= [
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0],
        [0,-1,0,0,0,0,0,0],
        [0,0,0,0,0,-1,0,0],
        [0,0,0,-1,0,0,0,0],
        [0,0,0,0,-1,0,0,0],
        [2,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,0]
        ]        
    for row in chess:
        for col in row:
            if col == 1:
                initial_state = (chess.index(row), row.index(col))
    wall = []
    for row in chess:
        for col in row:
            if col == -1:
                sare = (chess.index(row),row.index(col)) 
                wall.append(sare)
    
    def initialState(self):    
        return (0,5)    
    
    goals = []    
    def goal(self): 
       for row in self.chess:
        for col in row:
          if col == 2:
             g = (self.chess.index(row),row.index(col)) 
             self.goals.append(g)
       return self.goals 

    def isGoalTest(self, state):
        if state in self.goal():
            return True
        else:
            return False
       
    def actions(self,state): 
       actions = []
       agent_row = state[0]
       agent_col = state[1]
       g1_row = self.goals[0][0]
       g1_col = self.goals[0][1]
       g2_row = self.goals[1][0]
       g2_col = self.goals[1][1]   
       if agent_row > 1 :
            up = (agent_row-1,agent_col)
            if up not in self.wall:
                actions.append('U')
       if agent_row < g1_row or agent_row < g2_row :
            down = (agent_row + 1, agent_col)
            if down not in self.wall:
                actions.append('D') 
       if agent_col > 1:
            left = (agent_row, agent_col-1)
            if left not in self.wall: 
                actions.append('L')
       if agent_col < g1_col or agent_col < g2_col:
            right = (agent_row,agent_col+1)
            if right not in self.wall:      
                actions.append('R')
       return actions
    
    def results(self,actions,state):
        states = []
        for action in actions:
            next_state = deepcopy(state)
            next_state = list(next_state)
            state = list(state)
            if 'U' in action:
                next_state[0] = next_state[0] - 1
            elif 'D' in action:
                next_state[0] = next_state[0] + 1
            elif 'L' in action:             
                next_state[1] = next_state[1] - 1
            elif 'R' in action:
                next_state[1] = next_state[1] + 1
            states.append(tuple(next_state))
        return states

    def step_cost(self, current_state, next_state):
        return 1
    
    def print_path(self, path):
        def find_direction(current_state, next_state):
            if current_state[0] == next_state[0] and current_state[1] > next_state[1]:
                print("L", end=" ")
            elif current_state[0] == next_state[0] and current_state[1] < next_state[1]:
                print("R", end=" ")
            elif current_state[0] > next_state[0] and current_state[1] == next_state[1]:
                print("U", end=" ")
            elif current_state[0] < next_state[0] and current_state[1] == next_state[1]:
                print("D", end=" ")
        print("Path:")
        for current_state, next_state in zip(path, path[1:]):
            find_direction(current_state, next_state)
        print()

p = Problem()
SearchAlgorithms = ClassicSearchAlgorithm(p)
if __name__ =='__main__':
    while(True):
        print("search strategies:")
        print("\t(1) Graph DFS")
        print("\t(2) Graph BFS")
        print("\t(3) uniform cost") 
        selection = int(input("Select the search strategy you would like to use: "))
        if(selection==1):
            SearchAlgorithms.graph_depth_first_search(p.initialState())                             
        elif(selection==2):
            SearchAlgorithms.graph_breadth_first_search(p.initialState())         
        elif(selection==3):
            SearchAlgorithms.graph_uniform_cost_search(p.initialState())                           
        else:
            print("invalid selection")
            sys.exit()