class Floor():

    def __init__(self, level) -> None:
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
