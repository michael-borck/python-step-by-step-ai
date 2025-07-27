#!/usr/bin/env python3
"""
Week 1 Project: Fortune Teller - Intermediate Solution
This solution adds lucky numbers and fortune categories.
"""

import random

# Create different categories of fortunes
love_fortunes = [
    "Love is in the air! Keep your heart open.",
    "A meaningful connection will deepen soon.",
    "Someone appreciates you more than you know."
]

career_fortunes = [
    "Your hard work is about to pay off big time!",
    "A new opportunity will present itself this month.",
    "Your skills will be recognized and rewarded."
]

general_fortunes = [
    "Adventure awaits those who seek it!",
    "A mystery will be solved in unexpected ways.",
    "Your positive energy attracts good things."
]

# Combine all fortunes for random selection
all_fortunes = love_fortunes + career_fortunes + general_fortunes

# Fortune teller introduction
print("="*50)
print("🔮 Madame Mystique's Fortune Telling Parlor 🔮")
print("="*50)
print()
print("Welcome, seeker of wisdom!")
print("The cosmic energies are aligning...")
print()

# Select and display fortune
chosen_fortune = random.choice(all_fortunes)
print("⭐ The stars reveal: ⭐")
print()
print("    " + chosen_fortune)
print()

# Add lucky numbers
print("🎲 Your lucky numbers for today: ", end="")
lucky_numbers = []
for i in range(3):
    number = random.choice(range(1, 50))
    lucky_numbers.append(str(number))
print(" - ".join(lucky_numbers))
print()

# Mystical closing
print("✨ Remember: You hold the power to shape your destiny! ✨")
print("="*50)

"""
Intermediate Concepts Used:
- Multiple lists that get combined with +
- More elaborate formatting with "="*50
- Using end="" in print to keep output on same line
- Creating a list of lucky numbers with a loop
- Using .join() to display numbers nicely
- Added fortune teller personality
"""