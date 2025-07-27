# Text Adventure Game - Hints 💡

## Stuck? Here are some hints to help you progress!

### General Structure Hints

**Hint 1: Understanding the Game Data**
```python
# Rooms are stored as dictionaries
room = ROOMS[player["location"]]
print(room["name"])        # Room name
print(room["description"])  # Room description
print(room["exits"])        # Available directions
print(room["items"])        # Items in the room
```

**Hint 2: Command Parsing Pattern**
```python
def parse_command(command):
    words = command.strip().lower().split()
    if not words:
        return None, None
    
    action = words[0]
    target = " ".join(words[1:]) if len(words) > 1 else None
    return action, target
```

### Function-Specific Hints

**display_location() Hints:**
```python
def display_location(room_key):
    room = ROOMS[room_key]
    
    # Display room name with decoration
    print(f"\n📍 {room['name']}")
    print("=" * len(room['name']))
    
    # Display description
    print(room['description'])
    
    # Show exits
    exits = list(room['exits'].keys())
    print(f"\nExits: {', '.join(exits)}")
    
    # Show items if any
    if room.get('items', []):
        print(f"\nYou see: {', '.join(room['items'])}")
```

**handle_movement() Hints:**
```python
def handle_movement(direction):
    current_room = ROOMS[player["location"]]
    
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
```

**handle_take() Hints:**
```python
def handle_take(item):
    current_room = ROOMS[player["location"]]
    
    if "items" not in current_room:
        current_room["items"] = []
    
    if item in current_room["items"]:
        current_room["items"].remove(item)
        player["inventory"].append(item)
        print(f"You take the {item}.")
    else:
        print(f"There's no {item} here.")
```

### Game State Management

**Save Game Hints:**
```python
def save_game():
    save_data = {
        "player": player,
        "rooms": ROOMS
    }
    
    try:
        with open("savegame.json", "w") as f:
            json.dump(save_data, f, indent=2)
        print("Game saved!")
    except Exception as e:
        print(f"Failed to save game: {e}")
```

**Load Game Hints:**
```python
def load_game():
    global player, ROOMS
    
    try:
        with open("savegame.json", "r") as f:
            save_data = json.load(f)
        
        player.update(save_data["player"])
        ROOMS.update(save_data["rooms"])
        
        print("Game loaded!")
        display_location(player["location"])
    except FileNotFoundError:
        print("No save game found.")
    except Exception as e:
        print(f"Failed to load game: {e}")
```

### Item Usage

**handle_use() Hints:**
```python
def handle_use(item):
    if item not in player["inventory"]:
        print(f"You don't have a {item}.")
        return
    
    current_room = ROOMS[player["location"]]
    
    # Handle key usage
    if item.endswith("key"):
        used = False
        if "locked" in current_room:
            for direction, required_key in current_room["locked"].items():
                if required_key == item:
                    # Unlock the door
                    del current_room["locked"][direction]
                    print(f"You unlock the {direction} door with the {item}.")
                    used = True
                    break
        
        if not used:
            print(f"You can't use the {item} here.")
    
    # Handle flashlight in dark rooms
    elif item == "flashlight":
        if "dark" in current_room.get("tags", []):
            print("The flashlight illuminates hidden details!")
            # Could reveal hidden items or exits
        else:
            print("The flashlight doesn't reveal anything special here.")
    
    else:
        print(f"You can't use the {item} right now.")
```

### Inventory Management

**handle_inventory() Hints:**
```python
def handle_inventory():
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        print("\n🎒 Your inventory:")
        for i, item in enumerate(player["inventory"], 1):
            print(f"  {i}. {item}")
```

### Win Condition

**check_win_condition() Hints:**
```python
def check_win_condition():
    if "mystic orb" in player["inventory"]:
        player["game_won"] = True
        print("\n🎉 Congratulations! 🎉")
        print("You found the Mystic Orb and escaped the mansion!")
        print("Thanks for playing!")
```

### Common Issues and Solutions

**Issue: Case Sensitivity**
```python
# Always convert commands to lowercase
command = input("> ").strip().lower()

# Also handle item names
item = target.lower() if target else None
```

**Issue: Multi-word Items**
```python
# When parsing commands, join remaining words
target = " ".join(words[1:])  # "small key" not just "small"
```

**Issue: Empty Rooms**
```python
# Always check if keys exist
items = room.get("items", [])
locked = room.get("locked", {})
```

### Debugging Tips

1. **Print game state**:
   ```python
   print(f"Location: {player['location']}")
   print(f"Inventory: {player['inventory']}")
   ```

2. **Validate room data**:
   ```python
   for room_key, room in ROOMS.items():
       print(f"{room_key}: exits={list(room['exits'].keys())}")
   ```

3. **Test command parsing**:
   ```python
   action, target = parse_command("take small key")
   print(f"Action: {action}, Target: {target}")
   ```

### Enhancement Ideas

**Add room tags for special behaviors:**
```python
"dark_room": {
    "name": "Dark Cellar",
    "description": "It's too dark to see anything clearly.",
    "tags": ["dark"],
    "exits": {"up": "kitchen"}
}
```

**Add item descriptions:**
```python
def examine_item(item):
    descriptions = {
        "small key": "A small brass key with intricate engravings.",
        "flashlight": "A heavy-duty flashlight that still works!",
        "mystic orb": "A glowing sphere that pulses with mysterious energy."
    }
    return descriptions.get(item, f"It's a {item}.")
```

**Add room events:**
```python
def enter_room_event(room_key):
    if room_key == "study" and "mystic orb" in ROOMS[room_key].get("items", []):
        print("\n⚡ The orb glows brighter as you enter!")
```

### AI Partnership Hints

**Good prompts to try:**
- "How do I implement a text parser for adventure game commands?"
- "What's a good way to handle locked doors in a text adventure?"
- "How can I make room descriptions more dynamic?"

**Remember:** Start with basic navigation, then add items and puzzles!

