import numpy as np
import random


class AGSimple:

    def __init__(self,capacity: int, weights: list, profits: list, solution: list=[], n_ind: int = 20, n_gen: int = 500, mutate_rate: float = 0.1,i: int=0):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.n_ind = n_ind
        self.n_gen = n_gen
        self.mutate_rate = mutate_rate
        self.solution = solution
        self.i = i

    def simulate(self) -> None:
        
        individuals = [np.random.choice(2, len(self.profits)) for i in range(self.n_ind)]
        
        for i in range(self.n_gen):

            fitness_lst = self.fitness(individuals)        
            
            parents = self.get_parents(fitness_lst)
            
            new_ind = self.cross(individuals,parents)
            
            
            new_ind = self.mutate(new_ind)
            
            maior = np.argmax(fitness_lst)
            
            new_ind[0] = individuals[maior]
            with open("results.txt","a") as f:
                print(f"{self.n_gen}|{self.n_ind}|{self.mutate_rate},{self.i},{i},{fitness_lst[maior]}",file=f)
            #if np.array_equal(individuals[maior],self.solution):print("Solution has been reached!");break
            individuals = np.array(new_ind)
            
            
        return individuals[maior]
        

    def fitness(self, individuals : list) -> list:
        fitness_lst = []
        for i in range(self.n_ind):
            weight_ind = self.weights * individuals[i]
            profits_ind = self.profits * individuals[i]

            if sum(weight_ind) < self.capacity:
                fitness_lst.append(sum(profits_ind))
            else:
                penalty = sum(profits_ind)*(sum(weight_ind)-self.capacity)
                fitness_lst.append(sum(profits_ind) - penalty)
        
        return fitness_lst
    
    def get_parents(self,fitness : list) -> list:
        parents = []
        for i in range(self.n_ind):
            while(True):
                choosen = np.random.choice(len(self.profits),2,replace=False)
                best = choosen[np.argmax([fitness[j] for j in choosen])]
                if  i == 0 or best != parents[-1]:
                    parents.append(best)
                    break
        return parents
    
    def cross(self,individuals: list,parents: list):
        new_individuals = []
        for i in range(0,self.n_ind,2):
            a = parents[i]
            b = parents[i+1]

            point = random.randint(1,len(self.profits)-2)
            new_individuals.append(np.concatenate([individuals[a][:point], individuals[b][point:]]))
            new_individuals.append(np.concatenate([individuals[b][:point], individuals[a][point:]]))
        return new_individuals
    
    def mutate(self,individuals: list):
        
        for i in range(self.n_ind):
            for j in range(len(self.profits)):
                rate = random.random()
                if rate <= self.mutate_rate:
                    individuals[i][j] = int(not individuals[i][j])
        
        return individuals