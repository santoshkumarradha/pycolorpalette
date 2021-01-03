import pickle
from colour import Color
from math import sqrt


class colors():
    def __init__(self):
        self.data=pickle.load(open("colors.data","rb"))
        self.palette=[[Color("#"+i) for i in pal_list] for pal_list in self.data]
        
    def get_all_colors(self):
        return self.palette