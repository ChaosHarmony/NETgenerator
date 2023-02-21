from random import choice
import numpy as np
from floor import Floor, NET


########### RANDOM DICE THROW #############


def roll_1d6():
    return np.random.randint(6)+1


def roll_3d6():
    return roll_1d6()+roll_1d6()+roll_1d6()


def roll_1d10():
    return np.random.randint(10)+1


def roll_branch(branches_number, n=3):
    '''
    Branch 1 is n times more likely
    '''
    dice = [1]*n
    for i in range(1, branches_number):
        dice.append(i+1)

    return choice(dice)


############################################

def get_floors_number():
    return roll_3d6()


def get_branches_number(floors_number):

    max_branches_number = floors_number - 4
    branches_number = 0
    while (roll_1d10() >= 7 and branches_number <= max_branches_number):
        branches_number += 1

    return branches_number+1


def breadth_first_update_level(queue: list, level: int = 1):

    new_queue = []
    for floor in queue:
        floor.level = level
        for child in floor.children:
            new_queue.append(child)

    if new_queue != []:
        breadth_first_update_level(new_queue, level+1)
    return None


def construct_NET():

    ## SET UP ##
    floors_number = get_floors_number()
    branches_number = get_branches_number(floors_number)
    all_floor = np.empty(floors_number, dtype=object)
    bottom_branch = []
    # Filling the NET
    for id in range(floors_number):
        all_floor[id] = Floor(id+1, 1)

    # root of the tree
    all_floor[0].add_child(all_floor[1])
    all_floor[1].add_child(all_floor[2])

    bottom_branch.append(all_floor[2])
    # forcing one floor in each branch :
    for branch in range(1, branches_number):
        all_floor[2].add_child(all_floor[branch+2])
        bottom_branch.append(all_floor[branch+2])

    # choosing randomly where nods goes in which branch
    for id in range(branches_number+2, floors_number):
        selected_branch = roll_branch(branches_number)-1
        parent_of_current_floor = bottom_branch[selected_branch]
        parent_of_current_floor.add_child(all_floor[id])
        bottom_branch[selected_branch] = all_floor[id]

    breadth_first_update_level([all_floor[0]])

    return all_floor

    ################################################ TESTING RANGE ##########################################


if __name__ == "__main__":
    print("------------------------------------")
    print("Welcome to testing range")
    print("------------------------------------")

    root1 = Floor(1, 1)
    node2 = Floor(2, 1)
    node3 = Floor(3, 1)
    branche4 = Floor(4, 1)
    branche5 = Floor(5, 1)
    node6 = Floor(6, 1)

    root1.add_child(node2)
    node2.add_child(node3)
    node3.add_child(node6)
    node3.add_child(branche4)
    branche4.add_child(branche5)

    print("number 3 childs : ", node3.children)
    breadth_first_update_level([root1])
    tab = [root1.level, node2.level, node3.level,
           branche4.level, branche5.level, node6.level]
    print('node 1,2,3,4,5,6 levels = ', tab)
    print('is correct : ', tab == [1, 2, 3, 4, 5, 4])

    for i in range(3):
        Net = NET(construct_NET())
        print("Net is of number of floor : ", Net.n_floors)
        print("Net is deep of :", Net.depth)
        print("Net id is :", Net.id)
        print("Net has children :", Net.children_id)
