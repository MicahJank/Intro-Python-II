# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'Current Room: {self.name} \n {self.description} \n'

    # items is a list of items in the room so we can loop over that list and print out the items individually
    # what gets printed will be determined by whatever __str__ method i defined in the item.py
    def print_items(self):
        print(f"Current Items in {self.name}: ")
        for item in self.items:
            print(item)