# Using Collapsible Details Sections

This guide shows how to create collapsible details/summary sections for exercise answers, hints, and other content.

## Basic HTML Details

The simplest way to create a collapsible section:

```markdown
<details>
<summary>Click to show answer</summary>

The answer content goes here. It can include:
- Multiple paragraphs
- Lists
- Code blocks
- Any other content

</details>
```

## Exercise Solutions

For exercise solutions, use the special class:

```markdown
<details class="exercise-solution">
<summary>Show Solution</summary>

```python
# Solution code here
print("Hello, World!")
```

**Explanation**: The code prints a greeting message.

</details>
```

## Exercise Hints

For hints that don't give away the full answer:

```markdown
<details class="exercise-hint">
<summary>Need a hint?</summary>

Look at the quotation marks - are they matching?

</details>
```

## Using the Details Filter

The Quarto filter provides a cleaner syntax:

```markdown
::: {.details}
### Show Answer

Your answer content here.
:::
```

This automatically creates a collapsible section with "Show Answer" as the summary.

## Multiple Sequential Details

For step-by-step reveals:

```markdown
<details>
<summary>Step 1: Understanding the Problem</summary>

First, let's break down what we need to do...

</details>

<details>
<summary>Step 2: Planning the Solution</summary>

Now we can plan our approach...

</details>

<details>
<summary>Step 3: Complete Solution</summary>

Here's the full solution...

</details>
```

## Nested Details

For progressive disclosure:

```markdown
<details>
<summary>Hints</summary>

<details>
<summary>Hint 1: Small hint</summary>
Check your variable names.
</details>

<details>
<summary>Hint 2: Bigger hint</summary>
Python is case-sensitive. `Print` is not the same as `print`.
</details>

<details>
<summary>Hint 3: Give away</summary>
Change `Print` to `print` on line 3.
</details>

</details>
```

## Inline Details

For small reveals within text:

```markdown
The function returns `[details-inline]42[/details-inline]` when given valid input.
```

## Best Practices

### 1. Clear Summary Text
- ✅ "Show Solution"
- ✅ "Click for Answer"  
- ✅ "Need a Hint?"
- ❌ "Click Here"
- ❌ "Answer"

### 2. Progressive Disclosure
Start with hints before showing full solutions:

```markdown
<details class="exercise-hint">
<summary>Hint 1</summary>
What does the error message say?
</details>

<details class="exercise-hint">
<summary>Hint 2</summary>
Look at line 3 - something's missing.
</details>

<details class="exercise-solution">
<summary>Show Full Solution</summary>
The parentheses were missing...
</details>
```

### 3. Accessibility
- Always use descriptive summary text
- Ensure content makes sense when expanded
- Test with keyboard navigation

### 4. Mobile Considerations
- Keep summary text concise
- Ensure touch targets are large enough
- Test on small screens

## Styling Details Sections

Custom styles are automatically applied based on class:

| Class | Purpose | Style |
|-------|---------|-------|
| `exercise-solution` | Full solutions | Green theme |
| `exercise-hint` | Hints | Blue theme |
| `multiple-choice` | Quiz answers | Neutral theme |
| `inline-details` | Inline reveals | Compact style |

## Output Format Support

Details sections work across all output formats:

- **HTML**: Native `<details>` element with full interactivity
- **PDF**: Styled boxes with "Answer:" labels
- **EPUB**: JavaScript-free collapsible sections
- **Print**: Automatically expanded with clear labels

## Examples in Context

### Exercise with Progressive Hints

```markdown
### Exercise: Fix the Greeting

This code has an error:

```python
Print("Hello, World!)
```

<details class="exercise-hint">
<summary>Hint 1: Check the syntax</summary>
There are two syntax errors in this line.
</details>

<details class="exercise-hint">
<summary>Hint 2: More specific</summary>
1. Python commands are case-sensitive
2. Quotation marks must match
</details>

<details class="exercise-solution">
<summary>Show Solution</summary>

```python
print("Hello, World!")
```

**What was wrong:**
1. `Print` should be `print` (lowercase)
2. Missing closing quotation mark

</details>
```

### Multiple Choice with Feedback

```markdown
What will this code print?

```python
x = 5
y = 3
print(x + y)
```

<details class="multiple-choice incorrect">
<summary>A) 53</summary>
Incorrect. The `+` operator adds numbers, it doesn't concatenate them.
</details>

<details class="multiple-choice correct">
<summary>B) 8</summary>
Correct! The code adds 5 + 3 = 8.
</details>

<details class="multiple-choice incorrect">
<summary>C) "5 + 3"</summary>
Incorrect. This would only happen if we put quotes around the expression.
</details>
```