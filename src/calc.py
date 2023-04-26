import math
from const import *
from point import Point

class OpenList:
    def __init__(self) -> None:
        self.H = [0]*10000
        self.size = -1

    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return ((2 * index) + 1)
    
    def right_child(self, index):
        return ((2 * index) + 2)
    
    def is_empty(self):
        return self.size == -1
    
    def swap(self, index1, index2):
        temp = self.H[index1]
        self.H[index1] = self.H[index2]
        self.H[index2] = temp
    
    def shift_up(self, index):
        while index > 0 and self.H[self.parent(index)].f > self.H[index].f:
            self.swap(self.parent(index), index)
            index = self.parent(index)
    
    def shift_down(self, index):
        max_index = index

        l = self.left_child(index)

        if l <= self.size and self.H[l].f < self.H[max_index].f:
            max_index = l

        r = self.right_child(index)

        if r <= self.size and self.H[r].f < self.H[max_index].f:
            max_index = r

        if index != max_index:
            self.swap(index, max_index)
            self.shift_down(max_index)

    def insert(self, value):
        self.size = self.size + 1
        self.H[self.size] = value

        self.shift_up(self.size)

    def extractMin(self):
        result = self.H[0]

        self.H[0] = self.H[self.size]
        self.size = self.size - 1

        self.shift_down(0)
        return result
    
    def change_priority(self, index, value):
        oldp = self.H[index].f
        self.H[index] = value

        if value.f < oldp:
            self.shift_up(index)
        else:
            self.shift_down(index)
        
    def getMin(self):
        return self.H[0]
    
    def remove(self, index):
        self.H[index] = self.getMin() + 1
        self.shift_up(index)
        self.extractMin()
