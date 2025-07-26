# Citation Examples for Authors

This document shows how to use citations in the book chapters.

## In-text Citations

### Single Author
```markdown
As @knuth84 argues, literate programming combines documentation with source code.
```

### Multiple Authors
```markdown
Recent studies show that AI code generators significantly impact novice learners [@kazemitabaar2023studying; @becker2023teaching].
```

### Page Numbers
```markdown
According to Downey [-@downey2024think, 45], "thinking like a computer scientist" involves...
```

### Suppress Author
```markdown
The concept of computational thinking [-@wing2006computational] has become central to CS education.
```

## Common Citation Patterns

### Pedagogical Foundations
```markdown
This book's approach builds on constructionist learning theory [@papert1980mindstorms] and recent research on AI in education [@denny2024computing].
```

### AI and Learning
```markdown
While AI can generate code instantly, research shows that understanding remains crucial for learning [@becker2023teaching; @macneil2023experiences].
```

### Active Learning
```markdown
Following peer instruction methodology [@porter2013halving], each chapter includes...
```

## Bibliography Management

1. Add new references to `references.bib` in BibTeX format
2. Use citation keys that follow the pattern: `authorYEARfirstword`
3. Include DOIs when available for easy reader access

## Citation Style

We use Chicago Author-Date style, which produces citations like:
- (Knuth 1984)
- (Becker et al. 2023)
- (Wing 2006, 33–35)

## Required Fields by Type

### Journal Articles
- author, title, year, journal, volume, pages, doi

### Books  
- author, title, year, publisher, address, edition (if not first)

### Conference Papers
- author, title, year, booktitle, pages, doi

### Online Resources
- author, title, year, url, urldate (access date)