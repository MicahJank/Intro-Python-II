# Write a class to hold player information, e.g. what room they are in
# currently.

import os

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
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

        