import numpy as np
import functions as f

# constructs the sample space to desired dimensions
n = int(input("rows?"))
m = int(input("columns?"))
max_pop = n * m
start_population = int(input('input starting population(MAX:'+str(max_pop)+'):'))

calc_pond = f.Generate_Initial_Pond(np.tile(f.Tile(True, False), (n, m)),start_population, max_pop, n, m)
print(f.visualise_pond(calc_pond))    
