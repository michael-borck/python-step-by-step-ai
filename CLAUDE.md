# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Quarto Book project titled "Python Step by Step: Learning with AI" - a revolutionary approach to teaching Python programming where AI is embraced as a learning partner, not avoided. The book's philosophy is "Master Python by Learning How to Think With AI."

## Commands

### Building and Previewing
- **Preview the book (with live reload)**: `quarto preview`
- **Build HTML version**: `quarto render --to html`
- **Build PDF version**: `quarto render --to pdf`
- **Build all formats**: `quarto render`

### Using Profiles
- **Enhanced HTML**: `quarto render --profile html`
- **Professional PDF**: `quarto render --profile pdf`
- **E-reader EPUB**: `quarto render --profile epub`

## Architecture and Structure

### Content Philosophy
**"Learning with AI" Approach**: 
- Each chapter starts with concepts, not syntax
- AI is used as an exploration tool throughout
- Focus on mental models and patterns
- Students learn to be architects who guide AI

### Book Structure
- **Part 0**: Your AI Learning Partnership
- **Part I**: Computational Thinking (Weeks 1-4) - Concepts: I/O, Storage, Decisions, Patterns
- **Part II**: Building Systems (Weeks 5-8) - Modularity, Data Structures, Persistence, Integration
- **Part III**: Real-World Programming (Weeks 9-12) - Data, APIs, Interaction, Architecture
- **Part IV**: Your Journey Forward

### Chapter Structure Pattern
1. **The Concept First** - No code, just understanding
2. **Understanding Through Real Life** - Relatable examples
3. **Discovering with Your AI Partner** - Exploration prompts
4. **From Concept to Code** - Syntax emerges from need
5. **Mental Model Building** - Visual/conceptual understanding
6. **Prompt Evolution Exercise** - Core skill development
7. **Common AI Complications** - What AI typically overcomplicates
8. **Exercises** - New types: Concept Recognition, Prompt Engineering, Pattern Matching, Model Building, Architect First

### The Three Learning Strategies (formerly Three Rules)
1. **Understand the Concept Before the Code**
2. **Use AI to Explore, Not to Avoid Learning**
3. **Build Mental Models, Not Just Working Programs**

### Progressive AI Skills Development
- **Weeks 1-4**: AI as Concept Explorer
- **Weeks 5-8**: AI as Implementation Assistant
- **Weeks 9-12**: AI as Code Producer (Student as Architect)

### Exercise System Evolution
- **Concept Recognition** - Identify patterns without code
- **Prompt Engineering** - Develop AI communication skills
- **Pattern Matching** - Find concepts in complex code
- **Model Building** - Create mental models
- **Architect First** - Design before implementation

### Supporting Files
- `references.bib` - Bibliography in BibTeX format
- `cover.png` - Book cover image
- `notes/python-step-by-step-book.md` - Detailed book outline
- `notes/smaple-chapter-0.md` - Sample chapter (note typo in filename)
- `notes/smaple-chapter-1.md` - Sample chapter (note typo in filename)
- Templates in `/templates/` for consistent content creation

## Key Differences from Traditional Programming Books

1. **Concepts First**: Each topic starts with understanding, not syntax
2. **AI Integration**: AI is used throughout as a learning tool
3. **Prompt Evolution**: Students learn to communicate effectively with AI
4. **Mental Models**: Focus on how things work, not just making them work
5. **Architect Mindset**: Students design solutions, AI helps implement

## Writing Guidelines

### Chapter Development
- Start with real-world concept explanation
- Use AI exploration prompts to discover patterns
- Show AI's overcomplicated version first
- Guide toward simplified understanding
- Build mental models before showing syntax

### Exercise Creation
- Focus on understanding over implementation
- Include prompt engineering practice
- Emphasize pattern recognition
- Require design before coding
- Use AI as a learning partner, not answer generator

### Expression Explorer Callouts
- Add "Expression Explorer" callout boxes when introducing operators
- Focus on patterns and behavior, not syntax memorization
- Encourage AI exploration with specific prompts
- Show how same operators work differently with different types
- Keep explanations brief and discovery-oriented

### Project Structure
- Students architect solutions first
- AI assists with implementation
- Focus on simplification and understanding
- Reflection on AI partnership experience

## Important Notes

- The book acknowledges AI can write code faster, but positions students as architects
- Every chapter should reinforce: "You're learning to think, AI helps you build"
- Avoid "don't use AI" messaging - instead show how to use it effectively
- Examples should demonstrate prompt evolution and simplification