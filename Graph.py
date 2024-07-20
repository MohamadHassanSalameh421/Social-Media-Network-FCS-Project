from collections import deque
from User import *
class DiGraph(): #A directed graph, In this weighted Graph 0 means no connections

    def __init__(self):

        self.graph = []
        self.vertices = {}
    

    def add_user(self, user: User): #In here we add users to the social network
        if user not in self.vertices:

            self.vertices[user.name] = len(self.graph)

            for row in self.graph:
                row.append(0)

            self.graph.append([0] * (len(self.graph) + 1))
    


    def add_friends(self, user1: User, user2: User, distance=0): #We add friends with distances to user2 (user1 -> user2)
        if (user1.name and user2.name) in self.vertices:

            self.graph[self.vertices[user1.name]][self.vertices[user2.name]] = distance



    def remove_friends(self, user1: User, user2: User):
        if (user1.name and user2.name) in self.vertices:

            self.graph[self.vertices[user2.name]][self.vertices[user1.name]] = 0 #0 means no relationship between these two users
    
    

    def remove_user(self, user1: User):

        if user1.name in self.vertices:

            del self.graph[self.vertices[user1.name]]

            for row in self.graph:
                row.pop()
            
            for k, v in self.vertices.items():
                if v > self.vertices[user1.name]:
                    self.vertices[k] = v - 1
                    
            del self.vertices[user1.name]
    


    def DFS(self, start: User):

        visited = set()
        i = self.vertices[start.name]

        print("Depth-first Search starting from " + start.name + ":")

        def recursive_call(i, visited):
            for k, v in self.vertices.items():
                if v == i:
                    print(k, end= ' ')

            visited.add(i)

            for r in range(len(self.graph)):
                if self.graph[i][r] > 1 and r not in visited:
                    recursive_call(r, visited)

        recursive_call(i, visited)
    

    def BFS(self, start: User):
        j = self.vertices[start.name]
        queue = deque()
        queue.append(j)

        visited = set()
        visited.add(j)
        print("Breadth-first Search starting from " + start.name + ":")
        while queue:

            item = queue.popleft()
            for k, v in self.vertices.items():
                if v == item:
                    print(k, end=' ')

            for i in range(len(self.graph[item])):
                if self.graph[item][i] > 0 and i not in visited:
                    queue.append(i)
        
        

    
    def add_posts(self, user: User):
        user.add_posts()
    

    def show_posts(self, user: User):
        print(user.posts)


    def add_interests(self, user: User):
        user.add_interests()

    
    def show_interests(self, user: User):
        print(user.interests)

    
    def dijkstra(self, start_user: User):
        start_user_index = self.vertices[start_user.name]
        distances = [float('inf')] * len(self.graph)
        visited = [False] * len(self.graph)
        distances[start_user_index] = 0

        for _ in range(len(self.graph)):
            min_distance = float('inf')
            u = None
            for i in range(len(self.graph)):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
        
            if u is None:
                break
            
            visited[u] = True

            for v in range(len(self.graph)):
                if self.graph[u][v] > 0 and not visited[v]:
                    alt = distances[u] + self.graph[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
        
        for i, v in enumerate(distances):
            print(f"Shortest path from {start_user.name} to {User.names[i + 1]} is {v}")




G = DiGraph()
user1 = User("Alice", 17, "NY")
user2 = User("Bob", 18, "Lebanon")
user3 = User("Mohamad", 19, "Lebanon")
user4 = User("ali", 19, "Ny")
G.add_user(user1)
G.add_user(user2)
G.add_user(user3)
G.add_user(user4)
G.add_friends(user1, user2, 5)
G.add_friends(user2, user1, 5)
G.add_friends(user2, user3, 4)
G.add_friends(user3, user4, 5)



G.DFS(user1)

    






