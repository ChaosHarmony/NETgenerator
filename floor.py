import numpy as np


class Floor():

    def __init__(self, id: int, level: int) -> None:
        self.id = id
        self.level = level
        self.inside = []
        self.childs = []

    def add_child(self, child_floor):
        '''
        child must be of Floor class
        '''
        try:
            type(child_floor) == type(self)
        except:
            print("Child is not of Floor type")
        else:
            self.childs.append(child_floor)


class NET():

    def __init__(self, floors_list) -> None:
        """
        floors_list is an array like with floors as input
        NET class generalize floor class
        """
        self.n_floors = len(floors_list)
        self.floors = floors_list
        self.depth = max([floors_list[i].level for i in range(self.n_floors)])
        self.id = [floors_list[i].id for i in range(self.n_floors)]

    def id_to_index(self, floor_id):
        return np.where(floor_id == self.id)

    def fill_floor(self, floor_id, data):
        self.floors[self.id_to_index(floor_id)].inside = data
