# Standard Deviation

## What is Standard Deviation?
Standard deviation measures the average amount of variation or dispersion of a set of values. It indicates how spread out the values are from the mean.

## Calculating Standard Deviation

### Population Standard Deviation
- σ = √(Σ(x - μ)² / N)
- μ = population mean
- N = population size
- Uses all population data
- Theoretical parameter

### Sample Standard Deviation
- s = √(Σ(x - x̄)² / (n - 1))
- x̄ = sample mean
- n = sample size
- Uses n-1 (Bessel's correction)
- Estimates population parameter

### Example Calculation
```python
import numpy as np
data = [2, 4, 4, 4, 5, 5, 7, 9]
mean = np.mean(data)  # 5.0
std_dev = np.std(data, ddof=1)  # 2.138 (sample)
```

## Properties of Standard Deviation

### Mathematical Properties
- Always non-negative
- Zero only if all values identical
- Same units as original data
- Scale-dependent
- Additive under certain conditions

### Interpretation
- Average distance from mean
- Typical deviation
- Measure of spread
- Precision indicator
- Quality metric

### Distribution Relationship
- Normal distribution: 68-95-99.7 rule
- 68% within 1 SD of mean
- 95% within 2 SD of mean
- 99.7% within 3 SD of mean
- Empirical rule application

## When to Use Standard Deviation

### Appropriate Situations
- Normally distributed data
- When mathematical properties needed
- For parametric statistical tests
- When mean is appropriate center
- For further statistical calculations

### Inappropriate Situations
- Highly skewed data
- With extreme outliers
- For ordinal data
- Small samples with limited information
- When robustness needed

## Standard Deviation vs. Other Measures

### Comparison with Variance
- SD: same units as data
- Variance: squared units
- SD: interpretable
- Variance: mathematically convenient
- SD = √variance

### Comparison with IQR
- SD: uses all data, sensitive
- IQR: robust, non-parametric
- SD: requires interval data
- IQR: works with ordinal data
- SD: affected by outliers

### Comparison with Range
- SD: uses all information
- Range: only extremes
- SD: more stable
- Range: simpler
- SD: more informative

## Applications

### Quality Control
- Process capability (Cp, Cpk)
- Control chart limits
- Six sigma methodology
- Process monitoring
- Specification compliance

### Statistical Analysis
- Hypothesis testing
- Confidence intervals
- Effect sizes
- Regression analysis
- ANOVA

### Risk Assessment
- Financial risk (volatility)
- Investment analysis
- Insurance pricing
- Project risk
- Decision analysis

### Research
- Experimental error
- Measurement precision
- Reproducibility assessment
- Sample size calculation
- Power analysis

## Standard Deviation in Different Distributions

### Normal Distribution
- Well-defined relationship
- Empirical rule applies
- Predictable percentages
- Standard normal conversion
- Foundation of many tests

### Skewed Distributions
- Less meaningful
- May misrepresent spread
- Consider alternatives
- Use with caution
- Examine distribution shape

### Small Samples
- Less reliable estimate
- High sampling variability
- Consider sample size
- Use t-distribution
- Report uncertainty

## Practical Considerations

### Calculation
- Requires mean calculation
- Computationally intensive for large datasets
- Numerical precision considerations
- Two-pass or one-pass algorithms
- Software implementation differences

### Interpretation
- Always consider distribution shape
- Compare with mean (coefficient of variation)
- Look at sample size
- Examine outliers
- Contextualize findings

### Communication
- Explain it's average deviation
- Provide context
- Compare to benchmarks
- Use visualizations
- Note limitations

## Common Mistakes

### Calculation Errors
- Wrong formula (population vs. sample)
- Not using Bessel's correction
- Numerical precision issues
- Including invalid data
- Division by n instead of n-1

### Interpretation Errors
- Assuming normal distribution
- Ignoring outliers
- Overstating precision
- Not considering sample size
- Missing context

### Application Errors
- Using with inappropriate data
- Comparing across different units
- Ignoring distribution shape
- Wrong standard error usage
- Miscommunication

## Best Practices

### Analysis
- Always examine distribution first
- Calculate multiple variability measures
- Check for outliers
- Consider appropriate measure for context
- Report uncertainty

### Reporting
- Specify sample vs. population
- Provide measure of center
- Note sample size
- Discuss distribution shape
- Contextualize findings

### Decision Making
- Consider if SD is appropriate
- Look at full distribution
- Understand business context
- Use multiple metrics
- Evaluate actionability

## Advanced Topics

### Coefficient of Variation
- CV = (SD / mean) × 100%
- Relative variability measure
- Unitless comparison
- Useful for comparing across scales
- Common in laboratory work

### Standard Error
- SE = SD / √n
- Precision of sample mean
- Used in confidence intervals
- Decreases with sample size
- Different from SD

### Pooled Standard Deviation
- Combines variability across groups
- Used in t-tests and ANOVA
- Weighted by sample sizes
- Assumes equal variances
- Statistical inference