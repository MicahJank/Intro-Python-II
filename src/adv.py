from room import Room
from player import Player
from item import Item
from commands import commands, print_commands
import os

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items
gold_coins = Item("Coins", "Ever wonder who coined the term coined? - Yeah me neither...")
long_sword = Item("Longsword", "It's a sword and its uh...long.")
potato_sack = Item("PotatoSack", "This thing is heavier than it looks...")
wizard_hat = Item("Hat", "A wizard hat, if you put it on...does that make you a wizard?")
rocks = Item("Rocks", "Not really sure why you need these...?")
ring = Item("Ring", "There are markings on the ring...its some form of Elvish, you cant read it.")


# Add Items to rooms
room['outside'].items = [gold_coins, rocks]
room['foyer'].items = [long_sword]
room['overlook'].items = [potato_sack]
room['narrow'].items = [wizard_hat]
room['treasure'].items = [ring]

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Player", room["outside"])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

selection = 0
# Main game loop
while selection != 'q':
    print(player.current_room)
    print("What would you like to do?")
    print_commands()

    selection = input("Enter Command: ")

    if selection == "n" or selection == "e" or selection == "s" or selection == "w":
        player.move(selection)
    elif selection == "q":
        print("Exiting...so long Adventurer...")
        input('Press any key to continue...')
        os.system('clear')
    elif selection == "c":
        print("You scout the area for hidden treasures...")
        input('Press any key to continue...')
        player.current_room.print_items()
    else:
        print("Please make sure you are choosing a valid command.")
        input('Press any key to continue...')
        os.system('clear')

    os.system('clear')
