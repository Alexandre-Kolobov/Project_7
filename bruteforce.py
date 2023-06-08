import csv
from itertools import combinations
bruteforce_data_path = "data\\dataset_bruteforce.csv"

        


def load_actions(bruteforce_data_path):
        """Charge les actions"""
        rows=[]

        with open(bruteforce_data_path, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            for row in csvreader:
                rows.append(row)
        return rows


def bruteforce_under_500(actions: list ) -> list:
    """Recherche des tous les possibilités pour un montant max de 500 euros"""
    combinations_under_500 = []
    n = 1 # Pour ne pas prendre l'entete du fichier csv 

    while n <= len(actions):
        actions_combinations = combinations(actions[1:], n) # possibilité d'avoir de 1 à 20 actions dans une combinaison

        for combination in actions_combinations: # verification de la somme pour chaque combinaison. Il ne faut pas depasser 500 euros
            sum = bruteforce_sum(combination)

            if sum <= 500:
                combinations_under_500.append(combination) #alimentation d'une liste avec les combinaisons <= à 500 euros
        n += 1
    
    return combinations_under_500

def bruteforce_sum(combination):
    sum = int(0)
    for action in combination:
        sum = sum + int(action[1])

    return sum


def bruteforce_benefit(combination):
    benefit = 0 
    for action in combination :
        benefit = benefit + (int(action[2])*0.01*int(action[1]))

    return benefit

actions = load_actions(bruteforce_data_path)
combinations_under_500 = bruteforce_under_500(actions)
combinations_under_500.sort(key=lambda combination: bruteforce_benefit(combination), reverse=True)

print(f"Voici la combinaison la plus rentable: {combinations_under_500[0]}")
print(f"Somme investit: {bruteforce_sum(combinations_under_500[0])}")
print(f"Benefice: {bruteforce_benefit(combinations_under_500[0])}")