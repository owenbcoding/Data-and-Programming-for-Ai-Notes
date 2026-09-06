# Default Arguments

Default arguments are parameters that have default values specified in the function definition.

## Purpose
- Make functions more flexible
- Allow common values to be specified once
- Reduce need for repetitive argument passing
- Simplify function calls
- Provide sensible defaults

## Default Parameter Syntax
Default parameters are specified by assigning a value in the parameter definition.

## Required vs. Default Parameters
- Required parameters must be provided
- Default parameters can be omitted
- Required parameters come first
- Default parameters follow required parameters

## Default Value Types
- Immutable types (strings, numbers, tuples) are safe
- Mutable types (lists, dictionaries) require caution
- Default values are evaluated once at function definition
- Be careful with mutable default values

## Common Use Cases
- Optional parameters
- Configuration values
- Common settings
- Fallback values
- Parameter validation