import csv
from itertools import combinations
import time
from memory_profiler import profile
# bruteforce_data_path = "data\\dataset_bruteforce.csv"
bruteforce_data_path = "data\\dataset1_Python+P7.csv"
start_time = time.time()

class Action: 
    def __init__(self, name, price, benefit_percent):
        self.name = name      
        self.price = float(price)
        self.benefit_percent = float(benefit_percent)
        self.benefit_net = float(self.benefit_percent)*0.01*float(price)
        self.rapport = self.benefit_net / self.price

    def __repr__ (self):
        return f"[{self.name};{self.price};{self.benefit_net};{self.rapport}]"

def load_actions(bruteforce_data_path):
    """Charge les actions"""
    actions = []

    with open(bruteforce_data_path, "r") as csvfile:
        csvreader = csv.reader(csvfile)

        next(csvreader)  # Pour eviter l'entete
        for action in csvreader:
            actions.append(Action(action[0], action[1], action[2]))
            print(actions)
    return actions

def calculation_optimized(actions, limit):
    sum = 0
    total_benefit = 0
    opitmized_list = []
    for action in actions:
        
        sum += action.price

        if sum <= limit:
            opitmized_list.append(action)
            total_benefit += action.benefit_net
        
        elif sum > limit:  # Pour prendre combler l'ecart entre limit possible avec les meilleurs solutions
            sum -= action.price

    print("==================================================================")
    print(f"Voici la combinaison la plus rentable: {opitmized_list}")
    print(f"Somme investie: {sum}")
    print(f"Benefice: {total_benefit}")
    print(f"Temps d'execution: {time.time() - start_time}")  # renvoi le temps en s depuis epoch 1970 à 00:00:00
    print("==================================================================")




actions = load_actions(bruteforce_data_path)
actions.sort(key= lambda a: a.rapport, reverse=True)
calculation_optimized(actions, 500)

