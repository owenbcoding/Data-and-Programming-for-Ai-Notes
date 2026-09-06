# Mean

## What is the Mean?
The mean (or average) is the sum of all values divided by the number of values. It's the most common measure of central tendency and represents the "balance point" of a distribution.

## Calculating the Mean

### Arithmetic Mean
- Sum all values
- Divide by count of values
- Formula: μ = Σx/n (population) or x̄ = Σx/n (sample)
- Most commonly used type of mean

### Example Calculation
```python
values = [4, 8, 15, 16, 23, 42]
mean = sum(values) / len(values)
# mean = 108 / 6 = 18
```

## Properties of the Mean

### Mathematical Properties
- Sum of deviations equals zero
- Minimizes squared deviations
- Sensitive to extreme values
- Unique for any dataset
- Can be calculated for any numerical data

### Interpretation
- Represents the "typical" value
- Balance point of distribution
- Center of mass metaphor
- Expected value in probability
- Used in many statistical formulas

## When to Use the Mean

### Appropriate Situations
- Symmetric distributions
- No extreme outliers
- Continuous numerical data
- When mathematical properties needed
- For normally distributed data

### Inappropriate Situations
- Highly skewed distributions
- Categorical data
- Ordinal data with unknown intervals
- Data with extreme outliers
- Multi-modal distributions

## Limitations and Issues

### Sensitivity to Outliers
- Single extreme value can dramatically change mean
- May not represent "typical" value
- Can be misleading in skewed data
- Example: Income data (billionaires skew mean)
- Consider median as alternative

### Skewed Distributions
- Mean pulled toward tail
- May not be central value
- Better measures exist for skewed data
- Median often more representative
- Consider distribution shape

### Categorical Data
- Cannot calculate meaningful mean
- Categories have no numeric meaning
- Mode is appropriate measure
- Example: Mean of "red, blue, green" meaningless
- Must use appropriate central tendency

## Types of Means

### Arithmetic Mean
- Most common type
- Simple average
- Used for most applications
- Assumes equal weighting
- Default interpretation of "mean"

### Geometric Mean
- Product of values, then nth root
- Useful for rates and ratios
- Less affected by extreme values
- Used for growth rates
- Formula: (Πx)^(1/n)

### Harmonic Mean
- Reciprocal of arithmetic mean of reciprocals
- Useful for rates and speeds
- Most affected by small values
- Used in averaging rates
- Formula: n / Σ(1/x)

### Weighted Mean
- Different weights for different values
- Accounts for importance/frequency
- Common in survey data
- Formula: Σ(w*x) / Σw
- Used when values have different significance

## Mean in Different Contexts

### Sample vs. Population
- **Sample mean (x̄)**: Estimate from subset
- **Population mean (μ)**: True parameter
- Sample mean estimates population mean
- Uncertainty in sample mean
- Confidence intervals for mean

### Grouped Data
- Mean of group means (weighted)
- Overall mean vs. subgroup means
- Simpson's paradox possible
- Careful interpretation needed
- Consider group sizes

### Time Series
- Moving averages
- Trend analysis
- Seasonal adjustment
- Exponential smoothing
- Forecasting applications

## Statistical Applications

### Hypothesis Testing
- t-tests compare means
- ANOVA compares multiple means
- Confidence intervals for means
- Power analysis involves means
- Effect sizes often based on means

### Regression Analysis
- Mean of dependent variable
- Predicted values as conditional means
- Residuals centered on zero mean
- R-squared relates to variance around mean
- Mean squared error as loss function

### Quality Control
- Process mean monitoring
- Control charts use means
- Capability analysis
- Six sigma methodology
- Process improvement targets

## Practical Considerations

### Calculation Issues
- Missing data handling
- Numerical precision
- Large dataset computation
- Streaming data calculation
- Database aggregation

### Interpretation Guidelines
- Always consider distribution shape
- Compare with median
- Report measure of spread
- Contextualize the value
- Note any limitations

### Communication
- Explain which mean used
- Provide context for interpretation
- Compare to relevant benchmarks
- Visualize with distribution
- Note uncertainty when appropriate

## Common Mistakes

### Using Mean Inappropriately
- For categorical data
- With extreme outliers
- For highly skewed data
- Without checking distribution
- As sole summary statistic

### Misinterpretation
- Assuming mean represents all values
- Ignoring variability
- Overstating precision
- Not considering sample size
- Missing context

### Calculation Errors
- Including non-numerical data
- Incorrect count of values
- Wrong formula application
- Precision issues
- Missing data mishandling

## Best Practices

### Analysis
- Always examine distribution first
- Calculate multiple central tendency measures
- Consider appropriate measure for context
- Report uncertainty for sample means
- Visualize alongside distribution

### Reporting
- Specify type of mean calculated
- Provide measure of spread
- Note sample size
- Discuss any data limitations
- Contextualize findings

### Decision Making
- Consider if mean is appropriate measure
- Look at full distribution
- Understand outliers' impact
- Use multiple metrics
- Consider practical significance