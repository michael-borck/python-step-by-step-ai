# Week 4 Project: Rock Paper Scissors 🪨📄✂️

## Overview

Create the classic Rock Paper Scissors game where a player competes against the computer. This project combines everything from Week 4: loops, conditions, comparisons, and decision trees.

## Learning Objectives

By completing this project, you will:
- ✓ Use complex if/elif/else decision trees
- ✓ Implement game loops for multiple rounds
- ✓ Work with random computer choices
- ✓ Track game state and scores
- ✓ Validate user input effectively

## Core Requirements (🟢 Basic)

Your Rock Paper Scissors game must:

1. **Explain the rules** at the start
2. **Accept player choice** (rock, paper, or scissors)
3. **Generate computer choice** randomly
4. **Determine the winner** using game rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same choice = Tie
5. **Display results** clearly showing:
   - Player's choice
   - Computer's choice
   - Who won the round
6. **Play multiple rounds** until the player wants to stop

### Example Gameplay
```
🪨📄✂️ Welcome to Rock Paper Scissors! 🪨📄✂️

Rules:
- Rock beats Scissors
- Scissors beats Paper  
- Paper beats Rock

Let's play!

Enter your choice (rock/paper/scissors): rock
You chose: ROCK
Computer chose: SCISSORS
🎉 You win! Rock crushes Scissors!

Play again? (yes/no): yes

Enter your choice (rock/paper/scissors): paper
You chose: PAPER
Computer chose: PAPER
🤝 It's a tie!

Play again? (yes/no): no

Thanks for playing!
Final Score - You: 1, Computer: 0, Ties: 1
```

## Implementation Guide

### Step 1: Set Up the Game
- Import random for computer choices
- Create welcome message and rules
- Initialize score variables

### Step 2: Create the Choice System
- Get player input
- Validate the input
- Generate computer choice

### Step 3: Determine Winner Logic
- Create the decision tree for all outcomes
- Consider all 9 possible combinations

### Step 4: Game Loop
- Allow multiple rounds
- Keep running score
- Provide option to quit

### Step 5: Display Results
- Show clear feedback for each round
- Display final statistics

## Challenges

### 🟡 Intermediate Challenges

1. **Best of 5**: First to win 3 rounds wins the match
2. **Emoji Mode**: Use 🪨📄✂️ instead of words
3. **Smart Computer**: Computer tracks player patterns
4. **Shortcuts**: Accept 'r', 'p', 's' as valid inputs
5. **Statistics**: Show win percentage and streaks

### 🔴 Advanced Challenges

1. **Extended Version**: Add Lizard and Spock (Rock Paper Scissors Lizard Spock)
2. **Tournament Mode**: Play against multiple AI personalities
3. **Prediction AI**: Computer tries to predict player's next move
4. **Graphical Display**: ASCII art for choices
5. **Save Game History**: Track all games played

### 🟣 AI Partnership Challenge

1. **Strategy Analysis**:
   - Ask AI: "What's the optimal Rock Paper Scissors strategy?"
   - Implement different AI strategies
   - Test which performs best

2. **Code Efficiency**:
   - Get AI's version of winner logic
   - Simplify to most readable form
   - Compare different approaches

### ⭐ Reflection Exercise

Write a short paragraph answering:
- How did you organize the winner determination logic?
- What patterns did you notice in the game rules?
- How would you detect if a player has a pattern?
- What makes this game fun despite being simple?

## Testing Your Program

Test these scenarios:
- [ ] Each possible outcome (9 combinations)
- [ ] Invalid inputs (typos, numbers, empty)
- [ ] Case sensitivity (ROCK vs rock)
- [ ] Multiple rounds in a row
- [ ] Quitting mid-game
- [ ] Score tracking accuracy

## Common Mistakes to Avoid

1. **Missing combinations** - Forgetting some win/lose scenarios
2. **Case sensitivity** - "Rock" not matching "rock"
3. **Infinite loops** - Not providing way to exit
4. **Poor feedback** - Unclear who won and why
5. **Score errors** - Incrementing wrong counter

## Winner Logic Patterns

There are different ways to determine the winner:

```python
# Method 1: Check each possibility
if player == "rock" and computer == "scissors":
    print("You win!")

# Method 2: Use nested conditions
if player == computer:
    print("Tie!")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")

# Method 3: Use a winner dictionary (advanced)
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "Show me different ways to structure Rock Paper Scissors winner logic"
- "How can I make user input case-insensitive?"
- "What's a clean way to handle invalid input?"

### ❌ Avoid These Prompts
- "Create an unbeatable AI using machine learning"
- "Add networking for online multiplayer"
- "Build a 3D animated version"

## Input Handling Tips

Make your game user-friendly:

```python
# Accept variations
choice = input("Your choice: ").lower().strip()

# Handle common typos
if choice in ["rock", "r", "1"]:
    player_choice = "rock"
```

## Submission Checklist

Before considering your project complete:
- [ ] Game explains rules clearly
- [ ] Accepts three valid choices
- [ ] Computer makes random choices
- [ ] Winner determination is correct
- [ ] Results display clearly
- [ ] Can play multiple rounds
- [ ] Score tracking works
- [ ] Clean exit option provided

## Extension Ideas

Once you've completed the basic requirements:
- Add "best of N" tournament modes
- Create different difficulty levels
- Add time limits for decisions
- Include power-ups or special moves
- Build player profiles with statistics

## Resources

- Chapter 4: Review if/elif/else statements
- Chapter 5: Review loops
- Chapter 7: Comparison operators
- Random module documentation

---

Remember: Even simple games can be engaging with good design. Focus on clear feedback and smooth gameplay! 🎮✨
