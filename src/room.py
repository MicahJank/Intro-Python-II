# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = "There is nothing to the north"
        self.e_to = "There is nothing to the east"
        self.s_to = "There is nothing to the south"
        self.w_to = "There is nothing to the west"

    def __str__(self):
        return f'Current Room: {self.name} \n {self.description}'