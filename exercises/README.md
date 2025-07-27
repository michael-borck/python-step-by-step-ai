# Python Step by Step: Exercise Repository

Welcome to the exercise repository for "Python Step by Step: Learning with AI"! This folder contains all the hands-on exercises and projects that accompany the book.

## 📚 How to Use This Repository

### For Students

1. **Navigate to your current week's folder** (e.g., `week-01-fortune-teller/`)
2. **Read the `instructions.md`** file for detailed requirements
3. **Start with `starter_code.py`** as your template
4. **Run `tests.py`** to check your progress (when available)
5. **Avoid looking at solutions** until you've tried solving it yourself!

### For Instructors

- Each week includes teaching notes and common student mistakes
- Solutions include multiple approaches and explanations
- Test files can be used for automated grading
- Difficulty progression is carefully calibrated

## 🗂️ Repository Structure

```
exercises/
├── README.md (this file)
├── setup.py (one-time setup script)
├── requirements.txt (Python packages needed)
│
├── week-01-fortune-teller/
│   ├── instructions.md
│   ├── starter_code.py
│   ├── tests.py
│   ├── hints.md
│   └── solutions/
│       ├── solution_basic.py
│       ├── solution_intermediate.py
│       └── solution_advanced.py
│
├── week-02-mad-libs/
│   └── ... (same structure)
│
└── ... (weeks 3-12)
```

## 🎯 Exercise Philosophy

Each exercise follows the book's three learning strategies:

### 1. Understand the Concept Before the Code
- Start by reading the conceptual overview in instructions
- Think about the problem before coding
- Use AI to explore concepts, not just get answers

### 2. Use AI to Explore, Not to Avoid Learning
- Good prompt: "Explain how random choice works in Python"
- Bad prompt: "Write the complete fortune teller program for me"
- Practice the "Simplification Game" with AI's suggestions

### 3. Build Mental Models, Not Just Working Programs
- Focus on understanding WHY code works
- Draw diagrams of data flow
- Explain your solution to someone else (or rubber duck!)

## 🚀 Getting Started

### One-Time Setup

1. Make sure Python 3.8+ is installed:
   ```bash
   python --version
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the setup script:
   ```bash
   python setup.py
   ```

### Starting an Exercise

1. Navigate to the exercise folder:
   ```bash
   cd week-01-fortune-teller
   ```

2. Read the instructions:
   ```bash
   cat instructions.md
   ```

3. Open the starter code in your editor:
   ```bash
   # Or use your preferred editor
   code starter_code.py
   ```

4. Start coding!

## 📊 Difficulty Levels

Each exercise includes challenges at different levels:

- **🟢 Basic**: Core requirements using only concepts covered so far
- **🟡 Intermediate**: Add features using creative applications
- **🔴 Advanced**: Explore concepts slightly beyond current chapter
- **🟣 AI Challenge**: Practice prompt engineering and code simplification
- **⭐ Reflection**: Non-coding exercises for deeper understanding

## 🤝 Working with AI

### Recommended AI Practices

✅ **DO:**
- Ask AI to explain error messages
- Request simpler versions of complex code
- Use AI to understand new concepts
- Compare your solution with AI's suggestions

❌ **DON'T:**
- Copy AI's code without understanding
- Use features you haven't learned yet
- Skip the struggle - it's part of learning!
- Ask AI to "do my homework"

### Example Good Prompts

For Week 1 (Fortune Teller):
```
"I need to pick a random item from a list in Python. 
Show me the simplest way using only print() and basic lists."
```

```
"My fortune teller always shows the same fortune. 
What concept am I missing about randomness?"
```

## 🏆 Progress Tracking

Track your progress with this checklist:

### Part I: Computational Thinking
- [ ] Week 1: Fortune Teller
- [ ] Week 2: Mad Libs Generator  
- [ ] Week 3: Number Guessing Game
- [ ] Week 4: Rock, Paper, Scissors

### Part II: Building Systems
- [ ] Week 5: Temperature Converter
- [ ] Week 6: Contact Book
- [ ] Week 7: Journal App
- [ ] Week 8: Quiz Game

### Part III: Real-World Programming
- [ ] Week 9: Grade Analysis Tool
- [ ] Week 10: Weather Dashboard
- [ ] Week 11: Text Adventure Game
- [ ] Week 12: Todo GUI Application

## 🆘 Getting Help

### When You're Stuck

1. **Re-read the relevant chapter** - The answer is often there!
2. **Check hints.md** - Progressive hints without spoiling the solution
3. **Use AI wisely** - Ask for explanations, not complete solutions
4. **Talk it through** - Explain your problem to a rubber duck
5. **Take a break** - Sometimes distance brings clarity

### Common Issues

**"Import error: No module named..."**
- Run `pip install -r requirements.txt` from the exercises folder

**"My tests won't pass"**
- Check that you're matching the expected output format exactly
- Read the test file to understand what it's checking

**"The starter code won't run"**
- Make sure you're using Python 3.8 or higher
- Check that you're in the correct directory

## 📝 Exercise Completion Criteria

You've truly completed an exercise when you can:

✓ **Run it successfully** - No errors, produces expected output
✓ **Explain how it works** - Could teach it to someone else
✓ **Modify it confidently** - Can add features or fix bugs
✓ **Connect to concepts** - Understand which programming concepts you used
✓ **Reflect on learning** - Identify what was challenging and why

## 🎓 After Completing All Exercises

Congratulations! You've built 12 real projects and developed strong programming skills. You're ready for:

1. **Python Jumpstart** - The next book in your journey
2. **Open Source Contributing** - Help improve these exercises
3. **Your Own Projects** - Apply your skills to solve real problems
4. **Teaching Others** - Share your knowledge with new learners

## 📜 License and Usage

These exercises are part of "Python Step by Step: Learning with AI" and are provided for educational use. Please respect the learning journey of others by not sharing solutions publicly.

---

**Remember**: The goal isn't just to make programs work - it's to understand HOW and WHY they work. Every challenge you overcome makes you a stronger programmer!

Happy coding! 🐍✨