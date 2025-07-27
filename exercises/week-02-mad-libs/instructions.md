# Week 2 Project: Mad Libs Generator 📝

## Overview

Create an interactive Mad Libs game that collects words from the user and inserts them into a funny story. This project reinforces concepts from Week 2: variables, string manipulation, and the `input()` function.

## Learning Objectives

By completing this project, you will:
- ✓ Use `input()` to collect information from users
- ✓ Store user responses in variables
- ✓ Combine strings using concatenation and f-strings
- ✓ Create an interactive program flow
- ✓ Handle different types of user input

## Core Requirements (🟢 Basic)

Your Mad Libs generator must:

1. **Ask for at least 8 different words** from the user including:
   - At least 2 nouns
   - At least 2 verbs
   - At least 2 adjectives
   - At least 2 other types (adverb, color, name, etc.)

2. **Store each input** in a descriptive variable

3. **Create a story** that uses all collected words

4. **Display the complete story** with proper formatting

5. **Make the story funny** or entertaining when words are inserted

### Example Interaction
```
🎭 Welcome to Mad Libs! 🎭

I'll ask you for some words, then create a silly story!

Enter a noun: pizza
Enter a verb: dance
Enter an adjective: purple
Enter an animal: elephant
Enter a food: spaghetti
Enter a verb ending in -ing: singing
Enter a color: green
Enter a place: moon

Here's your Mad Libs story:

The Purple Pizza Adventure
==========================

Once upon a time, a purple elephant decided to dance
to the moon. On the way, they met a pizza who was
singing loudly. Together, they ate green spaghetti
and lived happily ever after!

Thanks for playing Mad Libs! 🎉
```

## Implementation Guide

### Step 1: Plan Your Story
Write your story template first, marking where words will go:
- "The [ADJECTIVE] [NOUN] decided to [VERB]..."

### Step 2: Determine Word Types
List all the word types you'll need to collect.

### Step 3: Collect User Input
Use clear prompts that specify the type of word needed.

### Step 4: Build Your Story
Insert the collected words into your story template.

### Step 5: Display Results
Format the output to be clear and entertaining.

## Challenges

### 🟡 Intermediate Challenges

1. **Input Validation**: Check if users enter empty strings and ask again

2. **Multiple Stories**: Let users choose between 2-3 different story templates

3. **Grammar Helper**: Add "a" or "an" automatically based on the word

4. **Title Generator**: Create a dynamic title using some of the input words

### 🔴 Advanced Challenges

1. **Story Categories**: Offer genres (adventure, sci-fi, fairy tale) with appropriate templates

2. **Word Counter**: Tell users how many words they've entered and how many remain

3. **Replay Option**: Ask if they want to play again with a new story

4. **Save Story**: Offer to save their Mad Libs to a text file

### 🟣 AI Partnership Challenge

1. **Template Evolution**:
   - Ask AI for a Mad Libs template
   - Simplify it to use only Week 2 concepts
   - Compare complexity levels

2. **Prompt Engineering**:
   - "Create a Mad Libs game"
   - "Create a simple Mad Libs using only input() and print()"
   - Document the differences

### ⭐ Reflection Exercise

Write a short paragraph answering:
- What made a Mad Libs story funny vs. boring?
- How did variable names affect code readability?
- What input validation would improve user experience?
- How did AI suggestions differ from your approach?

## Testing Your Program

Run your program multiple times with different inputs:
- [ ] Try normal words
- [ ] Try silly/unexpected words
- [ ] Try leaving inputs blank
- [ ] Check story makes grammatical sense
- [ ] Verify all input words appear in the story

## Common Mistakes to Avoid

1. **Not storing inputs** - Each input() needs to be saved to a variable
2. **Confusing variable names** - Use descriptive names like `adjective1` not `a1`
3. **Missing spaces** - Remember spaces when concatenating strings
4. **Reusing variables** - Each input needs its own variable
5. **Unclear prompts** - Tell users exactly what type of word you need

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "Show me different ways to combine strings in Python"
- "How do I make input prompts clearer for users?"
- "What makes a good Mad Libs story template?"

### ❌ Avoid These Prompts
- "Write a complete Mad Libs program with 20 inputs"
- "Add advanced NLP to validate word types"
- "Create a GUI version with dropdowns"

## String Combination Methods

You've learned several ways to combine strings:

```python
# Method 1: Concatenation with +
story = "The " + adjective + " " + noun + " ran quickly."

# Method 2: f-strings (if covered)
story = f"The {adjective} {noun} ran quickly."

# Method 3: Multiple prints
print("The", adjective, noun, "ran quickly.")
```

Choose the method that makes your code clearest!

## Submission Checklist

Before considering your project complete:
- [ ] Program collects at least 8 different words
- [ ] Each word type is clearly requested
- [ ] Story incorporates all collected words
- [ ] Output is well-formatted and readable
- [ ] Story is entertaining with silly word combinations
- [ ] Code includes comments explaining sections
- [ ] You can explain how each line works

## Extension Ideas

Once you've completed the basic requirements:
- Create a Mad Libs that rhymes
- Add sound effects or emoji to enhance the story
- Create educational Mad Libs (history, science themes)
- Make a collaborative Mad Libs for multiple players

## Resources

- Chapter 2: Review variables and assignment
- Chapter 3: Review the `input()` function
- Chapter 4: String manipulation techniques

---

Remember: The best Mad Libs stories are creative and surprising. Have fun with your story templates and encourage silly inputs! 🎭✨