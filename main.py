from random import choice
import numpy as np
from floor import Floor


########### RANDOM DICE THROW #############


def throw_1d6():
    return np.random.randint(6)+1


def throw_3d6():
    return throw_1d6()+throw_1d6()+throw_1d6()


def throw_1d10():
    return np.random.randint(10)+1


def throw_branch(branches_number, n=3):
    '''
    Branch 1 is n times more likely
    '''
    dice = [1]*n
    for i in range(1, branches_number):
        dice.append(i+1)

    return choice(dice)


############################################

def get_floors_number():
    return throw_3d6()


def get_branches_number(floors_number):

    max_branches_number = floors_number - 4
    branches_number = 0
    while (throw_1d10 >= 7 and branches_number <= max_branches_number):
        branches_number += 1

    return branches_number+1


def breadth_update_level(queue: list, level: int = 1) -> None:
    for floor in queue:
        floor.level = level
        for child in floor.child:
            queue.append(child)
    while queue != []:
        breadth_update_level(queue, level+1)
    return None


def construct_NET():

    ## SET UP ##
    floors_number = get_floors_number()
    branches_number = get_branches_number(floors_number)
    branches = np.empty(branches_number, dtype=list)

    ## Force 1 and 2 to be on branch 0 ##
    branches[0].append(Floor(1, 1))
    branches[0].append(Floor(2, 2))

    ## Force next branches to be at least of one ##
    for branch in range(1, branches_number):
        branches[branch].append(Floor(branch+2, 1))

    # randomly spread floors id in each branch
    for id in range(branches_number+1, floors_number):
        selected_branch = throw_branch(branches_number)
        branches[selected_branch].append(
            Floor(id+1, len(branches[selected_branch])+1))

    # randomly attach branches respecting conditions
    attached = branches[0]
    for branch in range(1, branches_number):
        selected = choice(attached)
        while(selected.id == 1 or selected.id == 2):
            selected = choice(attached)
        selected.add_child(branch[0])
        attached.append(branches(branch))

    # finalize with child depedencies

    for branch in range(branches_number):
        for index in range(1, len(branches[branch])):
            branches[branch][index-1].add_child(branches[branch][index])

    breadth_update_level(branches[0][0])

    return branches.flat()
