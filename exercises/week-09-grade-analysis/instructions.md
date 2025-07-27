# Week 9 Project: Grade Analysis Tool 📊

## Overview

Create a grade analysis tool that processes student data from CSV files. This project introduces real-world data processing, teaching you to work with structured data files and perform meaningful analysis. Welcome to Part III: Real-World Programming!

## Learning Objectives

By completing this project, you will:
- ✓ Read and process CSV files
- ✓ Analyze data with calculations
- ✓ Generate statistical summaries
- ✓ Create formatted reports
- ✓ Handle real-world data edge cases

## Core Requirements (🟢 Basic)

Your grade analysis tool must:

1. **Load student data from CSV** file containing:
   - Student names
   - Assignment/test scores
   - Categories (homework, quiz, test, etc.)

2. **Calculate for each student**:
   - Average grade
   - Letter grade (A, B, C, D, F)
   - Highest and lowest scores

3. **Generate class statistics**:
   - Class average
   - Grade distribution
   - Top performers

4. **Create a summary report** showing:
   - Individual student summaries
   - Class overview
   - Notable achievements

5. **Handle data issues** gracefully:
   - Missing scores
   - Invalid data
   - Empty files

### Example CSV Format
```csv
Student,HW1,HW2,Quiz1,Test1,HW3,Quiz2,Test2
Alice Johnson,95,88,92,87,90,85,91
Bob Smith,78,82,75,80,85,79,83
Charlie Brown,92,90,88,95,87,91,89
Diana Lee,85,87,90,82,88,86,84
```

### Example Output
```
📊 Grade Analysis Report 📊
========================

Individual Student Reports:
--------------------------

Alice Johnson
  Scores: HW1(95), HW2(88), Quiz1(92), Test1(87), HW3(90), Quiz2(85), Test2(91)
  Average: 89.7%
  Grade: B+
  Highest: 95 (HW1)
  Lowest: 85 (Quiz2)

Bob Smith
  Scores: HW1(78), HW2(82), Quiz1(75), Test1(80), HW3(85), Quiz2(79), Test2(83)
  Average: 80.3%
  Grade: B-
  Highest: 85 (HW3)
  Lowest: 75 (Quiz1)

[... more students ...]

Class Summary:
--------------
Total Students: 4
Class Average: 85.5%

Grade Distribution:
  A: 1 student (25%)
  B: 2 students (50%)
  C: 1 student (25%)
  D: 0 students (0%)
  F: 0 students (0%)

Top Performers:
1. Charlie Brown - 90.3%
2. Alice Johnson - 89.7%
3. Diana Lee - 85.7%

Assignments Analysis:
  Highest Average: HW1 (87.5%)
  Lowest Average: Quiz1 (81.3%)
```

## Implementation Guide

### Step 1: CSV File Reading
Learn to parse CSV files and handle headers.

### Step 2: Data Structure Design
Organize student data in dictionaries/lists.

### Step 3: Calculation Functions
Create functions for averages, grades, statistics.

### Step 4: Report Generation
Format output in clear, readable sections.

### Step 5: Error Handling
Handle missing data and invalid entries.

## CSV Processing Tips

```python
# Reading CSV manually
with open("grades.csv", "r") as file:
    lines = file.readlines()
    headers = lines[0].strip().split(",")
    
    for line in lines[1:]:
        values = line.strip().split(",")
        # Process each row
```

## Challenges

### 🟡 Intermediate Challenges

1. **Weighted Grades**: Different weights for HW, Quiz, Test

2. **Grade Trends**: Show improvement/decline over time

3. **Export Reports**: Save analysis to new file

4. **Missing Data Handling**: Calculate with available scores

5. **Grade Curves**: Apply bell curve adjustments

### 🔴 Advanced Challenges

1. **Multiple Classes**: Analyze different class sections

2. **Visual Charts**: ASCII bar charts for distributions

3. **Predictive Analysis**: Estimate final grades

4. **Custom Grading Scales**: Support different systems

5. **Attendance Integration**: Factor in attendance data

### 🟣 AI Partnership Challenge

1. **Data Analysis Strategies**:
   - Ask AI: "What statistics are most useful for grade analysis?"
   - Learn about quartiles, standard deviation
   - Implement appropriate measures

2. **Report Design**:
   - Get AI's input on clear data presentation
   - Design informative summaries
   - Create actionable insights

### ⭐ Reflection Exercise

Write a short paragraph answering:
- What makes CSV a good format for data storage?
- How did you handle students with missing assignments?
- What insights can teachers gain from this analysis?
- How would you extend this for a real gradebook?

## Testing Your Program

Test these scenarios:
- [ ] Normal CSV loads correctly
- [ ] Handles missing scores (empty cells)
- [ ] Calculates averages accurately
- [ ] Letter grades assigned correctly
- [ ] Statistics compute properly
- [ ] Handles single student files
- [ ] Empty file doesn't crash

## Common Mistakes to Avoid

1. **Assuming all data is valid** - Check for numbers
2. **Division by zero** - Handle empty assignments
3. **Hardcoded column positions** - Use dynamic parsing
4. **Poor grade boundaries** - Clear A/B/C/D/F ranges
5. **Lost precision** - Keep decimals until display

## Grade Scale Reference

```python
def get_letter_grade(average):
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

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "How do I calculate the median of a list in Python?"
- "What's the best way to handle missing data in averages?"
- "How can I sort students by their grades?"

### ❌ Avoid These Prompts
- "Create a full school management system"
- "Add machine learning grade predictions"
- "Build a web interface for grade entry"

## Data Validation Pattern

```python
def parse_score(score_str):
    """Safely convert score string to number"""
    try:
        score = float(score_str)
        if 0 <= score <= 100:
            return score
        else:
            return None  # Invalid score
    except ValueError:
        return None  # Not a number
```

## Submission Checklist

Before considering your project complete:
- [ ] CSV file loads successfully
- [ ] Individual student analysis works
- [ ] Class statistics calculate correctly
- [ ] Report format is clear and readable
- [ ] Handles missing/invalid data
- [ ] Letter grades assigned properly
- [ ] Summary provides useful insights
- [ ] Code is well-organized with functions

## Extension Ideas

Once you've completed the basic requirements:
- Add assignment category analysis
- Create student progress tracking
- Generate parent-friendly reports
- Add comparison between students
- Create "what-if" grade calculators

## Resources

- Chapter 10: Working with CSV files
- Chapter 10: Data processing patterns
- Python docs: String splitting and parsing
- Statistics basics for calculations

---

Remember: Real-world data is messy! Your program should handle imperfect data gracefully while providing valuable insights. 📈✨

