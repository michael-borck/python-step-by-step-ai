# Hints for Fortune Teller Project 🔮

## Stuck? Here are progressive hints to help you!

### Hint 1: Creating Your Fortune List
<details>
<summary>Click to reveal hint</summary>

Your fortune list should look something like:
```python
fortunes = [
    "A pleasant surprise awaits you.",
    "Your hard work will pay off soon.",
    "An old friend will contact you.",
    # Add more fortunes...
]
```
Remember: Each fortune is a string, separated by commas!
</details>

### Hint 2: Using random.choice()
<details>
<summary>Click to reveal hint</summary>

The `random.choice()` function picks one random item from a list:
```python
selected_fortune = random.choice(fortunes)
```
This stores the randomly selected fortune in a variable.
</details>

### Hint 3: Creating Nice Output
<details>
<summary>Click to reveal hint</summary>

Use multiple `print()` statements for formatting:
```python
print("🔮 Welcome to the Mystic Fortune Teller! 🔮")
print()  # Empty line for spacing
print("Let me gaze into the crystal ball...")
print()
# Continue with your fortune display...
```
</details>

### Hint 4: Complete Basic Structure
<details>
<summary>Click to reveal hint</summary>

Your program structure should be:
1. Import random
2. Create fortune list
3. Print welcome message
4. Select random fortune
5. Print the fortune
6. Print closing message

Each step can be just 1-2 lines of code!
</details>

### Hint 5: Making It More Interesting
<details>
<summary>Click to reveal hint</summary>

Add personality with:
- Emojis: 🔮 ✨ 🌟 🌙 ⭐
- Dramatic pauses: `print("...")` 
- Formatting: Use `\n` for extra line breaks
- Descriptive text: "The mists are clearing..." 

Example:
```python
print("✨ Your fortune: " + selected_fortune + " ✨")
```
</details>

## Still Stuck?

### Common Issues:

**"NameError: name 'random' is not defined"**
- Make sure you have `import random` at the top of your file

**"TypeError: 'str' object is not callable"**
- Check that you're using `random.choice()` not `random.choice`
- Make sure your list variable name doesn't conflict with built-in functions

**Nothing happens when I run the program**
- Make sure you have `print()` statements to display output
- Check that your file is saved before running

### Learning Questions:

Before looking at the solution, can you answer:
1. Why do we need to import random?
2. What's the difference between `fortunes` and `"fortunes"`?
3. How does `random.choice()` know which item to pick?
4. Could you add 20 more fortunes easily? How?

Remember: The struggle is part of learning! Each error teaches you something valuable. 🌟