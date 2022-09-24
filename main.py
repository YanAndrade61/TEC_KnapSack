from heuristics.AGSimple import AGSimple
from utilities.utilities import load_knapsack
from heuristics.DinamicPrograming import dinamic_programing

def main():
    
    path = str("./example/p01_{t}.txt")
    
    capacity,wt,val,s = load_knapsack(path)
    
    dinamic_programing(capacity,wt,val,len(wt))
    
    # AGSimple(capacity,weights,profits,s,500,500,0.2).simulate()

if __name__ == '__main__':
    main()