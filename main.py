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

