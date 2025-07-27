# Exercise Quick Reference Guide 📚

This guide provides a quick overview of all 12 weekly projects in Python Step by Step: Learning with AI.

## Part I: Computational Thinking (Weeks 1-4)

### Week 1: Fortune Teller 🔮
- **Concepts**: Variables, lists, random selection, print()
- **Core Task**: Create a mystical fortune-telling program
- **Key Skills**: Working with lists, using random.choice()
- **Files**: `week-01-fortune-teller/`

### Week 2: Mad Libs Generator 📝
- **Concepts**: Variables, input(), string manipulation
- **Core Task**: Create interactive story with user inputs
- **Key Skills**: Collecting user input, string concatenation
- **Files**: `week-02-mad-libs/`

### Week 3: Number Guessing Game 🎯
- **Concepts**: While loops, if/elif/else, comparisons
- **Core Task**: Player guesses computer's random number
- **Key Skills**: Game loops, conditional logic, input validation
- **Files**: `week-03-number-game/`

### Week 4: Rock Paper Scissors 🪨📄✂️
- **Concepts**: Complex conditionals, game logic, loops
- **Core Task**: Classic RPS game against computer
- **Key Skills**: Decision trees, score tracking, multiple rounds
- **Files**: `week-04-rock-paper-scissors/`

## Part II: Building Systems (Weeks 5-8)

### Week 5: Temperature Converter 🌡️
- **Concepts**: Functions, parameters, return values
- **Core Task**: Convert between temperature units
- **Key Skills**: Creating reusable functions, calculations
- **Files**: `week-05-temperature-converter/`

### Week 6: Contact Book 📞
- **Concepts**: Dictionaries, data organization, CRUD operations
- **Core Task**: Store and manage contact information
- **Key Skills**: Dictionary manipulation, data structures
- **Files**: `week-06-contact-book/`

### Week 7: Journal App 📔
- **Concepts**: File I/O, data persistence, timestamps
- **Core Task**: Save and load journal entries
- **Key Skills**: Reading/writing files, data formatting
- **Files**: `week-07-journal-app/`

### Week 8: Quiz Game 🎮
- **Concepts**: Integration of all Part II concepts
- **Core Task**: Multi-question quiz with score tracking
- **Key Skills**: Combining files, functions, and data structures
- **Files**: `week-08-quiz-game/`

## Part III: Real-World Programming (Weeks 9-12)

### Week 9: Grade Analysis Tool 📊
- **Concepts**: CSV files, data analysis, statistics
- **Core Task**: Analyze student grades from files
- **Key Skills**: CSV processing, calculations, reporting
- **Files**: `week-09-grade-analysis/`

### Week 10: Weather Dashboard 🌤️
- **Concepts**: APIs, JSON, real-time data, GUI basics
- **Core Task**: Display live weather from internet
- **Key Skills**: API requests, JSON parsing, tkinter
- **Files**: `week-10-weather-dashboard/`

### Week 11: Text Adventure Game 🗺️
- **Concepts**: Complex state management, OOP basics
- **Core Task**: Create interactive story game
- **Key Skills**: Game state, save/load, complex logic
- **Files**: `week-11-text-adventure/`

### Week 12: Todo GUI Application ✅
- **Concepts**: Full GUI development, architecture
- **Core Task**: Complete todo list with graphical interface
- **Key Skills**: Software architecture, complete applications
- **Files**: `week-12-todo-gui/`

## Difficulty Progression

Each exercise includes multiple difficulty levels:

- **🟢 Basic**: Core requirements using only concepts covered so far
- **🟡 Intermediate**: Added features and enhancements
- **🔴 Advanced**: Stretch goals and future concepts
- **🟣 AI Challenge**: Practice with AI partnership
- **⭐ Reflection**: Non-coding exercises for understanding

## How to Use This Guide

1. **Start with your current week** - Don't skip ahead
2. **Complete Basic requirements first** - Master fundamentals
3. **Try at least one challenge** - Push your boundaries
4. **Do the AI Partnership exercise** - Practice prompting
5. **Complete the reflection** - Solidify understanding

## Common Patterns Across Projects

### Input Validation Pattern
```python
while True:
    user_input = input("Enter choice: ")
    if user_input in valid_choices:
        break
    print("Invalid input, try again")
```

### Game Loop Pattern
```python
playing = True
while playing:
    # Game logic here
    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        playing = False
```

### File Handling Pattern
```python
try:
    with open("data.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("No data file found")
    data = ""
```

## Tips for Success

1. **Read instructions completely** before starting
2. **Start simple** - get basic version working first
3. **Test frequently** - run your code often
4. **Use meaningful variable names** - code should be readable
5. **Comment your code** - explain your thinking
6. **Ask AI good questions** - focus on understanding

## Tracking Your Progress

Use the included `progress_tracker.py` to:
- Mark exercises as started/completed
- Track which challenges you've done
- Add notes about what you learned
- See your overall progress

Run it with:
```bash
python3 progress_tracker.py
```

---

Remember: The goal isn't just to complete the exercises, but to understand the concepts deeply. Take your time, experiment, and have fun! 🐍✨