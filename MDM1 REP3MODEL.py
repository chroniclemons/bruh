import numpy as np
import pandas as pd
from numpy import random
# constructs the sample space to desired dimensions
n = int(input("rows?"))
m = int(input("columns?"))
max_pop = n * m
start_population = int(input('input starting population(MAX:'+str(max_pop)+'):'))


class Tile():
    def __init__(self, empty, alive):
        self.empty = bool(empty)
        self.alive = bool(alive)
        self.represent = self.visualise()
    
    def visualise(self):
        if self.empty:
            self.represent = 0
        elif self.alive:
            self.represent = 1
        return self.represent

    




# Generates a random layout of out plant to start the model
def Generate_Initial_Pond(calc_pond, start_population, max_pop, n, m):   
    pond_count = 0
    n_count = 0 
    m_count = 0
    population_temp = 0
    for r in calc_pond:
        for c in r:        
            m_count += 1
            pond_count += 1
            prob_temp = (max_pop - pond_count)
            if prob_temp == 0:
                prob_temp = 1
            R = np.random.random()
            print(R,((start_population - population_temp) / prob_temp),population_temp)
            if population_temp == start_population:
                break
            elif R < ((start_population - population_temp) / prob_temp):
                calc_pond[n_count % n, m_count % m] = Tile(False, True)
                population_temp += 1
        n_count += 1
        m_count = 0
    return calc_pond



def visualise_pond(calc_pond):
    visual_pond = np.copy(calc_pond)
    n_count = 0 
    m_count = 0      
    for r in visual_pond:
        for c in r:
            visual_pond[n_count, m_count] = c.represent
            m_count += 1
        m_count = 0
        n_count += 1
    return visual_pond

    
    
    
    
    
    
    
    
    