# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 01:07:09 2020

@author: Dell
"""

class State:
    
    def __init__(self, mis, can, boat, parent):
        self.mis = mis
        self.can = can
        self.boat = boat
        self.parent = parent
        self.children = []
    
    def print_fun(self):
        print('Missionaries:', self.mis, 'Cannibals:', self.can)
    
    def Goal(self):
        if self.mis == 0 and self.can == 0 and self.boat == False:
            return True
        return False
    
    def createChildren(self):
        if self.boat:
            can = 4
            for mis in range(5):
                if (self.mis - int(mis/2)) >= 0 and (self.can - int(can/2)) >= 0:
                    if ((self.mis - int(mis/2)) == (self.can - int(can/2))) or (self.mis - int(mis/2)) == 0 or (self.mis - int(mis/2)) == 3:
                        self.children.append(State((self.mis - int(mis/2)), (self.can - int(can/2)), False, self))
                can -= 1
        else:
            can = 4
            for mis in range(5):
                if (self.mis + int(mis/2)) <= 3 and (self.can + int(can/2)) <= 3:
                    if ((self.mis + int(mis/2)) == (self.can + int(can/2))) or (self.mis + int(mis/2)) == 3 or (self.mis + int(mis/2)) == 0:
                        self.children.append(State((self.mis + int(mis/2)), (self.can + int(can/2)), True, self))
                can -= 1

def BFS(head):
    queue = []
    visited = []    
    queue.append(head)
    visited.append([head.mis, head.can, head.boat])
    while queue:
        cur = queue.pop(0)
        
        if cur.Goal():
            return cur
        cur.createChildren()
        for child in cur.children:
            tmp = [child.mis, child.can, child.boat]
            if tmp not in visited:
                queue.append(child)
                visited.append(tmp)

def getParents(solution):
    path = []
    path.append(solution)
    state = solution.parent
    while state:
        path.insert(0, state)
        state = state.parent
    return path

def __main__():
    head = State(3, 3, True, None)
    solution = BFS(head)
    path = getParents(solution)

    if path is not None:
        for state in path:
            state.print_fun()
    else:
        print('No solution found')
        
if __name__ == "__main__":
    __main__()