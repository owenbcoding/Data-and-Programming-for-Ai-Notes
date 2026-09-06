# Variable Scope

Variable scope determines where variables are accessible in your code.

## Local Variables
- Defined inside functions
- Only accessible within the function
- Created when function is called
- Destroyed when function exits
- Not accessible outside function

## Global Variables
- Defined outside functions
- Accessible throughout the program
- Can be accessed and modified by functions
- Created when program starts
- Persist until program ends

## Scope Rules
- Local variables take precedence over global variables
- Functions can access global variables
- Functions can modify global variables with `global` keyword
- Variables created in blocks are still local to function

## Best Practices
- Minimize use of global variables
- Use parameters to pass data to functions
- Return values from functions rather than modifying globals
- Keep scope as local as possible
- Use descriptive variable names to avoid confusion