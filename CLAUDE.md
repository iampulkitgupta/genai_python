# CLAUDE.md - AI Assistant Guide for genai_python

## Repository Overview

This is a **Python learning repository** that teaches Python programming concepts through practical, themed examples centered around chai (tea) and food-related scenarios. The repository serves as an educational resource with progressive difficulty levels.

**Project Type**: Educational Python examples and exercises
**Primary Theme**: Chai/tea shop scenarios for relatable learning
**Target Audience**: Python learners from beginners to intermediate level

## Codebase Structure

```
genai_python/
├── 00_python/              # Python basics and setup
├── 02_datatypes/           # Data types, variables, and memory concepts
├── 03_conditionals/        # If-elif-else, conditional logic
├── 04_loops/               # For loops, while loops, iteration
├── 05_functions/           # Function definitions, scope, parameters
├── 06_chai_business/       # Module/package structure demo
│   ├── recipes/           # Sub-package with flavor functions
│   └── utlis/             # Utilities (note: "utlis" is the actual spelling)
├── 07_comprehensions/      # List, set, dict, generator comprehensions
├── 12_threads_concurrency/ # Threading and multiprocessing
└── readme.md              # Project readme
```

## Directory Organization Pattern

Each directory follows a numbered or named file structure:
- **Numbered files** (e.g., `chapter_1.py`, `01_token_dispenser.py`) indicate sequential learning progression
- **Named files** (e.g., `tea_size_3.py`) describe specific concept examples
- Files are self-contained examples that can be run independently

## Core Conventions

### 1. Code Style

**Naming Conventions:**
- Variables: `snake_case` (e.g., `sugar_amount`, `cup_size`)
- Functions: `snake_case` (e.g., `brew_chai()`, `take_orders()`)
- Constants: Not heavily used, but follow UPPER_CASE when present

**String Formatting:**
- Primary: **f-strings** (e.g., `f"Initial sugar: {sugar_amount}"`)
- This is the preferred formatting method throughout the codebase

**Code Structure:**
- Simple, educational code prioritizing readability over complexity
- Minimal dependencies (mostly stdlib)
- Direct execution (most files run directly without main guards)
- Some files include commented-out alternative implementations for learning

### 2. Documentation Style

**Function Documentation:**
```python
def generate_bill(chai=0, samosa=0):
    """This function generates the bill for chai and samosa
    :param chai: Number of chai
    :param samosa: Number of samosa
    :return: Total bill
    """
    return chai * 20 + samosa * 10
```

**Inline Comments:**
- Used sparingly, mainly for explaining alternatives
- Often show commented-out code blocks demonstrating different approaches

### 3. Thematic Consistency

The repository uses **chai/tea shop scenarios** consistently:
- Menu items: chai, samosa, biryani, chaat
- Operations: brewing chai, taking orders, serving tokens
- Flavors: masala chai, elachi chai, ginger chai, spicy chai
- Business concepts: pricing, discounts, order processing

**When adding new examples:**
- Maintain the chai/food theme
- Use relatable shop/business scenarios
- Keep examples simple and focused on one concept

## Development Workflow

### Commit Message Format

Follow the **Conventional Commits** pattern:

```
feat: add example demonstrating generator comprehensions
feat: Add dictionary comprehension example for currency conversion
feat: introduce elachi and ginger chai flavor functions
```

**Pattern**: `<type>: <description>`
- **type**: Usually `feat` for new examples/features
- **description**: Clear, concise description starting with lowercase verb
- Examples: "add", "introduce", "demonstrate", "update"

### Branch Strategy

- Main branch: Development happens on main (or master)
- Feature branches: Use `claude/` prefix for AI assistant work
- Format: `claude/claude-md-<session-id>`

### File Creation Guidelines

**When adding new examples:**

1. **Choose appropriate directory** based on the concept being taught
2. **Follow naming convention**:
   - Sequential: `01_`, `02_`, etc. for ordered progression
   - Descriptive: `<concept_name>.py` for standalone examples
   - Chapter format: `chapter_X.py` for series within a topic

3. **Keep it simple**:
   - One concept per file
   - 5-50 lines typically
   - Self-contained and runnable

4. **Use the theme**:
   - Incorporate chai/tea examples
   - Use familiar variables: `chai`, `samosa`, `menu`, `flavours`, etc.

## Key Patterns and Examples

### Pattern 1: Basic Concept Introduction
```python
# File: 02_datatypes/chapter_1.py
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")
print(id(sugar_amount))
```
Simple, focused demonstration of one concept (here: object identity)

### Pattern 2: Interactive Input
```python
# File: 03_conditionals/tea_size_3.py
cup_size = input("Which cup of tea do you require? ").lower()
if cup_size == "small":
    print(f"{cup_size} cup of tea is of Rs10")
```
User interaction for demonstrating conditionals

