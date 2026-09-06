# Interquartile Range (IQR)

## What is the IQR?
The Interquartile Range (IQR) is the range between the first quartile (Q1) and third quartile (Q3). It represents the middle 50% of data and is a robust measure of variability.

## Calculating the IQR

### Basic Formula
- IQR = Q3 - Q1
- Subtract first quartile from third quartile
- Simple calculation
- Robust measure
- Uses quartile values

### Example
```python
import numpy as np
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
Q1 = np.percentile(data, 25)  # 7.0
Q3 = np.percentile(data, 75)  # 17.0
IQR = Q3 - Q1  # 10.0
```

## Properties of the IQR

### Robustness
- Not affected by extreme values
- Resistant to outliers
- Stable measure of spread
- Less sensitive than range
- Reliable for skewed data

### Interpretation
- Spread of middle 50%
- Typical variability
- Core data range
- Represents "normal" spread
- Excludes extremes

### Mathematical Properties
- Always non-negative
- Scale-dependent
- Units same as original data
- Can be zero (if Q1 = Q3)
- Additive under transformations

## When to Use the IQR

### Appropriate Situations
- Data with outliers
- Skewed distributions
- When robustness needed
- Box plot construction
- Non-parametric analysis

### Inappropriate Situations
- When mathematical properties needed
- For further statistical calculations
- Small samples with limited information
- When full spread important
- For normally distributed data without outliers

## IQR vs. Other Variability Measures

### Comparison with Range
- IQR: middle 50%, robust
- Range: full spread, sensitive
- IQR: more stable
- Range: includes extremes
- IQR: less affected by outliers

### Comparison with Standard Deviation
- IQR: robust, non-parametric
- SD: uses all data, parametric
- IQR: works with ordinal data
- SD: requires interval data
- IQR: less affected by extremes

### Comparison with Variance
- IQR: interpretable units
- Variance: squared units
- IQR: intuitive
- Variance: mathematical convenience
- IQR: robust

## Applications

### Outlier Detection
- **Tukey's Rule**: Values outside Q1 - 1.5×IQR or Q3 + 1.5×IQR
- **Modified Rule**: Use 3×IQR for extreme outliers
- **Visual Detection**: Box plot whiskers
- **Data Cleaning**: Identify problematic values
- **Quality Control**: Monitor process variation

### Box Plots
- Box spans Q1 to Q3
- Box height = IQR
- Whiskers typically extend to 1.5×IQR
- Median line inside box
- Outliers shown beyond whiskers

### Statistical Analysis
- Non-parametric tests
- Robust confidence intervals
- Distribution comparison
- Effect size measures
- Quality assessment

### Data Exploration
- Understanding typical spread
- Comparing group variability
- Assessing data quality
- Identifying unusual patterns
- Generating hypotheses

## IQR in Different Contexts

### Normal Distribution
- IQR ≈ 1.35 × SD
- Predictable relationship
- Used for normality assessment
- Conversion possible
- Quality check

### Skewed Distributions
- More reliable than SD
- Better represents typical spread
- Less affected by tail
- Preferred measure
- Robust alternative

### Small Samples
- Less stable than with large samples
- Still more robust than range
- Consider sample size
- May have wide confidence intervals
- Use with caution

## Practical Considerations

### Calculation
- Requires quartile calculation
- Method choice affects result
- Different software may differ
- Consistency important
- Document method

### Interpretation
- Consider distribution shape
- Compare with other measures
- Look at sample size
- Understand context
- Relate to business meaning

### Communication
- Explain it's middle 50%
- Provide context
- Compare to benchmarks
- Use visualizations
- Note robustness advantage

## Common Mistakes

### Calculation Errors
- Wrong quartile method
- Subtraction errors
- Using wrong quartiles
- Method inconsistency
- Not documenting method

### Interpretation Errors
- Assuming IQR = full range
- Ignoring distribution shape
- Overstating precision
- Not considering sample size
- Missing context

### Application Errors
- Wrong outlier detection multiplier
- Inappropriate for very small samples
- Using when full spread needed
- Inconsistent with other measures
- Miscommunication

## Best Practices

### Analysis
- Calculate multiple variability measures
- Compare IQR with SD and range
- Examine distribution shape
- Identify outliers appropriately
- Document methodology

### Reporting
- Specify quartile calculation method
- Provide context for interpretation
- Compare with other measures
- Note sample size
- Discuss practical significance

### Decision Making
- Use IQR for robust assessments
- Consider when outliers matter
- Look at full distribution
- Understand business context
- Evaluate actionability

## Advanced Topics

### IQR-Based Statistics
- Quartile coefficient of dispersion
- Robust coefficient of variation
- Quartile-based skewness measures
- Non-parametric effect sizes
- Advanced robust statistics

### IQR in Time Series
- Rolling IQR calculations
- Volatility monitoring
- Change point detection
- Process monitoring
- Quality control applications

### IQR Confidence Intervals
- Bootstrap methods
- Order statistics
- Distribution-free intervals
- Sample size considerations
- Statistical inference