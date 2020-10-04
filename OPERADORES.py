import math
import random
import numpy as np


def index_of(a,list):
    for i in range(0,len(list)):
        if list[i] == a:
            return i
    return -1

def sort_by_values(list1,values):
    sorted_list = []
    while(len(sorted_list)!=len(list1)):
        if index_of(min(values),values) in list1:
            sorted_list.append(index_of(min(values),values))
        values[index_of(min(values),values)] = math.inf
    return sorted_list

def fast_non_dominated_sort(values1,values2):
    S = [[] for i in range(0,len(values1))]
    front = [[]]
    n = [0 for i in range(0,len(values1))]
    rank = [0 for i in range(0,len(values1))]
    for p in range(0,len(values1)):
        S[p] = []
        n[p] = 0
        for q in range(0,len(values1)):
            if (values1[p] < values1[q] and values2[p] < values2[q]) or (values1[p] <= values1[q] and values2[p] < values2[q]) or (values1[p] < values1[q] and values2[p] <= values2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (values1[q]<values1[p] and values2[q] < values2[p]) or (values1[q] <= values1[p] and values2[q] < values2[p]) or (values1[q] < values1[p] and values2[q] <= values2[p]):
                n[p] = n[p] + 1
        if n[p] == 0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)
    i = 0
    while(front[i] != []):
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] = n[q] - 1
                if (n[q] == 0):
                    rank[q] = i+1
                    if q not in Q:
                        Q.append(q)
        i += 1
        front.append(Q)
    del front[len(front) -1]
    return front

def crowding_distance(values1,values2,front):
    distance = [0 for i in range(0,len(front))]
    sorted1 = sort_by_values(front,values1[:])
    sorted2 = sort_by_values(front,values2[:])
    distance[0] = 4444444444444444
    distance[len(front) - 1] = 4444444444444444
    for k in range(1,len(front)-1):
        distance[k] = distance[k] + (values1[sorted1[k + 1]] - values1[sorted1[k - 1]]) / (max([values1[i] for i in front]) - min([values1[i] for i in front]))
    for k in range(1,len(front)-1):
       distance[k] = distance[k] + (values2[sorted2[k + 1]] - values2[sorted2[k - 1]]) / (max([values2[i] for i in front]) - min([values2[i] for i in front]))
    return distance


def crossover(pai1,pai2,varmin,varmax):
    r = random.random()
    if r>0.5:
        return mutation((pai1+pai2)/2,varmin,varmax)
    else:
        return mutation((pai1-pai2)/2,varmin,varmax)


def mutation(solution,min_x,max_x):
    mutation_prob = random.random()
    if mutation_prob < 1:
        solution = np.array(min_x)+(np.array(max_x)-np.array(min_x))*random.random()
    return solution