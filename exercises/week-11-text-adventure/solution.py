#!/usr/bin/env python3
"""
Text Adventure Game - Complete Solution
Week 11 Project

This solution implements an interactive text-based adventure game
with save/load functionality and inventory management.
"""

import json
import os
from datetime import datetime

# Game world data structure
ROOMS = {
    "entrance": {
        "name": "Entrance Hall",
        "description": "A dusty entrance hall with a grand staircase. Sunlight filters through dirty windows.",
        "exits": {"north": "upstairs", "east": "library", "west": "kitchen"},
        "items": ["small key", "dusty book"]
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
        "items": ["flashlight", "apple"]
    },
    "pantry": {
        "name": "Pantry",
        "description": "A small pantry with empty shelves. It's very dark here.",
        "exits": {"south": "kitchen"},
        "items": ["golden key"],
        "tags": ["dark"]
    },
    "upstairs": {
        "name": "Upstairs Landing",
        "description": "A creaky upstairs landing. Doors lead east and west.",
        "exits": {"south": "entrance", "east": "bedroom", "west": "bathroom"},
        "items": []
    },
    "bedroom": {
        "name": "Master Bedroom",
        "description": "A large bedroom with a four-poster bed. A painting hangs crooked on the wall.",
        "exits": {"west": "upstairs", "north": "secret_passage"},
        "items": ["silver coin"],
        "locked": {"north": "golden key"},
        "hidden_exits": {"north": "secret_passage"}  # Hidden until painting is examined
    },
    "bathroom": {
        "name": "Bathroom",
        "description": "An old bathroom with a clawfoot tub. The mirror is cracked.",
        "exits": {"east": "upstairs"},
        "items": ["soap"]
    },
    "study": {
        "name": "Secret Study",
        "description": "A hidden study with ancient books. A glowing orb sits on the desk!",
        "exits": {"north": "library"},
        "items": ["mystic orb", "ancient scroll"]
    },
    "secret_passage": {
        "name": "Secret Passage",
        "description": "A narrow passage behind the bedroom wall. It leads to a hidden vault.",
        "exits": {"south": "bedroom", "east": "vault"},
        "items": [],
        "tags": ["dark"]
    },
    "vault": {
        "name": "Hidden Vault",
        "description": "A secret vault filled with treasures! Gold coins sparkle in the darkness.",
        "exits": {"west": "secret_passage"},
        "items": ["treasure chest", "ancient crown"],
        "tags": ["dark"]
    }
}

# Player state
player = {
    "location": "entrance",
    "inventory": [],
    "game_won": False,
    "moves": 0,
    "score": 0,
    "discovered_rooms": ["entrance"],
    "examined": []  # Track what has been examined
}

# Item descriptions
ITEM_DESCRIPTIONS = {
    "small key": "A small brass key with intricate engravings.",
    "dusty book": "An old book about the mansion's history. It mentions hidden passages.",
    "flashlight": "A heavy-duty flashlight that still works!",
    "apple": "A surprisingly fresh apple. Still edible!",
    "golden key": "An ornate golden key that looks important.",
    "silver coin": "An ancient silver coin with mysterious symbols.",
    "soap": "A bar of lavender-scented soap.",
    "mystic orb": "A glowing sphere that pulses with mysterious energy.",
    "ancient scroll": "A scroll with cryptic writing. It seems to be a map.",
    "treasure chest": "A heavy chest filled with gold coins!",
    "ancient crown": "A jeweled crown that once belonged to royalty."
}

# Item values for scoring
ITEM_VALUES = {
    "silver coin": 10,
    "mystic orb": 50,
    "ancient scroll": 20,
    "treasure chest": 100,
    "ancient crown": 75,
    "apple": 5
}

