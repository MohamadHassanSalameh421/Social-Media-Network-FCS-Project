from collections import deque
class DiGraph(): #A directed graph, In this weighted Graph 0 means no connections

    def __init__(self):

        self.graph = []
        self.vertices = {}
    

    def add_user(self, user): #In here we add users to the social network
        if user not in self.vertices:

            self.vertices[user] = len(self.graph)

            for row in self.graph:
                row.append(0)

            self.graph.append([0] * (len(self.graph) + 1))
    


    def add_friends(self, user1, user2, distance=0): #We add friends with distances to user2 (user1 -> user2)
        if (user1 and user2) in self.vertices:

            self.graph[self.vertices[user1]][self.vertices[user2]] = distance



    def remove_friends(self, user1, user2):
        if (user1 and user2) in self.vertices:

            self.graph[self.vertices[user2]][self.vertices[user1]] = 0 #0 means no relationship between these two users
    
    

    def remove_user(self, user1):

        if user1 in self.vertices:

            del self.graph[self.vertices[user1]]

            for row in self.graph:
                row.pop()
            
            for k, v in self.vertices.items():
                if v > self.vertices[user1]:
                    self.vertices[k] = v - 1
                    
            del self.vertices[user1]
    


    def DFS(self, start):

        visited = set()
        i = self.vertices[start]

        def recursive_call(i, visited):
            for k, v in self.vertices.items():
                if v == i:
                    print(k)
                    print('|')

            visited.add(i)

            for r in range(len(self.graph)):
                if self.graph[i][r] > 1 and r not in visited:
                    recursive_call(r, visited)

        recursive_call(i, visited)
        print("Null")
    

    def BFS(self, start):
        j = self.vertices[start]
        queue = deque()
        queue.append(j)

        visited = set()
        visited.add(j)
        while queue:

            item = queue.popleft()
            for k, v in self.vertices.items():
                if v == item:
                    print(k)
                    print("|")

            for i in range(len(self.graph[item])):
                if self.graph[item][i] > 0 and i not in visited:
                    queue.append(i)
        
        
        print("Null")










