import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

def plot_results():
    data = pd.read_csv("results.txt")   
    data_mean = data.groupby(by=["n_gen|n_ind|mutate_rate"])['best'].mean().reset_index()
    best_parameter = data_mean.max()['n_gen|n_ind|mutate_rate']
    data_parameter = data[data["n_gen|n_ind|mutate_rate"] == best_parameter]
    it_ls = data_parameter.groupby(by="it").agg({"best": lambda x: list(x)})
    for lst in it_ls['best']:
        plt.plot(range(len(it_ls['best'][0])),lst)
    plt.title("Fitness per generation")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.savefig("Best_Parameters_Plot.png")