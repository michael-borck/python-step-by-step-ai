# Week 1 Project: Fortune Teller 🔮

## Overview

Create a mystical fortune-telling program that delivers random predictions to users. This project reinforces the concepts from Week 1: variables, strings, lists, and the `print()` function.

## Learning Objectives

By completing this project, you will:
- ✓ Use variables to store different types of data
- ✓ Work with lists to hold multiple fortunes
- ✓ Select random items from a list
- ✓ Display output with the `print()` function
- ✓ Practice the "Simplification Game" with AI assistance

## Core Requirements (🟢 Basic)

Your fortune teller must:

1. **Store at least 5 different fortunes** in a list
2. **Randomly select one fortune** when the program runs
3. **Display the fortune** in an engaging way
4. **Include a greeting** before revealing the fortune
5. **Include a closing message** after the fortune

### Example Output
```
🔮 Welcome to the Mystic Fortune Teller! 🔮

Let me gaze into the crystal ball...

✨ Your fortune: A pleasant surprise will come your way soon! ✨

May the stars guide your path!
```

## Implementation Guide

### Step 1: Create Your Fortunes
Start by creating a list of fortune messages. Think creatively!

### Step 2: Add Personality
Give your fortune teller character with:
- An interesting name
- Mystical vocabulary
- Decorative elements (emojis, symbols)

### Step 3: Random Selection
Use Python's `random` module to pick a fortune:
```python
import random
```

### Step 4: Format Your Output
Make the experience engaging with clear formatting and spacing.

## Challenges

### 🟡 Intermediate Challenges

1. **Fortune Categories**: Create different types of fortunes (love, career, health) and randomly select both a category and a fortune

2. **Lucky Numbers**: Add random lucky numbers to each fortune reading

3. **Time-Based Greetings**: Change the greeting based on when the program runs (morning, afternoon, evening)

### 🔴 Advanced Challenges

1. **Fortune History**: Keep track of which fortunes have been shown and avoid repeats until all have been used

2. **Personalized Fortunes**: Ask for the user's name and incorporate it into the fortune

3. **ASCII Art**: Add decorative ASCII art to make your fortune teller more visually appealing

### 🟣 AI Partnership Challenge

1. **The Simplification Game**: 
   - Ask AI to create a fortune teller
   - Systematically simplify it until it only uses concepts from Week 1
   - Document what you removed and why

2. **Prompt Evolution**:
   - Start with: "Make a fortune teller program"
   - Evolve to: "Make a simple fortune teller using only print and random choice"
   - Compare the results

### ⭐ Reflection Exercise

Write a short paragraph answering:
- What was the hardest part of this project?
- How did you decide what fortunes to include?
- What would you add if you knew more Python?
- How did working with AI help or hinder your learning?

## Testing Your Program

Run your program multiple times to ensure:
- [ ] Different fortunes appear
- [ ] The formatting looks good
- [ ] No error messages appear
- [ ] The experience feels complete

## Common Mistakes to Avoid

1. **Forgetting to import random** - You'll get a NameError
2. **Using quotes incorrectly** - Match your opening and closing quotes
3. **Selecting from the wrong variable** - Make sure you're choosing from your fortune list
4. **Poor formatting** - Use `\n` for line breaks and spacing

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "Explain how random.choice works in simple terms"
- "Why do I need to import random before using it?"
- "Show me different ways to format text output in Python"

### ❌ Avoid These Prompts
- "Write a complete fortune teller program for me"
- "Add advanced features like GUI and database storage"
- "Make it as complex as possible"

## Submission Checklist

Before considering your project complete:
- [ ] Program runs without errors
- [ ] At least 5 different fortunes are possible
- [ ] Output is nicely formatted
- [ ] Code includes comments explaining your thinking
- [ ] You can explain how every line works

## Extension Ideas

Once you've completed the basic requirements:
- Add seasonal fortunes that change based on the date
- Create a "fortune cookie" mode with shorter messages
- Add dramatic pauses using `time.sleep()`
- Create different fortune teller personalities

## Resources

- Chapter 1: Review the `print()` function
- Chapter 2: Review variables and lists
- Python documentation: `random.choice()`

---

Remember: The goal is not just to make it work, but to understand WHY it works. Take your time, experiment, and have fun with your fortunes! 🔮✨