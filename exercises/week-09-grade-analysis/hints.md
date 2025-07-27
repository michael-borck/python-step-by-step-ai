# Grade Analysis Tool - Hints 💡

## Stuck? Here are some hints to help you progress!

### General Structure Hints

**Hint 1: CSV File Reading**
```python
# Manual CSV parsing
with open(filename, 'r') as f:
    lines = f.readlines()
    
# First line is headers
headers = lines[0].strip().split(',')[1:]  # Skip "Student" column

# Remaining lines are student data
for line in lines[1:]:
    values = line.strip().split(',')
    name = values[0]
    scores = values[1:]  # All scores as strings
```

**Hint 2: Student Data Structure**
```python
student = {
    "name": "Alice Johnson",
    "scores": [95, 88, 92, 87, 90],  # Convert to numbers
    "average": 90.4,
    "letter_grade": "A",
    "highest": 95,
    "lowest": 87
}
```

### Function-Specific Hints

**load_student_data() Hints:**
```python
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    if not lines:
        return [], []
        
    # Parse headers (skip "Student" column)
    headers = lines[0].strip().split(',')[1:]
    
    students = []
    for line in lines[1:]:
        if line.strip():  # Skip empty lines
            values = line.strip().split(',')
            name = values[0]
            scores = []
            
            # Convert scores to numbers, handle invalid data
            for score_str in values[1:]:
                score = validate_score(score_str)
                if score is not None:
                    scores.append(score)
            
            students.append({
                "name": name,
                "scores": scores
            })
            
    return students, headers
```

**calculate_student_average() Hints:**
```python
if not scores:
    return 0.0

valid_scores = [s for s in scores if s is not None]
if not valid_scores:
    return 0.0
    
return sum(valid_scores) / len(valid_scores)
```

**get_letter_grade() Hints:**
```python
if average >= 90:
    return "A"
elif average >= 80:
    return "B"
elif average >= 70:
    return "C"
elif average >= 60:
    return "D"
else:
    return "F"
```

### Statistical Calculations

**Class Average:**
```python
def calculate_class_average(students):
    total_score = 0
    total_assignments = 0
    
    for student in students:
        total_score += sum(student['scores'])
        total_assignments += len(student['scores'])
    
    return total_score / total_assignments if total_assignments > 0 else 0
```

**Grade Distribution:**
```python
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for student in students:
    average = calculate_student_average(student['scores'])
    letter = get_letter_grade(average)
    grade_counts[letter] += 1
```

**Top Performers:**
```python
# Create list of (name, average) tuples
student_averages = []
for student in students:
    avg = calculate_student_average(student['scores'])
    student_averages.append((student['name'], avg))

# Sort by average (highest first)
student_averages.sort(key=lambda x: x[1], reverse=True)

# Get top 3
top_3 = student_averages[:3]
```

### Assignment Analysis

**Assignment Averages:**
```python
assignment_averages = {}

for i, assignment in enumerate(headers):
    total = 0
    count = 0
    
    for student in students:
        if i < len(student['scores']):
            total += student['scores'][i]
            count += 1
    
    assignment_averages[assignment] = total / count if count > 0 else 0
```

### Display Formatting

**Student Report:**
```python
def generate_student_report(student, headers):
    scores = student['scores']
    average = calculate_student_average(scores)
    letter = get_letter_grade(average)
    min_score, max_score = find_min_max_scores(scores)
    
    print(f"\n{student['name']}")
    
    # Show individual scores
    score_details = []
    for i, score in enumerate(scores):
        if i < len(headers):
            score_details.append(f"{headers[i]}({score})")
    
    print(f"  Scores: {', '.join(score_details)}")
    print(f"  Average: {average:.1f}%")
    print(f"  Grade: {letter}")
    print(f"  Highest: {max_score}")
    print(f"  Lowest: {min_score}")
```

### Error Handling

**File Not Found:**
```python
try:
    with open(filename, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print(f"❌ File '{filename}' not found!")
    return [], []
```

**Invalid Data:**
```python
def validate_score(score_str):
    try:
        score = float(score_str.strip())
        if 0 <= score <= 100:
            return score
        else:
            return None  # Invalid range
    except ValueError:
        return None  # Not a number
```

### Common Issues and Solutions

**Issue: Empty CSV File**
```python
if not lines or len(lines) < 2:
    print("CSV file is empty or has no student data")
    return [], []
```

**Issue: Inconsistent Data**
```python
# Handle students with different numbers of assignments
max_assignments = len(headers)
for student in students:
    while len(student['scores']) < max_assignments:
        student['scores'].append(None)  # Missing assignment
```

**Issue: Division by Zero**
```python
# Always check before dividing
if total_students > 0:
    percentage = (grade_counts[grade] / total_students) * 100
else:
    percentage = 0
```

### Debugging Tips

1. **Print CSV parsing**:
   ```python
   print(f"Headers: {headers}")
   print(f"First student: {students[0] if students else 'None'}")
   ```

2. **Check data types**:
   ```python
   print(f"Score type: {type(student['scores'][0])}")
   ```

3. **Validate calculations**:
   ```python
   print(f"Manual average: {sum([95,88,92])/3}")
   ```

### AI Partnership Hints

**Good prompts to try:**
- "How do I calculate the median of a list in Python?"
- "What's an efficient way to process CSV data without pandas?"
- "How can I handle missing data when calculating averages?"

**Remember:** Start with basic CSV reading, then add statistical calculations!

