import numpy as np


########### RANDOM DICE THROW #############


def throw_1d6():
    return np.random.randint(6)+1


def throw_3d6():
    return throw_1d6()+throw_1d6()+throw_1d6()


def throw_1d10():
    return np.random.randint(10)+1


############################################

def get_floors_number():
    return throw_3d6()


def get_branches_number(floors_number):

    max_branches_number = floors_number - 4
    branches_number = 0
    while (throw_1d10 >= 7 and branches_number <= max_branches_number):
        branches_number += 1

    return branches_number
