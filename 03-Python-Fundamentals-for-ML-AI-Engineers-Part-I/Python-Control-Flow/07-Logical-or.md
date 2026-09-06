# Logical or

The `or` operator performs logical OR operation on boolean values.

## or Operator
- Returns True if either operand is True
- Returns False only if both operands are False
- Short-circuits evaluation
- Has lower precedence than `and` operator
- Can chain multiple conditions

## Short-Circuit Evaluation
The `or` operator stops evaluating as soon as it finds a True value (because the result will be True regardless of remaining values).

## Use Cases
- Multiple conditions where any one can be true
- Fallback or default values
- Error handling
- Option selection
- Permission checking

## Truthiness
Non-boolean values are evaluated for truthiness before the logical operation is applied.