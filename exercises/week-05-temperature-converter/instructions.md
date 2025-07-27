# Week 5 Project: Temperature Converter 🌡️

## Overview

Create a temperature conversion program using functions. This project introduces modular programming by building reusable functions for different conversions. This is your first step into organizing code professionally!

## Learning Objectives

By completing this project, you will:
- ✓ Create and use functions with parameters
- ✓ Return values from functions
- ✓ Build a menu-driven program
- ✓ Organize code into logical units
- ✓ Practice function naming and documentation

## Core Requirements (🟢 Basic)

Your temperature converter must:

1. **Create separate functions** for each conversion:
   - `celsius_to_fahrenheit(celsius)`
   - `fahrenheit_to_celsius(fahrenheit)`
   
2. **Display a menu** of conversion options

3. **Get user input** for:
   - Conversion type choice
   - Temperature value to convert
   
4. **Call the appropriate function** based on user choice

5. **Display the result** clearly with units

6. **Allow multiple conversions** until user chooses to quit

### Example Interaction
```
🌡️ Temperature Converter 🌡️
==========================

Select conversion type:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Quit

Enter choice (1-3): 1

Enter temperature in Celsius: 25
25.0°C = 77.0°F

Convert another temperature? (yes/no): yes

Select conversion type:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Quit

Enter choice (1-3): 2

Enter temperature in Fahrenheit: 98.6
98.6°F = 37.0°C

Convert another temperature? (yes/no): no

Thanks for using Temperature Converter!
```

## Implementation Guide

### Step 1: Create Conversion Functions
Write functions that take a temperature and return the converted value.

### Step 2: Build the Menu System
Create a function to display options and get user choice.

### Step 3: Input Handling
Get temperature values and validate they're numbers.

### Step 4: Main Program Loop
Coordinate menu, input, conversion, and output.

### Step 5: Format Output
Display results clearly with appropriate decimal places.

## Conversion Formulas

```python
# Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9
```

## Challenges

### 🟡 Intermediate Challenges

1. **Add More Conversions**:
   - Celsius to Kelvin
   - Fahrenheit to Kelvin
   - Kelvin to both C and F

2. **Round Results**: Allow user to specify decimal places

3. **Temperature Validation**: Warn about impossible temperatures (below absolute zero)

4. **Batch Conversion**: Convert a list of temperatures at once

5. **Temperature Facts**: Add interesting facts (water boiling/freezing points)

### 🔴 Advanced Challenges

1. **All-in-One Converter**: Auto-detect input unit and convert to all others

2. **Historical Data**: Save conversion history to file

3. **Temperature Ranges**: Convert and categorize (freezing, cold, warm, hot)

4. **Graphical Display**: Show temperature on ASCII thermometer

5. **Scientific Mode**: Add Rankine scale and other scientific units

### 🟣 AI Partnership Challenge

1. **Function Design**:
   - Ask AI for different ways to structure conversion functions
   - Compare single function vs multiple functions
   - Evaluate readability and reusability

2. **Error Handling**:
   - Get AI's approach to handling invalid inputs
   - Simplify to appropriate level
   - Test edge cases

### ⭐ Reflection Exercise

Write a short paragraph answering:
- Why are functions better than repeating code?
- How did you decide what each function should do?
- What makes a good function name?
- How would you explain functions to a friend?

## Testing Your Program

Test these scenarios:
- [ ] Each conversion type works correctly
- [ ] Negative temperatures convert properly
- [ ] Decimal values work
- [ ] Invalid menu choices are handled
- [ ] Non-numeric temperatures are rejected
- [ ] Program exits cleanly

## Common Mistakes to Avoid

1. **Forgetting return statements** - Functions must return values
2. **Wrong formula application** - Check your math
3. **Integer division issues** - Use proper decimal division
4. **Not calling functions** - Remember the parentheses
5. **Global vs local variables** - Understand scope

## Function Best Practices

```python
# Good function design:
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

# Using the function:
temp_f = celsius_to_fahrenheit(25)
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "Show me different ways to organize temperature conversion functions"
- "How do I validate that user input is a number?"
- "What's the difference between print and return in functions?"

### ❌ Avoid These Prompts
- "Create a complete temperature converter with GUI"
- "Add voice recognition for temperature input"
- "Build a weather station data processor"

## Menu Design Pattern

```python
def display_menu():
    """Display conversion options"""
    print("\nSelect conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

def get_user_choice():
    """Get and validate user's menu choice"""
    choice = input("\nEnter choice (1-3): ")
    # Add validation here
    return choice
```

## Submission Checklist

Before considering your project complete:
- [ ] Two conversion functions work correctly
- [ ] Functions have clear names and purposes
- [ ] Menu system displays options clearly
- [ ] User can perform multiple conversions
- [ ] Input validation prevents crashes
- [ ] Output shows units (°C, °F)
- [ ] Clean exit option works
- [ ] Code is organized with functions

## Extension Ideas

Once you've completed the basic requirements:
- Create a universal unit converter (length, weight, etc.)
- Add temperature conversion charts
- Build a cooking temperature guide
- Create a weather temperature interpreter
- Add historical temperature records

## Resources

- Chapter 6: Review function creation
- Chapter 6: Parameters and return values
- Python docs: Built-in functions
- Math formulas: Temperature conversions

---

Remember: Functions are the building blocks of larger programs. Master them here, and you'll use them everywhere! 🔧✨

