# Week 3 Project: Number Guessing Game 🎯

## Overview

Create an interactive number guessing game where the computer picks a random number and the player tries to guess it. This project reinforces concepts from Week 3: loops, conditions, and comparisons.

## Learning Objectives

By completing this project, you will:
- ✓ Use `while` loops for repeated gameplay
- ✓ Implement `if/elif/else` for game logic
- ✓ Work with comparison operators (`<`, `>`, `==`)
- ✓ Track game state with variables
- ✓ Convert string input to numbers

## Core Requirements (🟢 Basic)

Your number guessing game must:

1. **Generate a random number** between 1 and 100
2. **Ask the player to guess** the number
3. **Provide feedback** after each guess:
   - "Too high!" if guess is above the number
   - "Too low!" if guess is below the number
   - "Correct!" when they guess right
4. **Count the number of guesses** taken
5. **Continue until the player guesses correctly**

### Example Gameplay
```
🎯 Welcome to the Number Guessing Game! 🎯

I'm thinking of a number between 1 and 100.
Can you guess it?

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Too high! Try again.

Enter your guess: 31
🎉 Correct! You got it in 4 guesses!

Thanks for playing!
```

## Implementation Guide

### Step 1: Set Up the Game
- Import random module
- Generate a secret number
- Initialize guess counter

### Step 2: Create the Game Loop
- Use a `while` loop that continues until the correct guess
- Inside the loop: get guess, check it, give feedback

### Step 3: Handle User Input
- Convert string input to integer
- Consider what happens with invalid input

### Step 4: Provide Clear Feedback
- Use if/elif/else for different cases
- Make messages helpful and encouraging

### Step 5: End the Game
- Congratulate the player
- Show final statistics

## Challenges

### 🟡 Intermediate Challenges

1. **Input Validation**: Handle non-number inputs gracefully
2. **Guess Limiting**: Give players only 7 chances to guess
3. **Play Again**: Ask if they want to play another round
4. **Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-500)
5. **Hint System**: Give better hints like "Way too high!" or "Very close!"

### 🔴 Advanced Challenges

1. **Score System**: Award points based on number of guesses
2. **High Score Tracking**: Remember the best score
3. **Statistics**: Show average guesses across multiple games
4. **Smart Computer**: Make the number harder to guess based on patterns
5. **Reverse Mode**: Player picks number, computer guesses

### 🟣 AI Partnership Challenge

1. **Code Comparison**:
   - Ask AI to create a number guessing game
   - Simplify it to use only Week 3 concepts
   - Compare efficiency and readability

2. **Algorithm Analysis**:
   - Ask AI: "What's the optimal guessing strategy?"
   - Implement a "binary search" hint system
   - Test if it reduces average guesses

### ⭐ Reflection Exercise

Write a short paragraph answering:
- What makes a game fun vs frustrating?
- How did loops simplify your code?
- What edge cases did you need to handle?
- How would you explain the game logic to a friend?

## Testing Your Program

Test these scenarios:
- [ ] Guess correctly on first try
- [ ] Guess too high several times
- [ ] Guess too low several times
- [ ] Enter non-numbers (letters, symbols)
- [ ] Enter numbers outside the range
- [ ] Play multiple rounds

## Common Mistakes to Avoid

1. **Infinite loops** - Forgetting to update loop condition
2. **String vs integer comparison** - "50" is not equal to 50
3. **Off-by-one errors** - Is the range 1-100 or 0-99?
4. **Not handling bad input** - Program crashes on non-numbers
5. **Poor feedback** - Player doesn't know if they're close

## Code Structure Tips

```python
# Good structure example:
secret_number = # generate random
guess_count = 0
guessed_correctly = False

while not guessed_correctly:
    # Get guess
    # Increment counter
    # Check guess
    # Update guessed_correctly if correct
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "How do I convert a string to integer safely in Python?"
- "What's the difference between while and for loops?"
- "Explain the optimal strategy for guessing games"

### ❌ Avoid These Prompts
- "Write a complete number guessing game with GUI"
- "Add machine learning to predict player behavior"
- "Create multiplayer networking support"

## Input Handling Patterns

You'll need to handle user input carefully:

```python
# Basic conversion (can crash):
guess = int(input("Enter guess: "))

# Safer approach:
user_input = input("Enter guess: ")
if user_input.isdigit():
    guess = int(user_input)
else:
    print("Please enter a number!")
```

## Submission Checklist

Before considering your project complete:
- [ ] Game generates random number 1-100
- [ ] Player can make multiple guesses
- [ ] Each guess receives appropriate feedback
- [ ] Guess counter works correctly
- [ ] Game ends when number is guessed
- [ ] Final message shows total guesses
- [ ] Code is commented and readable

## Extension Ideas

Once you've completed the basic requirements:
- Add sound effects for correct/incorrect guesses
- Create themed versions (guess the price, guess my age)
- Implement a "warmer/colder" feedback system
- Add time limits for extra challenge
- Create a two-player competitive mode

## Resources

- Chapter 5: Review while loops
- Chapter 4: Review if/elif/else statements
- Chapter 7: Comparison operators
- Python docs: `random.randint()`

---

Remember: A good game is challenging but fair. Make sure your feedback helps players improve their next guess! 🎯✨