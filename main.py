import numpy as np
import random

def txt2list(path):
    with open(path,'r') as f:
        x = [int(n) for n in f.readlines()]
    return x

def genetics(capacity: int, weights: list, profits: list, n_ind: int, n_gen: int):
    
    n_items = len(profits)

    individuals = [np.random.choice(2, n_items) for i in range(n_ind)]
    
    fitness = [0]*n_ind
    

    for k in range(n_gen):
        for i in range(n_ind):

            weight_ind = weights*individuals[i]
            profits_ind = profits*individuals[i]

            if sum(weight_ind) < capacity:
                fitness[i] =  sum(profits_ind)
            else:
                penalty = sum(profits_ind)*(sum(weight_ind)-capacity)
                fitness[i] = sum(profits_ind) - penalty
        choices = []
        for i in range(n_ind):
            while(True):
                choosen = np.random.choice(n_items,2,replace=False)
                best = choosen[np.argmax([fitness[j] for j in choosen])]
                if  i == 0 or best != choices[-1]:
                    choices.append(best)
                    break
        new_ind = []
        for i in range(0,n_ind,2):
            a = choices[i]
            b = choices[i+1]
            point = random.randint(1,n_ind-2)

            new_ind.append(np.concatenate([individuals[a][:point], individuals[b][point:]]))
            new_ind.append(np.concatenate([individuals[b][:point], individuals[a][point:]]))

        maior = np.argmax(fitness)
        new_ind[0] = individuals[maior]
        individuals = np.array(new_ind)
        print(fitness[maior],individuals[maior])

    pass

def main():
    path = str("./data/p01_{t}.txt")
    capacity = txt2list(path.format(t = 'c'))[0]
    weights = np.array(txt2list(path.format(t = 'w')))
    profits = np.array(txt2list(path.format(t = 'p')))
    solution = np.array(txt2list(path.format(t = 's')))
    genetics(capacity,weights,profits,300,1000)
    
if __name__ == '__main__':
    main()