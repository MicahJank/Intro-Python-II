from room import Room
from player import Player
from commands import commands, print_commands
import os
import pygame
from item import Item
from dialogue import *

pygame.init()

# controls the update rate of the game screen
clock = pygame.time.Clock()

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Legend of Lambda")

# will determine when the game is running or when it should close the game window
gameActive = False

# in the beginning the user shouldnt be able to do the normal commands so i need to set this to
# keep track of where they are in the game loop
start_scene = True

# a while loop for dialogue is needs since i dont want the user to be moving between rooms when dialogue is happening
dialogue_loop = False

# different scenes need different dialogue - there should be a boolean value for each that can set off those different dialogues
gate_scene = False
wizard_tower_scene = False
death_plains_scene = False
snow_mountains_scene = False
dark_forest_scene = False


# defined colors
BLACK = ( 0, 0, 0)
RED = ( 255, 0, 0)
WHITE = ( 255, 255, 255)
TEXT_COLOR = (255,255,0)

# define images
bg_image = pygame.image.load('../assets/skeletonbg.png')

# font for the game
font = pygame.font.Font('freesansbold.ttf', 24)

# Declare all the rooms
room = {
    'gate':  Room("The Outside Gate Entrance",
                     "To the north lies the hidden wizard tower"),

    'wizard_tower':    Room("The Hidden Wizard Tower", """Doesn't look so hidden to me..."""),

    'death_plains': Room("The Death Plains", """Think of it like one of those endless runner games, eventually you die."""),

    'snow_mountains':   Room("The Snowy Mountains", """Did you know it snows here?"""),

    'dark_forest': Room("Dark Forest", """I heard crazy barbarians like to roam around here at night."""),

    'gamestart': Room("Start of The Game",
                        "Your adventure awaits...")
}


# Declare all items
gold_coins = Item("Coins", "Ever wonder who coined the term coined? - Yeah me neither...")
long_sword = Item("Longsword", "It's a sword and its uh...long.")
potato_sack = Item("PotatoSack", "This thing is heavier than it looks...")
wizard_hat = Item("Hat", "A wizard hat, if you put it on...does that make you a wizard?")
rocks = Item("Rocks", "Not really sure why you need these...?")
ring = Item("Ring", "There are markings on the ring...its some form of Elvish, you cant read it.")


# Link rooms together
room['gate'].n_to = room['wizard_tower']
room['wizard_tower'].s_to = room['gate']
room['wizard_tower'].n_to = room['death_plains']
room['death_plains'].s_to = room['wizard_tower']
room['wizard_tower'].e_to = room['snow_mountains']
room['snow_mountains'].w_to = room['wizard_tower']
room['wizard_tower'].w_to = room['dark_forest']
room['dark_forest'].e_to = room['wizard_tower']


# Link the background images for each room
room['gate'].img = '../assets/gate-sm.png'
room['wizard_tower'].img = '../assets/wizardtower.png'
room['death_plains'].img = '../assets/sunsetintheswamp.png'
room['snow_mountains'].img = '../assets/dark forest trees.png'
room['dark_forest'].img = '../assets/snow_5.png'
room['gamestart'].img = '../assets/skeletonbg.png'

#
# Main
#

# function that will write the text to the screen
def write(text, location=(70, 430), color=(TEXT_COLOR)):
    if len(text) >= 49:
        line1 = text[0:49]
        line2 = text[49:]
        screen.blit(font.render(line1, True, color), location)
        screen.blit(font.render(line2, True, color), (70, 460))
    else:
        screen.blit(font.render(text, True, color), location)
    

# Make a new player object that is currently in the 'outside' room.
player = Player("Player", room["gamestart"])

# the current text being displayed to the user
current_dialogue = start_dialogue[0]

# start scene
while start_scene:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): # gets the even from the user
        if event.type == pygame.QUIT:
            start_scene = False # game ends when user closes the window
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                start_scene = False # game ends when user presses q key
            elif event.key == pygame.K_RETURN:
                next_dialogue = ''
                for index, text in enumerate(start_dialogue):
                    if text == current_dialogue and index + 1 < len(start_dialogue):
                        next_dialogue = start_dialogue[index + 1]
               
                if current_dialogue == start_dialogue[len(start_dialogue) - 1]:
                    gameActive = True
                    player.current_room = room["gate"] # change to start room
                    start_scene = False
                current_dialogue = next_dialogue
                       



    # screen should start out initially black
    screen.fill(BLACK)
    bg_image = pygame.image.load(player.current_room.img)
    # background image
    screen.blit(bg_image, (0,0))
    pygame.draw.rect(screen, BLACK, [10, 400, 680, 90], 0)

    # writes the dialogue to the screen
    write(current_dialogue)
        

    pygame.display.flip()

    clock.tick(60)

# dialogue loop
# while dialogue_loop:
    


# check key inputs from player
def check_keydown_input(key):
    if key == pygame.K_q:
        gameActive = False # game ends when user presses q key
    elif key == pygame.K_RETURN:
        print("Working")
    elif key == pygame.K_n or key == pygame.K_s or key == pygame.K_w or key == pygame.K_e:
        # player.move needs a string representation of the key - NOT a keycode
        player.move(pygame.key.name(key))

# Main game loop
while gameActive:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): # gets the even from the user
        if event.type == pygame.QUIT:
            gameActive = False # game ends when user closes the window
        elif event.type == pygame.KEYDOWN:
            check_keydown_input(event.key)
            
    screen.fill(BLACK)
    # background image
    bg_image = pygame.image.load(player.current_room.img)
    screen.blit(bg_image, (0,0))



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

