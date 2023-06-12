import csv
import time
import sys

data_path = sys.argv[1]
start_time = time.time()


class Action:
    def __init__(self, name, price, benefit_percent):
        self.name = name
        self.price = float(price)
        self.benefit_percent = float(benefit_percent)
        self.benefit_net = float(self.benefit_percent)*0.01*float(price)
        self.rapport = self.benefit_net / self.price

    def __repr__(self):
        return f"[{self.name};{self.price};{self.benefit_percent}]"


def load_actions(data_path):
    """Charge les actions"""
    actions = []

    with open(data_path, "r") as csvfile:
        csvreader = csv.reader(csvfile)

        next(csvreader)  # Pour eviter l'entete
        for action in csvreader:
            if float(action[1]) != 0:
                actions.append(Action(action[0], action[1], action[2]))
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
    print(f"Voici les actions à acheter: {opitmized_list} \n")
    print(f"Somme investie: {sum}")
    print(f"Benefice: {total_benefit}")
    print(f"Temps d'execution: {time.time() - start_time}")  # renvoi le temps en s depuis epoch 1970 à 00:00:00
    print("==================================================================")


def main():
    actions = load_actions(data_path)
    actions.sort(key=lambda a: a.rapport, reverse=True)
    calculation_optimized(actions, 500)


main()
