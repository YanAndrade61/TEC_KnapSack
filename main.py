from heuristics.AGSimple import AGSimple
import numpy as np
import random

def txt2list(path):
    with open(path,'r') as f:
        x = [int(n) for n in f.readlines()]
    return x

def main():
    path = str("./data/p01_{t}.txt")
    capacity = txt2list(path.format(t = 'c'))[0]
    weights = np.array(txt2list(path.format(t = 'w')))
    profits = np.array(txt2list(path.format(t = 'p')))
    solution = np.array(txt2list(path.format(t = 's')))
    AGSimple(capacity,weights,profits,500,500,0.2).simulate()
if __name__ == '__main__':
    main()