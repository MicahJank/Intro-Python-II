from room import Room
from player import Player
from commands import commands, print_commands
import os
import pygame

pygame.init()

# controls the update rate of the game screen
clock = pygame.time.Clock()

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Legend of Lambda")

# will determine when the game is running or when it should close the game window
gameActive = True

# defined colors
BLACK = ( 0, 0, 0)
RED = ( 255, 0, 0)
WHITE = ( 255, 255, 255)

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
while gameActive:
    for event in pygame.event.get(): # gets the even from the user
        if event.type == pygame.QUIT:
            gameActive = False # game ends when user quits
    
    # screen should start out initially black
    screen.fill(BLACK)


    pygame.display.flip()

    clock.tick(60)

    # print(player.current_room)
    # print("What would you like to do?")
    # print_commands()

    # selection = input("Enter Command: ")

    # if selection == "n" or selection == "e" or selection == "s" or selection == "w":
    #     player.move(selection)
    # elif selection == "q":
    #     print("Exiting...so long Adventurer...")
    #     input('Press any key to continue...')
    #     os.system('clear')
    # else:
    #     print("Please make sure you are choosing a valid command.")
    #     input('Press any key to continue...')
    #     os.system('clear')

    # os.system('clear')
       
# after game ends we can stop the game engine
pygame.quit()

