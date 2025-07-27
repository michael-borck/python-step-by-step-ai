#!/usr/bin/env python3
"""
Week 2 Project: Mad Libs Generator - Basic Solution
This solution meets all core requirements using only Week 2 concepts.
"""

# Welcome message
print("🎭 Welcome to Mad Libs! 🎭")
print("\nI'll ask you for some words, then create a silly story!")
print()

# Collect 8 different words from the user
# Nouns (2)
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")

# Verbs (2)
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")

# Adjectives (2)
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")

# Other types (2)
animal = input("Enter an animal: ")
place = input("Enter a place: ")

# Display the story
print("\nHere's your Mad Libs story:\n")
print("The " + adjective1 + " " + animal + " Adventure")
print("=" * 40)
print()

# Story using all collected words
print("Once upon a time, a " + adjective1 + " " + animal + " wanted to " + verb1 + ".")
print("It packed its " + adjective2 + " " + noun1 + " and headed to the " + place + ".")
print("On the way, it met a " + noun2 + " who liked to " + verb2 + ".")
print("Together, they had the most " + adjective2 + " adventure ever!")
print()

# Closing message
print("Thanks for playing Mad Libs! 🎉")

"""
Learning Notes:
- Each input() is stored in a descriptively named variable
- String concatenation with + is used to build sentences
- The story uses all 8 collected words
- Print statements create readable output with proper spacing
- Empty print() creates blank lines for better formatting
"""