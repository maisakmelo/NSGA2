import random
import matplotlib.pyplot as plt
import numpy as np
import OPERADORES as op
from tqdm import tqdm


# Fonseca e Fleming
varmin = [-4, -4,-4]
varmax = [4,4,4]
nvar = 3

def function1(x):
    return 1-np.exp(-(x[0]-1/np.sqrt(3))**2-(x[1]-1/np.sqrt(3))**2-(x[2]-1/np.sqrt(3))**2)

def function2(x):
    return 1 - np.exp(-(x[0] + 1 / np.sqrt(3)) ** 2 - (x[1] + 1 / np.sqrt(3)) ** 2 - (x[2] + 1 / np.sqrt(3)) ** 2)

pop_size = 300
max_gen = 300


def gera_populacao(pop_size,nvar,varmin,varmax):
    pop = np.zeros((pop_size,nvar))
    for i in range(pop_size):
        pop[i,:] = np.random.uniform(varmin,varmax,nvar)
    return pop

solution = gera_populacao(pop_size,nvar,varmin,varmax)


for gen_no in  tqdm(range(0,max_gen)):
    function1_values = [function1(solution[i][:]) for i in range(0, pop_size)]
    function2_values = [function2(solution[i][:]) for i in range(0,pop_size)]
    non_dominated_sorted_solution = op.fast_non_dominated_sort(function1_values[:],function2_values[:])
    crowding_distance_values = []
    for i in range(0,len(non_dominated_sorted_solution)):
        crowding_distance_values.append((op.crowding_distance(function1_values[:], function2_values[:], non_dominated_sorted_solution[i][:])))
    solution2 = solution[:]
    #Generating offspring
    while(len(solution2)!=2*pop_size):
        a1 = random.randint(0,pop_size-1)
        b1 = random.randint(0,pop_size-1)
        solution2 = np.vstack([solution2,op.crossover(solution[a1][:],solution[b1][:], varmin, varmax)[:]])
    function1_values2 = [function1(solution2[i,:]) for i in range(0,2*pop_size)]
    function2_values2 = [function2(solution2[i,:]) for i in range(0,2*pop_size)]
    non_dominated_sorted_solution2 = op.fast_non_dominated_sort(function1_values2[:],function2_values2[:])
    crowding_distance_values2 = []
    for i in range(0,len(non_dominated_sorted_solution2)):
        crowding_distance_values2.append(op.crowding_distance(function1_values2[:],function2_values2[:],non_dominated_sorted_solution2[i][:]))
    new_solution = []
    for i in range(0,len(non_dominated_sorted_solution2)):
        non_dominated_sorted_solution2_1 = [op.index_of(non_dominated_sorted_solution2[i][j],non_dominated_sorted_solution2[i]) for j in range(0,len(non_dominated_sorted_solution2[i]))]
        front22 = op.sort_by_values(non_dominated_sorted_solution2_1[:],crowding_distance_values2[i][:])
        front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(0,len(non_dominated_sorted_solution2[i]))]
        front.reverse()
        for value in front:
            new_solution.append(value)
            if(len(new_solution)==pop_size):
                break
        if (len(new_solution)==pop_size):
            break
    solution = [solution2[i] for i in new_solution]

function1 = [i for i in function1_values]
function2 = [j for j in function2_values]


plt.xlabel('f1',fontsize = 15)
plt.ylabel('f2',fontsize = 15)
plt.scatter(function1,function2)
plt.show()

