from collections import deque
from User import *
import networkx as nx
import matplotlib.pyplot as plt
class DiGraph(): #A directed graph, In this weighted Graph 0 means no connections

    def __init__(self):

        self.graph = []
        self.vertices = {}
        self.names = []
    

    def add_user(self, user: User): #In here we add users to the social network
        if user not in self.vertices:

            self.vertices[user.name] = len(self.graph)

            for row in self.graph:
                row.append(0)

            self.graph.append([0] * (len(self.graph) + 1))

            self.names.append(user.name)
    


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

    

    def displayGraph(self):
        H = nx.DiGraph()

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] > 0:
                    H.add_edge(User.names[i], User.names[j], weight=self.graph[i][j])
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
                return True

            elif self.names[mid] < user_name:
                left = mid + 1
            else:
                right = mid - 1

        return False
        








G = DiGraph()
user1 = User("Alice", 17, "NY")
user2 = User("Bob", 18, "Lebanon")
user3 = User("Mohamad", 19, "Lebanon")
user4 = User("ali", 19, "Ny")

G.add_user(user1)
G.add_user(user2)
G.add_user(user3)
G.add_user(user4)
G.add_friends(user1, user3, 5)
G.add_friends(user1, user2, 5)
G.add_friends(user2, user4, 4)




G.displayGraph()


    






