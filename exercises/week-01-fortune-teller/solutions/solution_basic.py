#!/usr/bin/env python3
"""
Week 1 Project: Fortune Teller - Basic Solution
This solution meets all core requirements using only Week 1 concepts.
"""

# Import random to select fortunes randomly
import random

# Create a list of fortunes
fortunes = [
    "A pleasant surprise will come your way soon!",
    "Your persistence will lead to success.",
    "An exciting opportunity awaits around the corner.",
    "Someone special is thinking of you right now.",
    "Your creative talents will shine this week.",
    "Good news will arrive in an unexpected way.",
    "A small act of kindness will bring great joy."
]

# Welcome message
print("🔮 Welcome to the Mystic Fortune Teller! 🔮")
print()
print("Let me gaze into the crystal ball...")
print()

# Select a random fortune
chosen_fortune = random.choice(fortunes)

# Display the fortune
print("✨ Your fortune: " + chosen_fortune + " ✨")
print()

# Closing message
print("May the stars guide your path!")

"""
Learning Notes:
- We import random at the top to use its functions
- The fortune list contains 7 different string messages
- random.choice() randomly selects one item from the list
- We use print() with empty parentheses for blank lines
- String concatenation (+) combines text with our fortune
- Emojis make the output more engaging
"""