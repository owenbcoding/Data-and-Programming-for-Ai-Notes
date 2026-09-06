# Local Variables

Local variables are variables defined within a function that are only accessible within that function.

## Characteristics
- Defined inside functions
- Only accessible within the function
- Created when function is called
- Destroyed when function exits
- Not accessible outside function

## Scope
- Limited to the function
- Shadows global variables with same name
- Not accessible from other functions
- Not accessible outside any function
- Exist only during function execution

## Advantages
- Prevent naming conflicts
- Improve code modularity
- Enable function independence
- Reduce unexpected side effects
- Make code more predictable

## Best Practices
- Use local variables when possible
- Pass data through parameters
- Return results rather than modifying globals
- Keep variable scope minimal
- Use descriptive names