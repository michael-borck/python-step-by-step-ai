# Quiz Game - Hints 💡

## Stuck? Here are some hints to help you progress!

### General Structure Hints

**Hint 1: Question File Format**
Each question takes exactly 6 lines:
1. Question text
2. Option A
3. Option B
4. Option C
5. Option D
6. Correct answer (A, B, C, or D)
7. Points value
8. Empty line (separator)

**Hint 2: Question Dictionary Structure**
```python
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
```

### Function-Specific Hints

**load_questions() Hints:**
```python
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Process every 7 lines (6 for question + 1 empty)
    for i in range(0, len(lines), 7):
        if i + 5 < len(lines):  # Make sure we have enough lines
            question = {
                "text": lines[i].strip(),
                "options": {
                    "A": lines[i+1].strip()[3:],  # Remove "A) "
                    "B": lines[i+2].strip()[3:],  # Remove "B) "
                    "C": lines[i+3].strip()[3:],  # Remove "C) "
                    "D": lines[i+4].strip()[3:]   # Remove "D) "
                },
                "answer": lines[i+5].strip(),
                "points": int(lines[i+6].strip())
            }
            questions.append(question)
```

**display_question() Hints:**
```python
print(f"\nQuestion {question_num} of {total_questions} ({question['points']} points):")
print(question['text'])
print()
for letter, option in question['options'].items():
    print(f"{letter}) {option}")
```

**get_user_answer() Hints:**
```python
while True:
    answer = input("\nYour answer (A-D): ").upper().strip()
    if answer in ['A', 'B', 'C', 'D']:
        return answer
    print("Please enter A, B, C, or D")
```

**High Scores Hints:**
```python
# Loading high scores
try:
    with open(SCORES_FILE, 'r') as f:
        return json.load(f)
except FileNotFoundError:
    return []

# Saving high scores  
scores.sort(key=lambda x: x['score'], reverse=True)
scores = scores[:5]  # Keep only top 5
with open(SCORES_FILE, 'w') as f:
    json.dump(scores, f, indent=2)
```

### Common Issues and Solutions

**Issue: File Parsing Errors**
```python
# Check if you have enough lines for a complete question
if i + 6 >= len(lines):
    break  # Not enough lines for complete question
```

**Issue: Empty Questions List**
```python
if not questions:
    print("No valid questions found in file!")
    return []
```

**Issue: JSON Errors**
```python
try:
    with open(SCORES_FILE, 'r') as f:
        scores = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    scores = []  # Start with empty scores
```

### Game Loop Implementation

**Main Game Loop:**
```python
for i, question in enumerate(questions, 1):
    display_question(question, i, len(questions))
    
    user_answer = get_user_answer()
    is_correct = check_answer(user_answer, question['answer'])
    
    if is_correct:
        score += question['points']
        correct_count += 1
        
    display_feedback(is_correct, question['answer'], 
                    question['points'] if is_correct else 0)
```

### High Score Management

**Check if Score Qualifies:**
```python
def is_high_score(score, high_scores):
    if len(high_scores) < 5:
        return True
    return score > min(s['score'] for s in high_scores)
```

**Update High Scores:**
```python
def update_high_scores(scores, name, score):
    new_score = {"name": name, "score": score}
    scores.append(new_score)
    scores.sort(key=lambda x: x['score'], reverse=True)
    return scores[:5]  # Keep top 5
```

### Question File Creation Tips

**Sample Question Format:**
```
What is the correct way to create a function in Python?
A) function myFunc():
B) def myFunc():
C) create myFunc():
D) func myFunc():
B
10

```

Note the empty line at the end!

### Debugging Tips

1. **Print parsed questions** to verify format:
   ```python
   for q in questions:
       print(f"Q: {q['text']}")
       print(f"Answer: {q['answer']}")
   ```

2. **Test with one question** first

3. **Check file line endings** (Windows vs Unix)

4. **Verify JSON format** for high scores

### AI Partnership Hints

**Good prompts to try:**
- "How do I parse a structured text file in Python?"
- "What's the best way to handle file format errors?"
- "How can I sort a list of dictionaries by a specific key?"

**Remember:** Start with simple file reading, then add game logic!

