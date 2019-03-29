from __future__ import print_function
from SearchAlgorithms.ClassicSearchAlgorithms import *
from copy import deepcopy
import numpy as np

#********************************#
#                +---+---+---+   #
#                | 1 | 2 | 3 |   #
#                +---+---+---+   #
#   GOAL STATE:  | 4 | 5 | 6 |   #
#                +---+---+---+   #
#                | 7 | 8 |   |   #
#                +---+---+---+   #
#********************************#

def display(arr):
   return 'initial State\n' \
           '\t +---+---+---+\n' \
           '\t | %s | %s | %s |\n' \
           '\t +---+---+---+\n' \
           '\t | %s | %s | %s |\n' \
           '\t +---+---+---+\n' \
           '\t | %s | %s | %s |\n' \
           '\t +---+---+---+\n' \
           % (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])


def check_solubility(puzzle,n):
    #Calculating inversion
    inv_count = 0
    for i in range(n):
        for j in range(i+1,n):
            if(puzzle[i] > puzzle[j] and puzzle[i] != 0 and puzzle[j] != 0):
                inv_count = inv_count + 1
    print("Number of Inversion: ",inv_count)
    if(inv_count % 2 == 1):
       print("*** Oops:( No Solution for this board.***")
       exit()   
    else:
       print("*** Let's Go:) it's solvable ***")
        
class Problem(): 
    def initialState(self):
        # solvable examples: ((1,2,3),(6,4,0),(7,8,5)), ((1,2,5),(6,8,0),(7,4,3)), ((2,3,0),(1,6,8),(7,5,4)) 
        # un solvable examples: ((1,2,7),(4,5,6),(3,8,0)) with 7, ((8,1,2),(0,4,3),(7,6,5)) with 11
        initialstate = ((1,2,3),(4,5,6),(0,7,8))
        puzzle = np.hstack(initialstate)
        check_solubility(puzzle,len(puzzle))
        print(display(puzzle))
        return initialstate

    def goal(self):
        return ((1,2,3),(4,5,6),(7,8,0))
        
    def isGoalTest(self, state):
        return state == self.goal()
 
    def actions(self, state):
        emptySpot_row = -1
        emptySpot_col = -1
        actions = []
        for row in state:
            for col in row:
                if col == 0:
                    emptySpot_row = state.index(row)
                    emptySpot_col = row.index(col)
        if emptySpot_col > 0:
            actions.append('L')
        if emptySpot_col < 2:
            actions.append('R')
        if emptySpot_row > 0:
            actions.append('U')
        if emptySpot_row < 2:
            actions.append('D')
        return actions

    def results(self, actions, state):
        emptySpot_row  = -1
        emptySpot_col = -1
        states = []
        for row in state:
            for col in row:
                if col == 0:
                    emptySpot_row = state.index(row)
                    emptySpot_col = row.index(col)
        for action in actions:
            state = list(list(item) for item in state)
            temp_state = deepcopy(state)
            if 'U' in action:
                temp_state[emptySpot_row][emptySpot_col], temp_state[emptySpot_row - 1][emptySpot_col] = state[emptySpot_row - 1][emptySpot_col], \
                                                                                     state[emptySpot_row][emptySpot_col]
            if 'D' in action:
                temp_state[emptySpot_row][emptySpot_col], temp_state[emptySpot_row + 1][emptySpot_col] = state[emptySpot_row + 1][emptySpot_col], \
                                                                                     state[emptySpot_row][emptySpot_col]
            if 'L' in action:
                temp_state[emptySpot_row][emptySpot_col], temp_state[emptySpot_row][emptySpot_col - 1] = state[emptySpot_row][emptySpot_col - 1], \
                                                                                     state[emptySpot_row][emptySpot_col]
            if 'R' in action:
                temp_state[emptySpot_row][emptySpot_col], temp_state[emptySpot_row][emptySpot_col + 1] = state[emptySpot_row][emptySpot_col + 1], \
                                                                                     state[emptySpot_row][emptySpot_col]
            temp_state = tuple(tuple(item) for item in temp_state)
            states.append(temp_state)
        return states  

    def step_cost(self, current_state, next_state):
        return 1

    def heuristic(self, state):
        '''
        #best heuristic function    
        x = 0
        for i in range(0, 3):
            for j in range(0, 3):
                a = state[i][j] / 3
                b = state[i][j] % 3
                x += ((a-i)**2 + (b-j)**2)**(1/2.0)
        return x
        '''
        emptySpot_row = -1
        emptySpot_col = -1
        for row in state:
            for col in row:
                if col == 0:
                    emptySpot_row = state.index(row)
                    emptySpot_col = row.index(col)
        return emptySpot_col + emptySpot_row
        
    def print_path(self, path):
        def find_direction(current_state, next_state):
            current_emptySpot_row = -1
            current_emptySpot_col = -1
            for row in current_state:
                for col in row:
                    if col == 0:
                        current_emptySpot_row = current_state.index(row)
                        current_emptySpot_col = row.index(col)
            next_emptySpot_row = -1
            next_emptySpot_col = -1
            for row in next_state:
                for col in row:
                    if col == 0:
                        next_emptySpot_row = next_state.index(row)
                        next_emptySpot_col = row.index(col)
            if next_emptySpot_col == current_emptySpot_col and next_emptySpot_row > current_emptySpot_row:
                print('U', end=" ")
            if next_emptySpot_col == current_emptySpot_col and next_emptySpot_row < current_emptySpot_row:
                print('D', end=" ")
            if next_emptySpot_col > current_emptySpot_col and next_emptySpot_row == current_emptySpot_row:
                print('R', end=" ")
            if next_emptySpot_col < current_emptySpot_col and next_emptySpot_row == current_emptySpot_row:
                print('L', end=" ")
        
        print("Path:",end= " ")
        for current_state, next_state in zip(path, path[1:]):
            find_direction(current_state, next_state)
        print()

p = Problem()
csa = ClassicSearchAlgorithm(p)

if __name__ =='__main__':
    while(True):
        print("search strategies:")
        print("\t(1) uniform cost")
        print("\t(2) Graph BFS")
        print("\t(3) Graph A*")
        print("\t(4) Tree  A*")
        print("\t(5) Tree BFS")
        selection = int(input("Select the search strategy you would like to use: "))
        if(selection==1):
            csa.tree_uniform_cost_search(p.initialState())                         
        elif(selection==2):
            csa.graph_breadth_first_search(p.initialState())
        elif(selection==3):
            csa.graph_a_star(p.initialState())                    
        elif(selection==4):
            csa.tree_a_star(p.initialState()) 
        elif(selection==5):
             csa.TBFS(p.initialState())                 
        else:
            print("invalid selection")
            sys.exit()