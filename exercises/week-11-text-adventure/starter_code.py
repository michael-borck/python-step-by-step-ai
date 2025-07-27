#!/usr/bin/env python3
"""
Text Adventure Game - Starter Code
Week 11 Project

TODO: Create an interactive text-based adventure game
"""

import json

# Game world data structure
ROOMS = {
    "entrance": {
        "name": "Entrance Hall",
        "description": "A dusty entrance hall with a grand staircase. Sunlight filters through dirty windows.",
        "exits": {"north": "upstairs", "east": "library", "west": "kitchen"},
        "items": ["small key"]
    },
    "library": {
        "name": "Library", 
        "description": "Tall bookshelves line the walls. One book seems oddly placed.",
        "exits": {"west": "entrance", "south": "study"},
        "items": [],
        "locked": {"south": "small key"}
    },
    "kitchen": {
        "name": "Kitchen",
        "description": "An old kitchen with rusty pots and pans. A door leads north.",
        "exits": {"east": "entrance", "north": "pantry"},
        "items": ["flashlight"]
    },
    "upstairs": {
        "name": "Upstairs Landing",
        "description": "A creaky upstairs landing. Doors lead east and west.",
        "exits": {"south": "entrance", "east": "bedroom", "west": "bathroom"},
        "items": []
    },
    "study": {
        "name": "Secret Study",
        "description": "A hidden study with ancient books. A glowing orb sits on the desk!",
        "exits": {"north": "library"},
        "items": ["mystic orb"]
    }
}

# Player state
player = {
    "location": "entrance",
    "inventory": [],
    "game_won": False
}

def display_location(room_key):
    """Display current room information"""
    # TODO: Get room data
    # TODO: Display room name and description
    # TODO: Show available exits
    # TODO: Show items in room
    pass

def parse_command(command):
    """Parse player input into action and target"""
    # TODO: Split command into words
    # TODO: Extract action (first word)
    # TODO: Extract target (remaining words)
    # TODO: Handle empty input
    return None, None

def handle_movement(direction):
    """Handle player movement"""
    # TODO: Get current room
    # TODO: Check if direction is valid
    # TODO: Check if exit is locked
    # TODO: Move player to new room
    # TODO: Display new location
    pass

def handle_take(item):
    """Handle taking an item"""
    # TODO: Get current room
    # TODO: Check if item exists in room
    # TODO: Add item to inventory
    # TODO: Remove item from room
    # TODO: Display success message
    pass

def handle_drop(item):
    """Handle dropping an item"""
    # TODO: Check if item is in inventory
    # TODO: Remove from inventory
    # TODO: Add to current room
    # TODO: Display success message
    pass

def handle_use(item):
    """Handle using an item"""
    # TODO: Check if item is in inventory
    # TODO: Handle specific item uses (keys for doors)
    # TODO: Update game state if needed
    # TODO: Display result
    pass

def handle_inventory():
    """Display player inventory"""
    # TODO: Check if inventory is empty
    # TODO: Display all items in inventory
    pass

def handle_look():
    """Look around current room"""
    # TODO: Display current location details
    pass

def handle_help():
    """Display available commands"""
    print("\nAvailable commands:")
    print("- go <direction>: Move north, south, east, or west")
    print("- take <item>: Pick up an item")
    print("- drop <item>: Drop an item from inventory")
    print("- use <item>: Use an item")
    print("- inventory: Show your items")
    print("- look: Look around")
    print("- help: Show this help")
    print("- save: Save game")
    print("- load: Load game")
    print("- quit: Exit game")

def save_game():
    """Save game state to file"""
    # TODO: Create save data dictionary
    # TODO: Write to JSON file
    # TODO: Handle file errors
    pass

def load_game():
    """Load game state from file"""
    # TODO: Try to read save file
    # TODO: Parse JSON data
    # TODO: Update player state
    # TODO: Handle file not found
    pass

def check_win_condition():
    """Check if player has won the game"""
    # TODO: Check if mystic orb is in inventory
    # TODO: Update game_won status
    # TODO: Display win message
    pass

def game_loop():
    """Main game loop"""
    print("🗺️ The Mystery Mansion 🗺️")
    print("========================")
    print("\nYou wake up in a dusty entrance hall. The air is thick with mystery.")
    print("Type 'help' for commands.")
    
    # Display starting location
    display_location(player["location"])
    
    while not player["game_won"]:
        # TODO: Get user input
        # TODO: Parse command
        # TODO: Handle different actions
        # TODO: Check win condition
        # TODO: Handle quit command
        
        command = input("\n> ").strip().lower()
        
        if not command:
            continue
            
        action, target = parse_command(command)
        
        if action == "go":
            if target:
                handle_movement(target)
            else:
                print("Go where? (north, south, east, west)")
                
        elif action == "take":
            if target:
                handle_take(target)
            else:
                print("Take what?")
                
        elif action == "drop":
            if target:
                handle_drop(target)
            else:
                print("Drop what?")
                
        elif action == "use":
            if target:
                handle_use(target)
            else:
                print("Use what?")
                
        elif action == "inventory":
            handle_inventory()
            
        elif action == "look":
            handle_look()
            
        elif action == "help":
            handle_help()
            
        elif action == "save":
            save_game()
            
        elif action == "load":
            load_game()
            
        elif action == "quit":
            print("\nThanks for playing!")
            break
            
        else:
            print("I don't understand that command. Type 'help' for commands.")
        
        # Check if player won
        check_win_condition()

def main():
    """Main program"""
    try:
        game_loop()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")

if __name__ == "__main__":
    main()

