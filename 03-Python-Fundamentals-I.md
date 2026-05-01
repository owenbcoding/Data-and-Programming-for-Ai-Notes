# Python Fundamentals for ML/AI Engineers (Part I)

Part I focuses on core syntax and small programs: how Python represents information, how control flows, and how to package logic in functions. These skills are prerequisites for data work in Pandas (Part II builds on this file with more Python for ML prep).

**Learning path:** This is step 3 in [00-START-HERE.md](00-START-HERE.md). Next: [04-Python-Fundamentals-II.md](04-Python-Fundamentals-II.md).

---

## Learning outcomes (Part I)

After working through this unit, you should be able to:

- Run Python in a consistent environment (script or notebook) and read tracebacks without panic.
- Use variables, built-in types, and operators correctly (numbers, strings, booleans, type quirks that bite beginners).
- Control program flow with conditionals and loops, including iterating over common structures.
- Define and call functions with parameters, return values, and sensible scope habits.
- Use lists (and basic sequences) to hold and transform data—the shape most tabular code builds on later.

---

## 1. Environment and running code

- Interpreter vs script vs notebook (when each is appropriate for ML notes).
- `python`, `pip`, virtual environments (short checklist—you will reuse this setup for Pandas).

_Add your commands, paths, and gotchas here._

---

## 2. Variables, types, and operators

- Assignment, naming, and mutability (what “rebinding” means).
- `int`, `float`, `str`, `bool`; safe conversion with `int()`, `float()`, `str()`.
- Arithmetic, comparisons, logical `and` / `or` / `not`.
- Common pitfalls: integer division, floating-point rounding, string vs number concatenation.

_Notes and examples:_

---

## 3. Strings and basic text handling

- Literals, quotes, escaping, multiline strings.
- Indexing, slicing, immutability.
- Useful methods: `strip`, `lower`, `split`, `join`, `replace` (patterns you will use when cleaning text features later).

_Notes and examples:_

---

## 4. Control flow

- `if` / `elif` / `else`; truthiness; guarding against empty inputs.
- `for` loops, `range`, iterating over strings and lists.
- `while` loops and termination conditions.
- `break`, `continue`, and when *not* to use them.

_Notes and examples:_

---

## 5. Functions

- Defining functions, parameters, default arguments, keyword arguments.
- Return values vs side effects; why “pure” functions are easier to test.
- Docstrings and naming for future-you.

_Notes and examples:_

---

## 6. Lists and sequences (Part I scope)

- Creating, indexing, slicing, copying (alias vs copy).
- Methods: `append`, `extend`, `pop`, `sort` vs `sorted`.
- List comprehensions as readable one-pass transforms (intro level).
- Optional touchpoint: tuples as fixed records; when lists are still the right default.

_Notes and examples:_

---

## Quick reference (fill as you go)

| Topic        | Syntax / idiom | Remember |
|-------------|----------------|----------|
| Type check  | `type(x)`      |          |
| Length      | `len(seq)`     |          |
| Last item   | `seq[-1]`      |          |
| Slice copy  | `seq[:]`       |          |

---

## Exercises and scratch work

_Paste Codecademy exercises, snippets, and mistakes worth keeping below._

---

## See also

- Previous: [02-Data-Literacy.md](02-Data-Literacy.md)
- Next: [04-Python-Fundamentals-II.md](04-Python-Fundamentals-II.md)
