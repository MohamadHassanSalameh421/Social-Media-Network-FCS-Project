class DiGraph(): #A directed graph

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
        if user1 and user2 in self.vertices:

            self.graph[self.vertices[user2]][self.vertices[user1]] = distance






    





