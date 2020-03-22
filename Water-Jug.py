# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 12:07:09 2020

@author: Dell
"""

graph = {}
jug_1 = []
jug_2 = []
goal = []
jug_1_cap = 0
jug_2_cap = 0

class jug:
       
    def input_jug(self):
    
        jug_1_cap = int(input("Enter the capacity of Jug 1"))
        while jug_1_cap != 0:
            print("Invalid")
            jug_1_cap = int(input("Enter the capacity of Jug 1"))
        
        jug_2_cap = int(input("Enter the capacity of Jug 2"))
        while jug_2_cap != 0:
            print("Invalid")
            jug_2_cap = int(input("Enter the capacity of Jug 2"))
    
    def method(self):
        
        n = 3
        while n !=0:
            print("Choose the method :- \n" \
                  "1. DFS \n" \
                  "2. BFS")
            n = int(input("Enter the choice -"))
            if n == 1:
                self.dfs()
            elif n == 2:
                self.bfs()
            else:
                print("Invaild Input")
                break
    
    def dfs(self):
        n = int(input("Enter start node - "))
        visited = []
        jug_1_cap = [n]
        q = True
        while q:
            current_node = q.pop()
            if current_node not in visited:
                visited.append(current_node)
                neighbours = graph[current_node]
                for values in neighbours:
                    q.append(values)
            else:
                print("Unsucessful")
        print(visited)

    def bfs(head):
        queue = []
        visited = []    
        queue.append(head)
        visited.append([head.jug_1_cap, head.jug_2_cap, head.boat])
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

    def do_main(self):
        
        global jug1size
        jug1size = int(input("Jug 1 size:"))
        global jug2size
        jug2size = int(input("Jug 2 size:"))

        goalstate1 = input("Goal state jug 1:")
        goalstate2 = input("Goal state jug 2:")
        
        startstate = (0, 0)
        goalstate = (int(goalstate1), int(goalstate2))

        openlist = []
        openlist.append([startstate])

        print("Jug sizes: " + str(jug1size) + ", " + str(jug2size))
        print("Starting state: " + str(startstate))
        print("Goal state: " + str(goalstate))

        while(1):
            if len(openlist) == 0:
                print("No solution found")
                exit(0)
                curnode = openlist.pop(0)

        if curnode[-1] == goalstate:
            print("Found solution:")
            print(curnode)
            exit(0)

        openlist += S(curnode)

    def S(node):

        returnlist = []
        state = node[-1]
        jug1, jug2 = state


    def checkState(new_state, old_state):
        if new_state != old_state:
            if not new_state in node:
                new_node = node.copy()
                new_node.append(new_state)
                returnlist.append(new_node)
                
    slist = [(jug1, 0), (0, jug2), (jug1size, jug2), (jug1, jug2size),
             (jug1 - min(jug1, jug2size - jug2), jug2 + min(jug1, jug2size - jug2)),
             (jug1 + min(jug2, jug1size - jug1), jug2 - min(jug2, jug1size - jug1))]
    for s in slist:
        checkState(s, state)

    return returnlist

if __name__ == "__main__":
    print("Water jug problem solver")
    do_main()
    pass
    
j = jug()
j.method()