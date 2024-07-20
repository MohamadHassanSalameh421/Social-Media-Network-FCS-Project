class Graph():

    def __init__(self):

        self.graph = []
        self.vertices = {}
    

    def add_user(self, user):
        if user not in self.vertices:

            self.vertices[user] = len(self.graph)

            for row in self.graph:
                self.graph.append(0)

            self.graph.append([0] * (len(self.graph) + 1))

            
