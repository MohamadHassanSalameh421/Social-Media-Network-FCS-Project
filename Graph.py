from collections import deque
from User import *
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import tkinter as tk
import customtkinter
import random
class DiGraph(): #A directed graph, In this weighted Graph 0 means no connections

    def __init__(self):

        self.graph = []
        self.vertices = {}
        self.names = []
        self.namesdict = {}
    

    def add_user(self, user_name): #In here we add users to the social network
        if user_name not in self.vertices:

            self.vertices[user_name] = len(self.graph)
            self.namesdict[len(self.graph)] = user_name

            for row in self.graph:
                row.append(0)

            self.graph.append([0] * (len(self.graph) + 1))

            self.names.append(user_name)
    


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

        print("Depth-first Search starting from " + start + ":")

        def recursive_call(i, visited):
            for k, v in self.vertices.items():
                if v == i:
                    print(k, end= ' ')

            visited.add(i)

            for r in range(len(self.graph)):
                if self.graph[i][r] > 1 and r not in visited:
                    recursive_call(r, visited)

        recursive_call(i, visited)
    

    def BFS(self, start):
        j = self.vertices[start]
        queue = deque()
        queue.append(j)

        visited = set()
        visited.add(j)
        print("Breadth-first Search starting from " + start + ":")
        while queue:
            

            item = queue.popleft()
            for k, v in self.vertices.items():
                if v == item:
                    print(k, end=' ')

            for i in range(len(self.graph[item])):
                if self.graph[item][i] > 0 and i not in visited:
                    queue.append(i)
        
        

    
    def dijkstra(self, start_user):
        start_user_index = self.vertices[start_user]
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
            print(f"Shortest path from {start_user} to {self.namesdict[i]} is {v}")

    

    def displayGraph(self):
        H = nx.DiGraph()

        for i in range(len(self.graph)):
            H.add_node(self.namesdict[i])
            for j in range(len(self.graph)):
                if self.graph[i][j] > 0:
                    H.add_edge(self.namesdict[i], self.namesdict[j], weight=self.graph[i][j])
                
        edge_label = nx.get_edge_attributes(H, 'weight')

        pos = nx.circular_layout(H)
        # nodes
        nx.draw_networkx_nodes(H, pos, node_size=5000, node_color= '#FEE715')
        # edges
        nx.draw_networkx_edges(H, pos, width=10, edge_color="#101820",alpha = 0.7, style="dashed", arrowsize= 90)
        # node labels
        nx.draw_networkx_labels(H, pos, font_size=30, font_family="Cursive")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(H, "weight")
        nx.draw_networkx_edge_labels(H, pos, edge_labels)

    
        
        plt.axis("off")
        plt.tight_layout()        
        plt.show()
    


    def searching_for_user(self, user_name):
        left = 0
        right = len(self.graph) - 1

        while left <= right:
            mid = left+ right // 2

            if self.names[mid] == user_name:
                return "Found"

            elif self.names[mid] < user_name:
                left = mid + 1
            else:
                right = mid - 1

        return "Not Found"
    

    def sorting_users(self):
        n = len(self.names)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.names[j] > self.names[j + 1]:
                    self.names[j], self.names[j + 1] = self.names[j + 1], self.names[j]

        

        

    def average_number_of_friends(self):
        #to count the number of friends of all of the users
        counter = 0

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] > 0:
                    counter += 1
        print(counter // len(self.graph)) # dividing the counter with number of users


    def average_age(self): #calculates the average age of all the users
        average = 0
        for i in User.users_ages:
            average += i
        print(f'Average age is: {average // len(self.graph)}')
    

    def most_common_location(self): #gets the most common location of the users
        locations = Counter(User.users_location)
    

        common_location = max(locations, key= lambda x: locations[x]) #gets the highest number of a specific location

        print(common_location)
    

    
    def connected_components(self, user): #We only need to use BFS or DFS because they will show us all the connected components
        j = self.vertices[user]
        queue = deque()
        queue.append(j)

        visited = set()
        visited.add(j)
        while queue:

            item = queue.popleft()
            for k, v in self.vertices.items():
                if v == item:
                    print(k, end=' ')

            for i in range(len(self.graph[item])):
                if self.graph[item][i] > 0 and i not in visited:
                    queue.append(i)







    






