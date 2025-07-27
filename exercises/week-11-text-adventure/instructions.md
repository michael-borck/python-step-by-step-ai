# Week 11 Project: Text Adventure Game 🗺️

## Overview

Create an interactive text-based adventure game with rooms, items, and puzzles. This project teaches complex state management, object-oriented thinking, and game design. You'll build a world that players can explore through text commands!

## Learning Objectives

By completing this project, you will:
- ✓ Manage complex game state
- ✓ Design interconnected systems
- ✓ Parse and validate user commands
- ✓ Create engaging narratives
- ✓ Implement save/load functionality

## Core Requirements (🟢 Basic)

Your text adventure must:

1. **Create a game world** with:
   - At least 5 connected rooms
   - Descriptions for each location
   - Clear navigation (north, south, east, west)
   - A simple story/objective

2. **Implement player commands**:
   - Movement: `go north`, `go south`, etc.
   - Look: `look` to see room description
   - Inventory: `inventory` to see items
   - Take/drop: `take key`, `drop sword`
   - Help: `help` for command list

3. **Add interactive elements**:
   - At least 3 items to find and use
   - 1 simple puzzle to solve
   - A win condition

4. **Manage game state**:
   - Player location
   - Inventory
   - Room states (locked/unlocked)
   - Game progress

5. **Save/Load feature**:
   - Save game to file
   - Load previous game

### Example Gameplay
```
🗺️ The Mystery Mansion 🗺️
========================

You wake up in a dusty entrance hall. The air is thick with mystery.
A grand staircase leads up, and doors lead east and west.

> look
You are in the Entrance Hall.
A dusty chandelier hangs overhead. There's a small key on a table.
Exits: north (stairs), east, west

> take key
You pick up the small key.

> inventory
You are carrying:
- small key

> go east
You enter the Library.
Tall bookshelves line the walls. One book seems oddly placed.
A locked door leads south.
Exits: west, south (locked)

> use key
You unlock the southern door with the small key.

> go south
You enter the Secret Study.
A mysterious glowing orb sits on the desk!
This must be what you were looking for!

🎉 Congratulations! You found the Mystic Orb! 🎉
You have won the game!
```

## Implementation Guide

### Step 1: Design Your World
Map out rooms and connections on paper first.

### Step 2: Create Data Structures
Design dictionaries for rooms, items, and game state.

### Step 3: Command Parser
Build system to understand player input.

### Step 4: Game Loop
Create main loop for commands and responses.

### Step 5: Save/Load System
Implement game persistence with files.

## Data Structure Examples

```python
# Room structure
rooms = {
    "entrance": {
        "name": "Entrance Hall",
        "description": "A dusty entrance with a grand staircase.",
        "exits": {"north": "upstairs", "east": "library", "west": "kitchen"},
        "items": ["small key"]
    },
    "library": {
        "name": "Library",
        "description": "Tall bookshelves line the walls.",
        "exits": {"west": "entrance", "south": "study"},
        "locked": {"south": "small key"}
    }
}

# Player state
player = {
    "location": "entrance",
    "inventory": [],
    "game_won": False
}
```

## Challenges

### 🟡 Intermediate Challenges

1. **NPCs**: Add characters with dialogue

2. **Combat System**: Simple health and battles

3. **Multiple Endings**: Different ways to win

4. **Item Combinations**: Combine items to solve puzzles

5. **Score System**: Points for exploration and puzzles

### 🔴 Advanced Challenges

1. **Random Events**: Unexpected occurrences

2. **Time System**: Day/night cycle affecting gameplay

3. **Character Stats**: Strength, intelligence, etc.

4. **Quest Journal**: Track objectives

5. **Procedural Generation**: Randomized dungeon layouts

### 🟣 AI Partnership Challenge

1. **World Building**:
   - Ask AI: "Help me design interesting rooms for a mystery mansion"
   - Get creative puzzle ideas
   - Generate atmospheric descriptions

2. **Command Design**:
   - Learn about text parsing strategies
   - Handle command variations
   - Create natural language understanding

### ⭐ Reflection Exercise

Write a short paragraph answering:
- How did you design your game world to be interesting?
- What was challenging about parsing player commands?
- How did you manage complex game state?
- What makes a text adventure engaging without graphics?

## Testing Your Program

Test these scenarios:
- [ ] All rooms are accessible
- [ ] Items can be taken and dropped
- [ ] Locked doors work properly
- [ ] Invalid commands handled gracefully
- [ ] Game can be won
- [ ] Save/load preserves full state
- [ ] Edge cases (empty inventory, etc.)

## Common Mistakes to Avoid

1. **Hardcoded connections** - Use data structures
2. **No command validation** - Handle typos
3. **Lost player state** - Track everything
4. **Unclear directions** - Good descriptions essential
5. **No way to win** - Test full playthrough

## Command Parsing Tips

```python
def parse_command(command):
    """Parse player input into action and target"""
    words = command.lower().split()
    if not words:
        return None, None
    
    action = words[0]
    target = " ".join(words[1:]) if len(words) > 1 else None
    
    return action, target
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "How should I structure room connections in a text adventure?"
- "What's a good way to parse two-word commands?"
- "How can I make room descriptions more atmospheric?"

### ❌ Avoid These Prompts
- "Create a 3D graphical adventure game"
- "Add voice recognition to my text game"
- "Build an AI that plays the game"

## Save/Load Pattern

```python
import json

def save_game(player, filename="savegame.json"):
    """Save game state to file"""
    with open(filename, 'w') as f:
        json.dump(player, f)
    print("Game saved!")

def load_game(filename="savegame.json"):
    """Load game state from file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
```

## Submission Checklist

Before considering your project complete:
- [ ] At least 5 interconnected rooms
- [ ] Movement commands work properly
- [ ] Items can be collected and used
- [ ] At least one puzzle to solve
- [ ] Clear win condition
- [ ] Save/load functionality works
- [ ] Help command lists all commands
- [ ] Engaging story and descriptions

## Extension Ideas

Once you've completed the basic requirements:
- Add sound effects (text-based)
- Create multiple floors/levels
- Add hidden rooms and secrets
- Implement character dialogue trees
- Create item-based puzzles

## Resources

- Chapter 8: Complex dictionaries
- Chapter 9: File I/O for save/load
- Chapter 12: Game state management
- Classic text adventures for inspiration

---

Remember: Text adventures prove that gameplay beats graphics! Focus on creating an immersive world through words. 📖✨

