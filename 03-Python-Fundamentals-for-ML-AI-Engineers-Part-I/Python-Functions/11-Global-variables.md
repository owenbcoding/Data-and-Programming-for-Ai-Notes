# Global Variables

Global variables are variables defined outside functions that are accessible throughout the program.

## Characteristics
- Defined outside functions
- Accessible throughout the program
- Can be accessed and modified by functions
- Created when program starts
- Persist until program ends

## Accessing Global Variables
- Functions can read global variables
- Functions can modify global variables with `global` keyword
- Global variables can be accessed anywhere in the program
- Global variables exist throughout program execution

## Modifying Global Variables
- Use `global` keyword to modify globals in functions
- Without `global`, assignment creates local variable
- Global modification affects entire program
- Can lead to unexpected side effects
- Should be used sparingly

## Best Practices
- Minimize use of global variables
- Use constants for unchanging global values
- Use uppercase for global constants
- Document global variables clearly
- Consider using classes instead of globals