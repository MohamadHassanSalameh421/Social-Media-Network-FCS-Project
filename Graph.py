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

            self.graph[self.vertices[user2]][self.vertices[user1]] = distance



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

        





G = DiGraph()
G.add_user("Alice")
G.add_user("Bob")
G.add_user("Ali")
G.add_friends("Alice", "Bob", 8)
G.add_friends("Bob", "Alice", 8)
G.add_friends("Bob", "Ali", 2)

G.DFS("Ali")

    






