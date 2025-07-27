#!/usr/bin/env python3
"""
Week 2 Project: Mad Libs Generator - Intermediate Solution
This solution adds input validation and multiple story options.
"""

# Welcome with ASCII art
print("*" * 50)
print("*" + " " * 48 + "*")
print("*" + "          🎭 MAD LIBS GENERATOR 🎭           ".center(48) + "*")
print("*" + " " * 48 + "*")
print("*" * 50)
print()

# Explain the game
print("Welcome! I'll ask you for various words, then create")
print("a hilarious story using your inputs!")
print()

# Let user choose a story type
print("Choose your story type:")
print("1. Adventure Story")
print("2. Cooking Recipe")
print("3. News Report")
story_choice = input("\nEnter 1, 2, or 3: ")

# Validate story choice
while story_choice not in ["1", "2", "3"]:
    print("Please enter 1, 2, or 3!")
    story_choice = input("Enter your choice: ")

print("\nGreat choice! Now I need some words...\n")

# Collect words with validation
def get_word(prompt):
    """Get a non-empty word from the user"""
    word = input(prompt)
    while word.strip() == "":
        print("Oops! You didn't enter anything.")
        word = input(prompt)
    return word

# Collect 10 words for more variety
noun1 = get_word("Enter a noun: ")
noun2 = get_word("Enter another noun: ")
verb1 = get_word("Enter a verb: ")
verb2 = get_word("Enter a verb ending in -ing: ")
adjective1 = get_word("Enter an adjective: ")
adjective2 = get_word("Enter another adjective: ")
animal = get_word("Enter an animal: ")
place = get_word("Enter a place: ")
food = get_word("Enter a type of food: ")
number = get_word("Enter a number: ")

# Create title based on inputs
print("\n" + "=" * 50)
print("📖 Your Mad Libs Masterpiece 📖".center(50))
print("=" * 50)

# Display chosen story
if story_choice == "1":
    # Adventure Story
    print(f"\nThe {adjective1.upper()} {animal.upper()} ADVENTURE")
    print("-" * 40)
    print(f"\nOnce upon a time, {number} brave {animal}s decided to {verb1}")
    print(f"to the mystical {place}. They packed {adjective2} {food}")
    print(f"for the journey. Along the way, they discovered a {noun1}")
    print(f"that was {verb2} mysteriously. Using their {noun2},")
    print(f"they solved the puzzle and became {adjective1} heroes!")
    
elif story_choice == "2":
    # Cooking Recipe
    print(f"\nRECIPE: {adjective1.upper()} {food.upper()} SURPRISE")
    print("-" * 40)
    print(f"\nIngredients:")
    print(f"- {number} cups of {noun1}")
    print(f"- 1 {adjective2} {noun2}")
    print(f"- A pinch of {animal} essence")
    print(f"\nInstructions:")
    print(f"1. First, {verb1} all ingredients in a bowl from {place}")
    print(f"2. Keep {verb2} for exactly {number} minutes")
    print(f"3. Serve {adjective1}ly and enjoy!")
    
else:
    # News Report
    print(f"\n📺 BREAKING NEWS FROM {place.upper()} 📺")
    print("-" * 40)
    print(f"\nThis just in: A {adjective1} {animal} was spotted")
    print(f"{verb2} near the local {noun1} factory today.")
    print(f"Witnesses report it was carrying {number} {adjective2}")
    print(f"{food}s and appeared to {verb1} occasionally.")
    print(f"Police chief {noun2} says there's no need to panic.")
    print(f'"It\'s perfectly {adjective2}," they stated.')

print("\n" + "=" * 50)
print("Thanks for playing Mad Libs! Your story was hilarious! 😄")
print()

# Ask if they want to save their story
save_choice = input("Would you like to save your story? (yes/no): ")
if save_choice.lower() == "yes":
    print("Story saved to 'my_madlib.txt'! (Just pretending for now 😉)")

"""
Intermediate Features:
- ASCII art welcome banner
- Story type selection with validation
- Input validation function to prevent empty inputs
- Three different story templates
- Dynamic title creation
- More words collected (10 instead of 8)
- f-strings used for cleaner formatting (if learned)
- Save option (simulated)
- Better formatting with separators
"""