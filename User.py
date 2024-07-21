class User():
    _id_ = 0
    names = {}
    users_ages = []
    users_location = []
    def __init__(self, name, age, location) -> None:
        self.name = name
        self.location = location
        self.age = age
        self.interests = []
        self.posts = []
        self.id = User._id_
        User._id_ += 1
        User.names[self.id] = self.name
        User.users_ages.append(self.age)
        User.users_location.append(self.location)

    
    def add_interests(self):
        decision = 0
        while decision == 0:
            interest = input("Write your interests: ")
            self.interests.append(interest)
            print("0: To continue, 1: To Stop")
            decision = int(input(""))


    def add_posts(self):
        decision = 0

        while decision == 0:
            post = input("Add a new post (name): ")
            self.posts.append(post)
            print("To Stop: Type 1, To Continue: Type 0")
            decision = int(input())


    