def clear_screen():
    """Clear the console screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_location(room_key):
    """Display current room information"""
    room = ROOMS[room_key]
    
    # Add to discovered rooms
    if room_key not in player["discovered_rooms"]:
        player["discovered_rooms"].append(room_key)
        player["score"] += 10  # Points for discovering new room
    
    print(f"\n📍 {room['name']}")
    print("=" * (len(room['name']) + 3))
    
    # Check if room is dark and player has no light
    if "dark" in room.get("tags", []) and "flashlight" not in player["inventory"]:
        print("It's too dark to see anything clearly!")
        print("You might need a light source...")
    else:
        print(room['description'])
    
    # Show exits
    exits = list(room['exits'].keys())
    # Don't show hidden exits unless discovered
    if room_key == "bedroom" and "painting" not in player["examined"]:
        if "north" in exits:
            exits.remove("north")
    
    print(f"\nExits: {', '.join(exits)}")
    
    # Show items if room is lit
    if "dark" not in room.get("tags", []) or "flashlight" in player["inventory"]:
        if room.get('items', []):
            print(f"You see: {', '.join(room['items'])}")

def parse_command(command):
    """Parse player input into action and target"""
    words = command.strip().lower().split()
    if not words:
        return None, None
    
    action = words[0]
    target = " ".join(words[1:]) if len(words) > 1 else None
    
    # Handle command aliases
    aliases = {
        "n": "go north",
        "s": "go south",
        "e": "go east",
        "w": "go west",
        "i": "inventory",
        "l": "look",
        "get": "take",
        "grab": "take",
        "check": "examine",
        "inspect": "examine"
    }
    
    if action in aliases:
        if action in ["n", "s", "e", "w"]:
            parts = aliases[action].split()
            return parts[0], parts[1]
        else:
            return aliases[action], target
    
    return action, target

def handle_movement(direction):
    """Handle player movement"""
    current_room = ROOMS[player["location"]]
    player["moves"] += 1
    
    # Check if direction is valid
    if direction not in current_room["exits"]:
        print(f"You can't go {direction} from here.")
        return
    
    # Check if exit is locked
    if "locked" in current_room:
        if direction in current_room["locked"]:
            required_key = current_room["locked"][direction]
            if required_key not in player["inventory"]:
                print(f"The {direction} door is locked. You need a {required_key}.")
                return
    
    # Move to new room
    new_room = current_room["exits"][direction]
    player["location"] = new_room
    display_location(new_room)

def handle_take(item):
    """Handle taking an item"""
    current_room = ROOMS[player["location"]]
    
    # Check if room is dark
    if "dark" in current_room.get("tags", []) and "flashlight" not in player["inventory"]:
        print("It's too dark to see what you're grabbing!")
        return
    
    if "items" not in current_room:
        current_room["items"] = []
    
    if item in current_room["items"]:
        current_room["items"].remove(item)
        player["inventory"].append(item)
        print(f"You take the {item}.")
        
        # Add score for valuable items
        if item in ITEM_VALUES:
            player["score"] += ITEM_VALUES[item]
            print(f"[+{ITEM_VALUES[item]} points]")
    else:
        print(f"There's no {item} here.")

def handle_drop(item):
    """Handle dropping an item"""
    if item not in player["inventory"]:
        print(f"You don't have a {item}.")
        return
    
    player["inventory"].remove(item)
    current_room = ROOMS[player["location"]]
    
    if "items" not in current_room:
        current_room["items"] = []
    
    current_room["items"].append(item)
    print(f"You drop the {item}.")

def handle_use(item):
    """Handle using an item"""
    if item not in player["inventory"]:
        print(f"You don't have a {item}.")
        return
    
    current_room = ROOMS[player["location"]]
    
    # Handle key usage
    if item.endswith("key"):
        used = False
        if "locked" in current_room:
            for direction, required_key in list(current_room["locked"].items()):
                if required_key == item:
                    # Unlock the door
                    del current_room["locked"][direction]
                    print(f"You unlock the {direction} door with the {item}.")
                    player["score"] += 20
                    used = True
                    break
        
        if not used:
            print(f"You can't use the {item} here.")
    
    # Handle flashlight in dark rooms
    elif item == "flashlight":
        if "dark" in current_room.get("tags", []):
            print("The flashlight illuminates the room!")
            display_location(player["location"])
        else:
            print("The flashlight doesn't reveal anything special here.")
    
    # Handle eating apple
    elif item == "apple":
        print("You eat the apple. It's surprisingly refreshing!")
        print("[+5 health]")
        player["inventory"].remove(item)
        player["score"] += 5
    
    # Handle reading items
    elif item in ["dusty book", "ancient scroll"]:
        handle_examine(item)
    
    else:
        print(f"You can't use the {item} right now.")

def handle_examine(item):
    """Examine an item or object"""
    # Check inventory first
    if item in player["inventory"]:
        desc = ITEM_DESCRIPTIONS.get(item, f"It's a {item}.")
        print(desc)
        
        # Special examination results
        if item == "ancient scroll" and item not in player["examined"]:
            print("\nThe scroll reveals the location of a hidden vault!")
            print("It mentions a secret passage behind a painting...")
            player["examined"].append(item)
            player["score"] += 10
        
        return
    
    # Check current room
    current_room = ROOMS[player["location"]]
    if item in current_room.get("items", []):
        desc = ITEM_DESCRIPTIONS.get(item, f"It's a {item}.")
        print(desc)
        return
    
    # Special examinations
    if player["location"] == "bedroom" and item == "painting":
        print("You examine the crooked painting...")
        print("Behind it, you discover a hidden door to the north!")
        player["examined"].append("painting")
        player["score"] += 15
        display_location(player["location"])
    else:
        print(f"You don't see a {item} here.")

def handle_inventory():
    """Display player inventory"""
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        print("\n🎒 Your inventory:")
        for i, item in enumerate(player["inventory"], 1):
            value_str = f" ({ITEM_VALUES[item]} points)" if item in ITEM_VALUES else ""
            print(f"  {i}. {item}{value_str}")
        print(f"\nTotal items: {len(player['inventory'])}")

def handle_look():
    """Look around current room"""
    display_location(player["location"])

def handle_help():
    """Display available commands"""
    print("\n📖 Available commands:")
    print("- go <direction>: Move north, south, east, or west (or just n/s/e/w)")
    print("- take <item>: Pick up an item")
    print("- drop <item>: Drop an item from inventory")
    print("- use <item>: Use an item")
    print("- examine <item/object>: Look at something closely")
    print("- inventory/i: Show your items")
    print("- look/l: Look around")
    print("- score: Show your current score")
    print("- help: Show this help")
    print("- save: Save game")
    print("- load: Load game")
    print("- quit: Exit game")

def handle_score():
    """Display current score and statistics"""
    print(f"\n🏆 Current Score: {player['score']} points")
    print(f"📍 Rooms discovered: {len(player['discovered_rooms'])}/{len(ROOMS)}")
    print(f"🚶 Moves made: {player['moves']}")
    print(f"🎒 Items collected: {len(player['inventory'])}")

def save_game():
    """Save game state to file"""
    save_data = {
        "player": player,
        "rooms": ROOMS,
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        with open("savegame.json", "w") as f:
            json.dump(save_data, f, indent=2)
        print("✅ Game saved successfully!")
        print(f"[Score: {player['score']}, Moves: {player['moves']}]")
    except Exception as e:
        print(f"❌ Failed to save game: {e}")

def load_game():
    """Load game state from file"""
    global player, ROOMS
    
    try:
        with open("savegame.json", "r") as f:
            save_data = json.load(f)
        
        player.update(save_data["player"])
        ROOMS.update(save_data["rooms"])
        
        timestamp = save_data.get("timestamp", "Unknown")
        print(f"✅ Game loaded successfully!")
        print(f"[Saved: {timestamp}]")
        display_location(player["location"])
    except FileNotFoundError:
        print("❌ No save game found.")
    except Exception as e:
        print(f"❌ Failed to load game: {e}")

def check_win_condition():
    """Check if player has won the game"""
    valuable_items = ["mystic orb", "treasure chest", "ancient crown"]
    items_collected = sum(1 for item in valuable_items if item in player["inventory"])
    
    if items_collected >= 2:  # Need at least 2 valuable items
        player["game_won"] = True
        print("\n" + "=" * 50)
        print("🎉 CONGRATULATIONS! 🎉")
        print("=" * 50)
        print(f"\nYou've collected enough treasures to win!")
        print(f"Final Score: {player['score']} points")
        print(f"Total Moves: {player['moves']}")
        print(f"Rooms Discovered: {len(player['discovered_rooms'])}/{len(ROOMS)}")
        print("\nThanks for playing The Mystery Mansion!")
        print("=" * 50)

def game_loop():
    """Main game loop"""
    clear_screen()
    print("🗺️  THE MYSTERY MANSION 🗺️")
    print("=" * 30)
    print("\nYou wake up in a dusty entrance hall.")
    print("The air is thick with mystery...")
    print("\nYour goal: Collect valuable treasures and escape!")
    print("Type 'help' for commands.")
    
    # Display starting location
    display_location(player["location"])
    
    while not player["game_won"]:
        try:
            # Get user input
            command = input("\n> ").strip().lower()
            
            if not command:
                continue
            
            # Parse command
            action, target = parse_command(command)
            
            # Handle commands
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
                    
            elif action == "examine":
                if target:
                    handle_examine(target)
                else:
                    print("Examine what?")
                    
            elif action == "inventory":
                handle_inventory()
                
            elif action == "look":
                handle_look()
                
            elif action == "score":
                handle_score()
                
            elif action == "help":
                handle_help()
                
            elif action == "save":
                save_game()
                
            elif action == "load":
                load_game()
                
            elif action == "quit":
                confirm = input("Are you sure you want to quit? (yes/no): ").lower()
                if confirm == "yes" or confirm == "y":
                    print("\nThanks for playing! Your adventure ends here...")
                    print(f"Final Score: {player['score']} points")
                    break
                    
            else:
                print("I don't understand that command. Type 'help' for commands.")
            
            # Check if player won
            check_win_condition()
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted.")
            save = input("Would you like to save before exiting? (yes/no): ").lower()
            if save == "yes" or save == "y":
                save_game()
            print("Goodbye!")
            break

def main():
    """Main program"""
    try:
        game_loop()
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("The game will now exit.")

if __name__ == "__main__":
    main()