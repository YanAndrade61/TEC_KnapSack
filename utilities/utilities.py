import numpy as np

def txt2list(path: str) -> list:
    with open(path,'r') as f:
        x = [int(n) for n in f.readlines()]
    return x

def load_knapsack(path: str) -> tuple:
    capacity = txt2list(path.format(t = 'c'))[0]
    weights = np.array(txt2list(path.format(t = 'w')))
    profits = np.array(txt2list(path.format(t = 'p')))
    solution = np.array(txt2list(path.format(t = 's')))
    
    return capacity, weights, profits, solution