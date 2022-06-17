#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tokenize import group
from typing import List


def convert_to_absolute(number: float) -> float:
    if number<0:
        number = -1 * number
        return number
    else:
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    Prefixes = list(prefixes)
    Noms = []
    for i in Prefixes:
        nom = i + suffixe
        Noms.append(nom)
    return Noms


def prime_integer_summation() -> int:

    somme = 0
    cpt = 0
    nbr = 2

    while cpt < 100:
        for i in range (2, nbr):
            if nbr % i == 0 :
                break
        else:
            somme += nbr
            cpt += 1
        nbr += 1
    return somme


def factorial(number: int) -> int:
    fct = 1
    for k in range(1, number + 1):
        fct = fct * k
    return fct


def use_continue() -> None:
    for i in range (1,11):
        if i == 5 : 
            continue
        else:
            print(i)
    


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    
    for sous_groupe in groups:
        critTaille = len(sous_groupe) > 10 or len(sous_groupe) <= 3
        critÂge = (min(sous_groupe) < 18) or (50 in sous_groupe and max(sous_groupe) > 70)

        if critTaille:
            acceptance.append(False)
            continue
        if 25 in sous_groupe:
            acceptance.append(True)
            continue
        if critÂge:
            acceptance.append(False)
            continue
        acceptance.append(True)
            
    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
