# this file stores and keeps track of the available commands the player can do

commands = {
    "n": "Go North",
    "e": "Go East",
    "s": "Go South",
    "w": "Go West",
    "c": "Look for items",
    "take/get [item name]": "Take the item if its in the room",
    "drop [item name]": "Drop the item if it is in your inventory",
    "i/inventory": "Check what items are in your inventory",
    "q": "Quit"
}

def print_commands():
    for key, value in commands.items():
        print(f"{key}: {value}")