# Write a class to hold player information, e.g. what room they are in
# currently.

import os

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    
    def __str__(self):
        return self.name
    
    def move(self, direction):
        # since every direction has a _to after the direction all i need to do is append the _to to whatever direction
        # has been passed
        next_room_dir = f'{direction}_to'

        try:
            self.current_room = getattr(self.current_room, next_room_dir)
        except:
            print("You cant go that way, try going in a different direction.")
            input('Press any key to continue...')

    def add_item(self, item_to_add):
        self.inventory.append(item_to_add)
        item_to_add.on_take()

    def remove_item(self, item_name):
        for index, item in enumerate(self.inventory):
            if item.name.lower() == item_name.lower():
                removed = self.inventory.pop(index)
                item.on_drop()
                return removed
        print(f"Item {item_name} does not exist in your inventory.")
        return item_name

    
    def print_inventory(self):
        print("Current Items in your inventory: ")
        for item in self.inventory:
            print(item) 

        