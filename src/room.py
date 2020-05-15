# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, visited=False):
        self.name = name
        self.description = description
        self.visited = visited

    def __str__(self):
        return f'Current Room: {self.name} \n {self.description} \n'