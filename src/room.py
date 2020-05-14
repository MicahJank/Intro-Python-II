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

    # removes the passed in item from the item list, if it exists
    def remove_item(self, item_name):
        for index, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                # rather than just removing the item i decided to use the pop method since it returns the removed item
                # this is useful because after removing the item here i would like to add it to the players inventory in
                # adv.py - returning the removed item here will make that much simpler
                removed = self.items.pop(index)
                return removed
        print(f"Item {item_name} is not in the room.")
        return item_name
                

    def add_item(self, item_to_add):
        self.items.append(item_to_add)

                
