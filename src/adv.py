from room import Room
from player import Player
from commands import commands, print_commands
import os
import pygame
from item import Item

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
    'outside':  Room("The Outside Gate Entrance",
                     "To the north lies the hidden wizard tower"),

    'foyer':    Room("The Hidden Wizard Tower", """Doesn't look so hidden to me..."""),

    'overlook': Room("The Death Plains", """Think of it like one of those endless runner games, eventually you die."""),

    'narrow':   Room("The Snowy Mountains", """Did you know it snows here?"""),

    'treasure': Room("Dark Forest", """I heard crazy barbarians like to roam around here at night."""),

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
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Link the background images for each room
room['outside'].img = '../assets/gate-sm.png'
room['foyer'].img = '../assets/wizardtower.png'
room['overlook'].img = '../assets/sunsetintheswamp.png'
room['narrow'].img = '../assets/dark forest trees.png'
room['treasure'].img = '../assets/snow_5.png'
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

# the available dialogue
dialogue = [
    "Hello Adventurer...",
     "Before you begin your adventure...",
    "Let me note a few things",
    "1. The developer of this game made this with about a weeks worth or python knowledge",
    "...so yeah, it sucks...",
    "2. You can move in any of the 4 directions by pressing that directions letter on your keyboard",
    "...so for example, if you want to go north press the 'n' key, if you want to go south press the 's' key",
    "You can also quit the game at anytime by pressing the 'q' key",
    "3. Thats it...",
    "What, were you expecting more?",
    "I told you this game sucks didn't I?",
    "Good luck adventurer..."
]

# the current text being displayed to the user
current_dialogue = dialogue[0]

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
                for index, text in enumerate(dialogue):
                    if text == current_dialogue and index + 1 < len(dialogue):
                        next_dialogue = dialogue[index + 1]
               
                if current_dialogue == dialogue[len(dialogue) - 1]:
                    gameActive = True
                    player.current_room = room["outside"] # change to start room
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


# Main game loop
while gameActive:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): # gets the even from the user
        if event.type == pygame.QUIT:
            gameActive = False # game ends when user closes the window
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameActive = False # game ends when user presses q key
            elif event.key == pygame.K_RETURN:
                print("Working")

    screen.fill(BLACK)
    bg_image = pygame.image.load(player.current_room.img)
    # background image
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

