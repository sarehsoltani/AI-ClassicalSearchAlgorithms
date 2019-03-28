from __future__ import print_function
from SearchAlgorithms.ClassicSearchAlgorithms import *
from copy import deepcopy

class Problem():
    def initialState(self):
        #initial_state = [1,1,1,1,1,1,1,1,1]  #on the left side or river
        initial_state = []
        for i in range(0,9):
            initial_state.append(1)
        print("initial state: ",initial_state)
        return initial_state

    def goal(self):
        goal = []
        for i in range(0,9):
            goal.append(0)
        return goal

    def isGoalTest(self,state):
        if(state == self.goal()):
            return True
        else:
            return False

    def actions(self, state):
        actions = []
        temp_state = deepcopy(state)
        boat = 0
        person1 = 0
        person2 = 0
        movement = []
        if(temp_state[8] == 0):
            boat = 0 # boat on the right side
        else:
            boat = 1 # boat on the left side
        for i in range(0, 8):
            if(person1 <= 6):   
                if(temp_state[person1] == boat and temp_state[person1 + 1] == boat):
                    person2 = person1 + 1    
                    movement = (person1, person2)
                    actions.append(movement)
            person1 = i + 2
            if(i <= 5):
                if(temp_state[i] == boat and temp_state[i + 2] == boat):
                    person2 = i + 2
                    movement = (i, person2)
                    actions.append(movement)
            if(i <= 3):
                if(temp_state[i] == boat and temp_state[i + 4] == boat):
                    person2 = i + 4
                    movement = (i, person2)
                    actions.append(movement)
            if(i <= 1):
                if(temp_state[i] == boat and temp_state[i + 6] == boat):
                    person2 = i + 6
                    movement = (i, person2)
                    actions.append(movement)
            if(temp_state[i] == boat):
                movement = (i,0)
                actions.append(movement)
        return actions
    
    def results(self,actions,state):
        states = []
        res = ""
        state = list(state)
        temp_state = deepcopy(state)
        for action in actions:
           if(temp_state[8]==1):
               temp_state[action[0]] = 0
               res = res + str(action[0])
               if(action[1] != 0):
                   temp_state[action[1]] = 0
                   res = res +str(action[1])            
               temp_state[8] = 0
               res = res + " RB"
           else:
               temp_state[action[0]] = 1
               if(action[1] != 0):
                   temp_state[action[1]] = 1 
               temp_state[8] = 1            
           states.append(temp_state)
        return states

    def print_path(self, path):
        print("Steps: ")
        
    def step_cost(self, current_state, next_state):
        return 1


p = Problem()  
csa = ClassicSearchAlgorithm(p)

if __name__ =='__main__':
    
        print("search strategies:")
        print("\t(1) BFS")
        print("\t(2) DFS")
        selection = int(input("Select the search strategy you would like to use: "))
        if(selection==1):
           csa.TBFS(p.initialState())                             
        elif(selection==2):
           csa.tree_depth_first_search(p.initialState()) 
        else:
            print("invalid selection")
            sys.exit()
