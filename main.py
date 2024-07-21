from collections import deque
from User import *
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import tkinter as tk
import customtkinter
import random
from Graph import *






class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.G = DiGraph() 

        #Add nodes
        self.label = customtkinter.CTkLabel(self, text="Create A user", font=("Arial", 20))
        self.label.grid(row = 0, column=0)
        self.label1 = customtkinter.CTkLabel(self, text="Enter Your Name") #Name
        self.label1.grid(row = 1, column=0)
        self.textbox = customtkinter.CTkTextbox(self, height = 20, width=200)
        self.textbox.grid(row = 2, column=0)

        #Age
        self.label2 = customtkinter.CTkLabel(self, text="Enter Your Age")
        self.label2.grid(row = 3, column=0)
        self.textbox1 = customtkinter.CTkTextbox(self, height = 20, width = 200)
        self.textbox1.grid(row = 4, column=0)

        #Location
        self.label3 = customtkinter.CTkLabel(self, text="Enter Your Location")
        self.label3.grid(row = 5, column=0)
        self.textbox2 = customtkinter.CTkTextbox(self, height = 20, width = 200)
        self.textbox2.grid(row = 6, column=0)

        #Retrieve the information
        self.button2 = customtkinter.CTkButton(self, text="Submit", command=self.retrieveInfo)
        self.button2.grid(row= 7, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        # Add friends
        self.label4 = customtkinter.CTkLabel(self, text="Follow User2", font=("Arial", 20))
        self.label4.grid(row = 8, column=0)
        self.label5 = customtkinter.CTkLabel(self, text="User1")
        self.label5.grid(row = 9, column=0)
        self.textbox3 = customtkinter.CTkTextbox(self, height = 20, width = 200)
        self.textbox3.grid(row = 10, column=0)

        self.label6 = customtkinter.CTkLabel(self, text="User2")
        self.label6.grid(row = 11, column=0)
        self.textbox4 = customtkinter.CTkTextbox(self, height = 20, width = 200)
        self.textbox4.grid(row = 12, column=0)

        self.button2 = customtkinter.CTkButton(self, text="Submit", command=self.add_friends)
        self.button2.grid(row= 13, column=0, padx=20, pady=20, sticky='ew', columnspan=2)

        self.button3 = customtkinter.CTkButton(self, text="Display Graph", command=self.display_graph)
        self.button3.grid(row= 14, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #Remove a user
        self.label7 = customtkinter.CTkLabel(self, text="Remove User", font=("Arial", 20))
        self.label7.grid(row = 15, column=0)
        self.label8 = customtkinter.CTkLabel(self, text="User")
        self.label8.grid(row = 16, column=0)
        self.textbox5 = customtkinter.CTkTextbox(self, height=20, width= 200)
        self.textbox5.grid(row = 17, column=0)
        self.button4 = customtkinter.CTkButton(self, text="Remove", command=self.remove_user)
        self.button4.grid(row= 18, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #Remove friends
        self.label9 = customtkinter.CTkLabel(self, text="Remove Follower", font=("Arial", 20))
        self.label9.grid(row = 19, column=0)
        self.label10 = customtkinter.CTkLabel(self, text="User1")
        self.label10.grid(row = 20, column=0)
        self.textbox6 = customtkinter.CTkTextbox(self, height=20, width= 200)
        self.textbox6.grid(row = 21, column=0)
        self.label11 = customtkinter.CTkLabel(self, text="User2")
        self.label11.grid(row = 22, column=0)
        self.textbox7 = customtkinter.CTkTextbox(self, height=20, width= 200)
        self.textbox7.grid(row = 23, column=0)
        self.button5 = customtkinter.CTkButton(self, text="Remove", command=self.remove_user)
        self.button5.grid(row= 24, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #Searching Algorithms
        self.label12 = customtkinter.CTkLabel(self, text="Where do you want to start?", font=("Arial", 20))
        self.label12.grid(row = 25, column=0)
        self.textbox8 = customtkinter.CTkTextbox(self, height=20, width= 200)
        self.textbox8.grid(row = 26, column=0)
        self.button6 = customtkinter.CTkButton(self, text="DFS", command=self.DFS)
        self.button6.grid(row= 27, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        self.button7 = customtkinter.CTkButton(self, text="BFS", command=self.BFS)
        self.button7.grid(row= 28, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        self.button8 = customtkinter.CTkButton(self, text="Dijkstra", command=self.dijkstra)
        self.button8.grid(row= 29, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #Search for a user
        self.label13 = customtkinter.CTkLabel(self, text="Please click on sort below before searching for a user", font=("Arial", 16))
        self.label13.grid(row = 30, column=0)
        self.textbox9 = customtkinter.CTkTextbox(self, height=20, width= 200)
        self.textbox9.grid(row = 31, column=0)
        self.button9 = customtkinter.CTkButton(self, text="Search", command=self.searching)
        self.button9.grid(row= 32, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #sorting
        self.button10 = customtkinter.CTkButton(self, text="Sort", command=self.sort)
        self.button10.grid(row= 33, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #average number of friends
        self.button11 = customtkinter.CTkButton(self, text="Average number of friends", command=self.average_number_off_friends)
        self.button11.grid(row= 34, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #Average Age
        self.button12 = customtkinter.CTkButton(self, text="Average age", command=self.average_age)
        self.button12.grid(row= 35, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #Most Common Location
        self.button13 = customtkinter.CTkButton(self, text="Most common location", command=self.most_commonn_location)
        self.button13.grid(row= 36, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
        #connected components
        self.label14 = customtkinter.CTkLabel(self, text="Connected Components", font=("Arial", 20))
        self.label14.grid(row = 37, column=0)
        self.label15 = customtkinter.CTkLabel(self, text="Enter a user", font=("Arial", 18))
        self.label15.grid(row = 38, column=0)
        self.textbox10 = customtkinter.CTkTextbox(self, height=20, width= 200)
        self.textbox10.grid(row = 39, column=0)
        self.button14 = customtkinter.CTkButton(self, text="Click", command=self.connected_components)
        self.button14.grid(row= 40, column=0, padx=20, pady=20, sticky='ew', columnspan=2)

    def retrieveInfo(self):
        inputValue = self.textbox.get("1.0","end-1c")
        inputValue1 = self.textbox1.get("1.0","end-1c")
        inputValue2 = self.textbox2.get("1.0","end-1c")
        
    
        if not inputValue or not inputValue1 or not inputValue2:
            customtkinter.CTkInputDialog(text="Please fill each field!") #I did not find any function to prompt a warning :(
        else:    
            user1 = User(inputValue, int(inputValue1), inputValue2)
            self.G.add_user(user1.name)
    
    def add_friends(self):
        inputValue1 = self.textbox3.get("1.0","end-1c")
        inputValue2 = self.textbox4.get("1.0","end-1c")
        if not inputValue1 or not inputValue2:
            customtkinter.CTkInputDialog(text="Please fill each field!")
        else:
            self.G.add_friends(inputValue1, inputValue2, random.randint(1, 11))
    
    def display_graph(self):
        self.G.displayGraph()

    
    def remove_user(self):
        inputValue1 = self.textbox5.get("1.0","end-1c")
        if not inputValue1:
            customtkinter.CTkInputDialog(text="Please fill the field!")
        else:
            self.G.remove_user(inputValue1)
    
    def remove_friends(self):
        inputValue1 = self.textbox6.get("1.0","end-1c")
        inputValue2 = self.textbox7.get("1.0","end-1c")

        if not inputValue1 or not inputValue2:
            customtkinter.CTkInputDialog(text="Please fill the field!")
        else:
            self.G.remove_friends(inputValue1, inputValue2)
    
    def DFS(self):
        inputValue1 = self.textbox8.get("1.0","end-1c")
        if not inputValue1:
            customtkinter.CTkInputDialog(text="Please fill the field!")
        else:
            self.G.DFS(inputValue1)


    def BFS(self):
        inputValue1 = self.textbox8.get("1.0","end-1c")
        if not inputValue1:
            customtkinter.CTkInputDialog(text="Please fill the field!")
        else:
            self.G.BFS(inputValue1)
                
    
    def dijkstra(self):
        inputValue1 = self.textbox8.get("1.0","end-1c")
        if not inputValue1:
            customtkinter.CTkInputDialog(text="Please fill the field!")
        else:
            self.G.dijkstra(inputValue1)
    def searching(self):
        inputValue1 = self.textbox9.get("1.0","end-1c")
        if not inputValue1:
            customtkinter.CTkInputDialog(text="Please fill the field!")
        else:
            if self.G.searching_for_user(inputValue1) == True:
                print("Found!")
            else:
                print("Not Found!")
    def sort(self):
        self.G.sorting_users()
