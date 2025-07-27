# Week 8 Project: Quiz Game 🎮

## Overview

Create an interactive quiz game that combines everything from Part II: functions, dictionaries, and file I/O. This capstone project for Part II challenges you to integrate multiple concepts into a cohesive, fun application!

## Learning Objectives

By completing this project, you will:
- ✓ Integrate functions, dictionaries, and files
- ✓ Design data structures for complex information
- ✓ Create a complete user experience
- ✓ Handle multiple types of data
- ✓ Build a scalable, maintainable program

## Core Requirements (🟢 Basic)

Your quiz game must:

1. **Load questions from a file** containing:
   - Question text
   - Multiple choice options (A, B, C, D)
   - Correct answer
   - Point value

2. **Present questions** one at a time with:
   - Clear display of question and options
   - Input validation for answers
   - Immediate feedback (correct/incorrect)

3. **Track game state** including:
   - Current score
   - Questions answered
   - Questions remaining

4. **Save high scores** to a file that persists

5. **Provide game summary** at the end showing:
   - Final score
   - Percentage correct
   - High score comparison

### Example Interaction
```
🎮 Python Quiz Game 🎮
====================

Loading questions...
Ready to test your Python knowledge?

Question 1 of 5 (10 points):
What is the correct way to create a function in Python?

A) function myFunc():
B) def myFunc():
C) create myFunc():
D) func myFunc():

Your answer (A-D): B

✅ Correct! Well done!
Score: 10 points

Question 2 of 5 (20 points):
Which data structure uses key-value pairs?

A) List
B) Tuple
C) Dictionary
D) Set

Your answer (A-D): C

✅ Correct! Great job!
Score: 30 points

[... more questions ...]

🏁 Game Over! 🏁
================
Final Score: 70/100 points
Correct: 4/5 (80%)

🏆 New High Score! 🏆
Enter your name: Alice

High Scores:
1. Alice - 70 points
2. Bob - 65 points
3. Charlie - 50 points
```

## Implementation Guide

### Step 1: Design Question Format
Decide how to structure questions in your file and dictionary.

### Step 2: File Operations
Create functions to load questions and save/load high scores.

### Step 3: Game Logic
Implement the main game loop with question presentation.

### Step 4: Scoring System
Track points and calculate statistics.

### Step 5: High Score Management
Compare scores and update the high score list.

## Question File Format Example

```
What is the correct way to create a function in Python?
A) function myFunc():
B) def myFunc():
C) create myFunc():
D) func myFunc():
B
10

Which data structure uses key-value pairs?
A) List
B) Tuple
C) Dictionary
D) Set
C
20
```

## Challenges

### 🟡 Intermediate Challenges

1. **Question Categories**: Add topics (loops, functions, etc.) and let players choose

2. **Difficulty Levels**: Easy/Medium/Hard with different point values

3. **Timer Feature**: Add time limits for each question

4. **Lifelines**: Add hints, 50/50, or skip question options

5. **Random Order**: Shuffle questions and answer options

### 🔴 Advanced Challenges

1. **Question Editor**: Create/edit questions from within the program

2. **Multiple Game Modes**: Speed round, survival, category challenge

3. **Player Profiles**: Track stats for different players

4. **Question Bank**: Support multiple question files

5. **Achievement System**: Unlock badges for milestones

### 🟣 AI Partnership Challenge

1. **Question Generation**:
   - Ask AI: "Generate Python quiz questions at different difficulty levels"
   - Format them for your game
   - Build a diverse question bank

2. **Game Balance**:
   - Get AI's input on scoring systems
   - Design fair difficulty progression
   - Create engaging gameplay loops

### ⭐ Reflection Exercise

Write a short paragraph answering:
- How did you decide to structure your question data?
- What was challenging about combining files, functions, and dictionaries?
- How would you extend this to support different types of questions?
- What makes a quiz game fun and engaging?

## Testing Your Program

Test these scenarios:
- [ ] Questions load correctly from file
- [ ] All answer validation works (A-D, invalid inputs)
- [ ] Score calculates correctly
- [ ] High scores save and persist
- [ ] Game handles empty/corrupted files
- [ ] Statistics display accurately
- [ ] Edge cases (0 correct, all correct)

## Common Mistakes to Avoid

1. **Hardcoding questions** - Always load from file
2. **Case sensitivity** - Accept 'a' and 'A' for answers
3. **File errors** - Handle missing question/score files
4. **Score calculation** - Test your math carefully
5. **Data structure** - Keep questions organized

## Data Structure Patterns

```python
# Question dictionary structure
question = {
    "text": "What is...?",
    "options": {
        "A": "Option 1",
        "B": "Option 2",
        "C": "Option 3",
        "D": "Option 4"
    },
    "answer": "B",
    "points": 10
}

# High scores list
high_scores = [
    {"name": "Alice", "score": 70},
    {"name": "Bob", "score": 65}
]
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "How should I structure quiz questions in a dictionary?"
- "What's the best way to parse a question file?"
- "How can I keep high scores sorted?"

### ❌ Avoid These Prompts
- "Create a web-based quiz with database"
- "Add multiplayer networking"
- "Implement voice recognition for answers"

## File Handling Tips

```python
# Safe file reading with default
def load_questions(filename):
    try:
        with open(filename, 'r') as f:
            # Parse questions
    except FileNotFoundError:
        print("No questions file found!")
        return []
```

## Submission Checklist

Before considering your project complete:
- [ ] Questions load from external file
- [ ] Game presents questions clearly
- [ ] Answer validation works properly
- [ ] Score tracking is accurate
- [ ] High scores save and load
- [ ] Game provides good feedback
- [ ] Error handling for files
- [ ] Clean, modular code with functions

## Extension Ideas

Once you've completed the basic requirements:
- Add true/false questions
- Create study mode with explanations
- Build question streak bonuses
- Add sound effects (using print statements)
- Create tournament brackets

## Resources

- Chapter 6: Functions
- Chapter 8: Dictionaries
- Chapter 9: File I/O
- Chapter 6-9: Integration techniques

---

Remember: This project brings together everything from Part II. Take time to plan your data structures and functions before coding! 🧩✨

