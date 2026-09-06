# Removing Items

Items can be removed from lists using various methods.

## Removal Methods
- `remove()` removes first occurrence
- `pop()` removes by index
- `del` statement removes by index
- `clear()` removes all items
- List comprehension for conditional removal

## remove() Method
- Removes first occurrence of value
- Raises ValueError if not found
- Modifies list in place
- Cannot remove by index
- Only removes one occurrence

## pop() Method
- Removes and returns element
- Removes last element by default
- Can specify index
- Modifies list in place
- Returns removed value

## del Statement
- Removes by index
- Cannot return value
- Can delete ranges
- Can delete entire list
- Does not return value