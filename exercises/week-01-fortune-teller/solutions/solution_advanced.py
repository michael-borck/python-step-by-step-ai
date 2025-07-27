#!/usr/bin/env python3
"""
Week 1 Project: Fortune Teller - Advanced Solution
This solution adds ASCII art, personalization, and time-based greetings.
"""

import random
import datetime

# ASCII art for visual appeal
crystal_ball = """
        ⋆｡‧˚ʚ♡ɞ˚‧｡⋆
       ╱|､
      (˚ˎ 。7  
       |､˜〵          
       じしˍ,)ノ
    ✨ Crystal Ball ✨
"""

# Fortunes organized by category
fortune_database = {
    "🌟 Destiny": [
        "Your path is illuminated by inner wisdom.",
        "A turning point approaches - embrace the change!",
        "The universe conspires to help you succeed."
    ],
    "💝 Heart": [
        "Love finds those who remain open to its magic.",
        "A cherished relationship will grow stronger.",
        "Your kindness creates ripples of joy."
    ],
    "💰 Prosperity": [
        "Abundance flows to those who share generously.",
        "An investment of effort yields golden returns.",
        "Success blooms where passion is planted."
    ],
    "🔮 Mystery": [
        "A hidden truth will soon be revealed.",
        "Trust your intuition - it knows the way.",
        "Synchronicities guide you toward your purpose."
    ]
}

# Get time-based greeting
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    time_greeting = "Good morning"
    time_message = "The morning mists reveal your fortune..."
elif current_hour < 17:
    time_greeting = "Good afternoon"
    time_message = "The afternoon sun illuminates your path..."
else:
    time_greeting = "Good evening"
    time_message = "The evening stars whisper your destiny..."

# Display fortune teller interface
print("\n" + "="*55)
print(crystal_ball)
print("="*55)
print(f"\n   {time_greeting}, seeker of wisdom!")
print(f"   {time_message}")
print("\n" + "="*55)

# Ask for user's name (using input if you want to try it)
print("\n🌙 The spirits wish to know your name...")
print("   (For now, we'll call you 'Mysterious Seeker')")
user_name = "Mysterious Seeker"
print()

# Select random category and fortune
category = random.choice(list(fortune_database.keys()))
fortune = random.choice(fortune_database[category])

# Create dramatic reveal
print(f"⚡ {user_name}, the mystical forces are stirring... ⚡")
print()
print("." * 10 + " Reading cosmic energies " + "." * 10)
print()
print(f"Category revealed: {category}")
print()
print("🔮 YOUR FORTUNE 🔮")
print("┌" + "─" * 51 + "┐")
print(f"│ {fortune:<49} │")
print("└" + "─" * 51 + "┘")
print()

# Lucky elements
print("✨ MYSTICAL INSIGHTS ✨")
print(f"  Lucky Color: {random.choice(['Cosmic Purple', 'Mystic Blue', 'Golden Sunrise', 'Emerald Dream'])}")
print(f"  Power Stone: {random.choice(['Amethyst', 'Rose Quartz', 'Tiger Eye', 'Moonstone'])}")
print(f"  Spirit Animal: {random.choice(['Wise Owl', 'Graceful Swan', 'Mighty Eagle', 'Clever Fox'])}")

# Generate lucky numbers with meaning
print(f"\n🎯 Sacred Numbers: ", end="")
numbers = []
for i in range(3):
    num = random.randint(1, 33)
    numbers.append(str(num))
print(" • ".join(numbers))

# Closing message
print("\n" + "="*55)
print("  ✨ Thank you for visiting Madame Mystique! ✨")
print("  May your path be filled with wonder and magic!")
print("="*55 + "\n")

# Fortune history tracker (demonstrates list usage)
fortune_history = []
fortune_history.append(f"{category}: {fortune}")
print(f"📜 Fortune recorded in the cosmic logs...")

"""
Advanced Concepts Demonstrated:
- ASCII art for visual appeal
- Dictionary data structure for categorized fortunes
- DateTime module for time-based features
- String formatting with f-strings and format specifiers
- Box drawing characters for fortune display
- Lists within dictionaries
- Multiple random selections
- Fortune history tracking concept

Note: Some concepts here are beyond Week 1, showing what's possible
as students progress. The basic requirements can still be met with
just the Week 1 concepts!
"""