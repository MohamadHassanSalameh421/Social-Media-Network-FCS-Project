class User():

    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        self.interests = []

    
    def add_interests(self):
        decision = 0
        while decision == 0:
            interest = input("Write your interests: ")
            self.interests.append(interest)
            print("0: To continue, 1: To Stop")
            decision = int(input(""))




    