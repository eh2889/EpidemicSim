import random
import math
from matplotlib import pyplot as plt
import numpy as np

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 15 # recovery time in time-steps
virality = .8    # probability that a neighbor cell is infected in 
sd = .8
mean = 3                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self):
        self.time = 0
        self.state = "I"
        
    
    def process(self, adjacent_cells):
        if self.time >= recovery_time:
            self.state = "S"
        if self.state == "I":
            r = random.random()
            p = pdeath(self.time,mean,sd)
            if r <= p:
                self.state = "R"
        if self.state == "I" and self.time >= 1:
            self.time += 1
            li = adjacent_cells
            for i in range(len(li)):
                if li[i].state == 'S':
                    r = random.random()
                    if r <= virality:
                        li[i].infect()
        else:
            self.time += 1
            
            
            
        
        
        
        
class Map(object):
    
    cells = dict()
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cell = cell
        key = (cell.x, cell.y)
        self.cells[key] = self.cell
        
    def display(self):
        img = np.zeros((150,150,3), dtype=np.uint8)
        #red,green,gray = range(3)
        for cell in self.cells:
            c = self.cells[cell]
            if c.state == 'S':
                color = 1
                img[c.x,c.y,color] = 255
            elif c.state == 'I':
                color = 0
                img[c.x,c.y,color] = 255
            else:
                img[c.x,c.y] = 150
        plt.imshow(img)
        #return img
    
    
    def adjacent_cells(self, x,y):
        li = []
        self.x = x
        self.y = y
        if self.x < 150 and self.x > 0:
            e = (self.x+1,self.y)
            w = (self.x-1,self.y)
            if e in self.cells:
                e1 = self.cells[e]
                li.append(e1)
            if w in self.cells:
                w1 = self.cells[w]
                li.append(w1)
        elif self.x < 150:
            e = (self.x+1,self.y)
            if e in self.cells:
                e1 = self.cells[e]
                li.append(e1)
        else:
            w = (self.x-1,self.y)
            if w in self.cells:
                w1 = self.cells[w]
                li.append(w1)
        
        if self.y < 150 and self.y > 0:
            n = (self.x,self.y-1)
            s = (self.x,self.y+1)
            if n in self.cells:
                n1 = self.cells[n]
                li.append(n1)
            if s in self.cells:
                s1 = self.cells[s]
                li.append(s1)
            
            
        elif self.y > 0:
            n = (self.x,self.y-1)
            if n in self.cells:
                n1 = self.cells[n]
                li.append(n1)
        else:
            s = (self.x,self.y+1)
            if s in self.cells:
                s1 = self.cells[s]
                li.append(s1)
        
        
        
        
        return li
    
    def time_step(self):
        for cell in self.cells:
            c = self.cells[cell]
            c1 = self.adjacent_cells(c.x,c.y)
            c.process(c1)
        self.display()
        # Update each cell on the map 
        # display the map.
        
        # ... cell.process(adjacent_cells... )
        

            
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m
