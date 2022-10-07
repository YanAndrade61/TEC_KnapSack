from heuristics.AGSimple import AGSimple
from utilities.utilities import load_knapsack
from utilities.utilities import plot_results
from heuristics.DinamicPrograming import dinamic_programing
import itertools as it
from tqdm import tqdm

def main():
    
    path = str("./example/p01_{t}.txt")
    mutate = [i/100 for i in range(1,21)]
    ind = [20, 50, 100]
    gen = [20, 50, 100]

    capacity,wt,val,s = load_knapsack(path)
    with open("results.txt","w") as f:
        f.write("n_gen|n_ind|mutate_rate,it,gen,best\n")
    
    # dinamic_programing(capacity,wt,val,len(wt))

    for n_gen,n_ind,mutate_rate in tqdm(it.product(gen,ind,mutate),desc="Runing genetics "):
        for i in range(10):
            AGSimple(capacity,wt,val,s,n_gen,n_ind,mutate_rate,i).simulate()
    plot_results()

if __name__ == '__main__':
    main()