### Pattern 3: Comprehensions
```python
# File: 07_comprehensions/01_list_compre.py
menu = ["chai", "samosa", "biryani", "samosa chaat"]
samosa = [item for item in menu if "samosa" in item]
```
Concise examples showing comprehension syntax

### Pattern 4: Module Structure
```python
# 06_chai_business/recipes/flavors.py
def elachi_chai():
    return "Elachi Chai"

# 06_chai_business/main.py
# from recipes.flavors import elachi_chai, ginger_chai
```
Demonstrates Python imports and package structure

## AI Assistant Instructions

### When Creating New Examples

1. **Analyze existing files** in the target directory to match style and complexity
2. **Maintain thematic consistency** - use chai/food shop scenarios
3. **Keep it educational** - prioritize clarity over cleverness
4. **One concept per file** - don't combine multiple learning objectives
5. **Use f-strings** for all string formatting
6. **Add docstrings** to functions (follow existing format)
7. **Make it runnable** - file should execute without errors

### When Modifying Existing Files

1. **Read the file first** - understand the concept being taught
2. **Preserve the educational intent** - don't over-complicate
3. **Maintain theme** - keep chai/food references
4. **Test execution** - ensure the file still runs correctly
5. **Keep similar line count** - don't drastically expand simple examples

### When Organizing Code

1. **Directory placement**: Choose based on primary concept:
   - Basics → `00_python`
   - Data structures → `02_datatypes`
   - Control flow → `03_conditionals` or `04_loops`
   - Abstractions → `05_functions`
   - Modules → `06_chai_business`
   - Advanced features → `07_comprehensions`, `12_threads_concurrency`

2. **File naming**: Match existing patterns in that directory

3. **Numbering**: If adding to a sequence, use next available number

### Common Pitfalls to Avoid

❌ **DON'T:**
- Add complex error handling (keep examples simple)
- Use type hints extensively (not the style here)
- Create abstract classes or complex OOP patterns
- Add logging, configuration files, or production patterns
- Use libraries beyond stdlib
- Create tests (this is educational code, not production)

✅ **DO:**
- Use simple, direct Python code
- Include print statements to show output
- Use relatable chai/food examples
- Keep files short and focused
- Follow the f-string convention
- Add docstrings to functions

## Testing and Validation

**No formal test suite** - this is educational code. Validation means:
- Files run without errors: `python path/to/file.py`
- Output demonstrates the concept clearly
- Code is readable and self-explanatory

## Dependencies

**Core**: Python 3.x (no specific version constraints)
**External Libraries**: Minimal - primarily stdlib
- `threading` (12_threads_concurrency)
- Standard modules (`time`, etc.)

**No requirements.txt** - intentionally kept simple for learners

## Examples of Good Additions

### Example 1: Adding a New Comprehension
```python
# 07_comprehensions/05_nested_compre.py
tea_types = ["masala", "ginger", "elachi"]
sizes = ["small", "medium", "large"]

menu = [f"{size} {tea}" for tea in tea_types for size in sizes]
print(menu)
```

### Example 2: Adding a New Function Example
```python
# 05_functions/13_decorators.py
def add_sugar(func):
    """Decorator to add sweetness to chai"""
    def wrapper():
        result = func()
        return f"{result} with sugar"
    return wrapper

@add_sugar
def plain_chai():
    return "Plain chai"

print(plain_chai())
```

## Git Operations

### Creating Commits
```bash
# Stage your changes
git add <files>

# Commit with conventional format
git commit -m "feat: add example demonstrating <concept>"

# Push to branch
git push -u origin <branch-name>
```

### Branch Naming
For AI assistant work: `claude/claude-md-<unique-id>`

## Quick Reference

**Repository Theme**: Chai/tea shop educational examples
**Code Style**: Simple, f-strings, snake_case, minimal complexity
**Commit Format**: `feat: <description>`
**File Pattern**: One concept per file, 5-50 lines typical
**Documentation**: Docstrings for functions, minimal inline comments
**Target**: Educational clarity over production quality

## Recent Development Activity

Based on recent commits:
- Focus on comprehensions (list, set, dict, generator)
- Function concepts (built-in attributes, types, returns)
- Scope and parameter handling
- Module/package structure
- Concurrency basics

## Questions or Clarifications?

When in doubt:
1. Look at similar files in the same directory
2. Keep it simple and educational
3. Maintain the chai/food theme
4. Prioritize readability
5. Use f-strings for formatting

---

**Last Updated**: 2025-11-23
**Repository**: genai_python (Python learning examples)
**Maintained for**: Educational purposes with AI assistance
