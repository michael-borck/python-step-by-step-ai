# Contributing to Python Step by Step

Thank you for your interest in contributing to "Python Step by Step: Learning with AI"! This guide will help you contribute effectively.

## Ways to Contribute

1. **Report Issues**: Found a typo, error, or confusing explanation? Open an issue!
2. **Suggest Improvements**: Have ideas for better exercises or explanations? We'd love to hear them.
3. **Fix Problems**: Submit pull requests for typos, code errors, or clarity improvements.
4. **Test Content**: Try the exercises and report your experience.

## Before Contributing

1. Check existing issues to avoid duplicates
2. For major changes, open an issue first to discuss
3. Read the book's philosophy in Chapter 0 to understand our approach

## Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/pythonstepbystep/book.git
cd book

# Install Quarto
# See: https://quarto.org/docs/get-started/

# Install pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install

# Preview the book
quarto preview
```

## Content Guidelines

### Writing Style

- **Tone**: Conversational, encouraging, honest about challenges
- **Audience**: Complete beginners with no programming experience
- **Length**: Keep explanations concise but complete
- **Examples**: Always show real scenarios, not abstract concepts

### Code Examples

```python
# ✅ Good: Clear, simple, well-commented
name = "Alice"  # Store the user's name
print("Hello, " + name)  # Display greeting

# ❌ Bad: Too complex for beginners
print(f"Hello, {input('Name: ')}")
```

### Exercise Format

All exercises must follow the 5-level system:

1. **Level 1: Trace** - Predict output without running
2. **Level 2: Fix** - Debug broken code
3. **Level 3: Simplify** - Reduce complexity
4. **Level 4: Explain** - Teach in plain English
5. **Level 5: Apply** - Create something new

Use the templates in `/templates/exercise-template.qmd`.

### AI Integration

- Always show AI's overcomplicated version first
- Then show simplified version
- Explain why the simple version is better
- Include good/bad prompt examples

## Submitting Changes

### For Small Fixes (typos, etc.)

1. Fork the repository
2. Create a branch: `git checkout -b fix-typo-chapter-2`
3. Make your changes
4. Test: `quarto preview`
5. Commit: `git commit -m "fix: Correct typo in Chapter 2"`
6. Push and create a pull request

### For Content Changes

1. Open an issue describing the change
2. Wait for discussion/approval
3. Fork and create a feature branch
4. Make changes following all guidelines
5. Test thoroughly
6. Submit PR with clear description

### Commit Messages

Follow conventional commits:

```
<type>: <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New content or features
- `fix`: Corrections to existing content
- `docs`: Documentation changes
- `style`: Formatting, punctuation
- `refactor`: Restructuring content
- `content`: Chapter or exercise updates
- `chore`: Maintenance tasks

## Code of Conduct

- Be respectful and inclusive
- Remember our audience is beginners
- Provide constructive feedback
- No gatekeeping or elitism
- Celebrate questions, not just answers

## Review Process

1. All PRs are reviewed for:
   - Alignment with book philosophy
   - Technical accuracy
   - Clarity for beginners
   - Proper exercise structure
   - Code quality

2. Reviews may request:
   - Simplification of examples
   - Additional explanation
   - Exercise adjustments
   - Style consistency

## Questions?

- Open an issue with the "question" label
- Check existing discussions
- Review the CLAUDE.md file for technical details

## Recognition

Contributors will be acknowledged in the book's credits section. Thank you for helping make programming education more accessible!

---

Remember: Every expert was once a beginner. Your contribution helps someone start their journey.