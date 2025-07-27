# Hints for Mad Libs Generator 📝

## Stuck? Here are progressive hints to help you!

### Hint 1: Getting Started with Input
<details>
<summary>Click to reveal hint</summary>

Each input needs to be stored in a variable:
```python
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
```
Make sure each variable has a different name!
</details>

### Hint 2: Making Clear Prompts
<details>
<summary>Click to reveal hint</summary>

Help users give you the right type of word:
```python
# Good prompts:
animal = input("Enter an animal (like cat, dog, elephant): ")
color = input("Enter a color: ")
verb_ing = input("Enter a verb ending in -ing (like running, jumping): ")

# Less helpful prompt:
word1 = input("Enter a word: ")  # User doesn't know what type!
```
</details>

### Hint 3: Building Your Story
<details>
<summary>Click to reveal hint</summary>

Method 1 - Using concatenation:
```python
story = "Once upon a time, a " + adjective1 + " " + animal + " decided to " + verb1 + "."
print(story)
```

Method 2 - Using multiple arguments in print:
```python
print("Once upon a time, a", adjective1, animal, "decided to", verb1 + ".")
```

Note the `+ "."` to attach the period without a space!
</details>

### Hint 4: Making Stories Readable
<details>
<summary>Click to reveal hint</summary>

Break long stories into multiple lines:
```python
print("Here's your story:\n")  # \n creates a blank line
print("The", adjective1, noun1, "Adventure")
print("=" * 25)  # Creates a line for decoration
print()  # Blank line
print("Once upon a time, a", adjective1, animal)
print("decided to", verb1, "to the", place + ".")
print("It was a", adjective2, "day!")
```
</details>

### Hint 5: Complete Basic Structure
<details>
<summary>Click to reveal hint</summary>

Your program flow should be:
```python
# 1. Welcome message
print("Welcome to Mad Libs!")

# 2. Collect all inputs
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
# ... more inputs ...

# 3. Display the story
print("\nYour Mad Libs Story:")
print("=" * 30)
# ... story lines ...

# 4. Thank the user
print("\nThanks for playing!")
```
</details>

## Still Stuck?

### Common Issues:

**"NameError: name 'variable' is not defined"**
- Make sure you've collected input before using it in the story
- Check spelling of variable names (Python is case-sensitive!)

**Story has weird spacing**
- When using `+`, add spaces: `" " + word + " "`
- When using commas in print, spaces are automatic

**Input seems to skip or not work**
- Make sure each input is saved to a different variable
- Don't reuse the same variable name

### Learning Questions:

Before looking at the solution, can you answer:
1. Why do we need different variable names for each input?
2. What's the difference between `print(word1 + word2)` and `print(word1, word2)`?
3. How would you check if someone entered an empty string?
4. Could you make a Mad Libs with 20 inputs? What would be challenging?

### Mad Libs Story Ideas:

If you're stuck on story ideas, try these templates:
- **Adventure**: "The [ADJECTIVE] [NOUN] [VERB-PAST] to the [PLACE]..."
- **Recipe**: "To make [ADJECTIVE] [FOOD], first [VERB] the [NOUN]..."
- **News Report**: "Breaking: [ADJECTIVE] [ANIMAL] [VERB-ING] at [PLACE]!"
- **Fairy Tale**: "Once upon a [NOUN], a [ADJECTIVE] [CHARACTER] [VERB-PAST]..."

Remember: The sillier the story, the funnier the Mad Libs! 🎭