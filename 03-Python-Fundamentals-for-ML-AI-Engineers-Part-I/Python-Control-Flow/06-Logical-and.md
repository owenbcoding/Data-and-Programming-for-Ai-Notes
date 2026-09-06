# Logical and

The `and` operator performs logical AND operation on boolean values.

## and Operator
- Returns True only if both operands are True
- Returns False if either operand is False
- Short-circuits evaluation
- Has lower precedence than comparison operators
- Can chain multiple conditions

## Short-Circuit Evaluation
The `and` operator stops evaluating as soon as it finds a False value (because the result will be False regardless of remaining values).

## Use Cases
- Multiple conditions that must all be true
- Checking multiple validation criteria
- Complex conditional logic
- Combining boolean expressions
- Filtering data

## Truthiness
Non-boolean values are evaluated for truthiness before the logical operation is applied.