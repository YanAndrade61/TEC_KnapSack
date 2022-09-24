from heuristics.AGSimple import AGSimple
from utilities.utilities import load_knapsack

def main():
    path = str("./example/p01_{t}.txt")
    capacity,weights,profits,s = load_knapsack(path)
    AGSimple(capacity,weights,profits,s,500,500,0.2).simulate()

if __name__ == '__main__':
    main()