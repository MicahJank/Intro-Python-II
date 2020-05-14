# this file stores and keeps track of the available commands the player can do

commands = {
    "n": "Go North",
    "e": "Go East",
    "s": "Go South",
    "w": "Go West",
    "c": "Look for items",
    "q": "Quit"
}

def print_commands():
    for key, value in commands.items():
        print(f"{key}: {value}")