# Median

## What is the Median?
The median is the middle value in an ordered dataset. It represents the 50th percentile, meaning half the values are above and half are below it.

## Calculating the Median

### For Odd Number of Values
- Sort values in ascending order
- Select the middle value
- Position: (n + 1) / 2
- Example: [1, 3, 5, 7, 9] → median = 5

### For Even Number of Values
- Sort values in ascending order
- Average the two middle values
- Position: average of n/2 and (n/2 + 1)
- Example: [1, 3, 5, 7, 9, 11] → median = (5 + 7) / 2 = 6

## Properties of the Median

### Robustness
- Not affected by extreme values
- Resistant to outliers
- Stable measure of center
- Less sensitive to skewness
- More reliable for skewed data

### Mathematical Properties
- Minimizes absolute deviations
- 50th percentile of distribution
- Not necessarily unique (even n)
- Can be calculated for ordinal data
- Always within data range

## When to Use the Median

### Appropriate Situations
- Skewed distributions
- Data with outliers
- Ordinal data
- When robustness needed
- Income and financial data

### Inappropriate Situations
- When mathematical properties needed
- For further statistical calculations
- Categorical nominal data
- When distribution symmetric
- Small samples with limited information

## Median vs. Mean

### Comparison
- **Mean**: Balance point, sensitive to outliers
- **Median**: Middle value, robust to outliers
- **Symmetric data**: Mean ≈ Median
- **Right-skewed**: Mean > Median
- **Left-skewed**: Mean < Median

### Decision Framework
- Check distribution shape
- Look for outliers
- Consider data type
- Think about robustness needs
- Evaluate application requirements

## Types of Medians

### Simple Median
- Single middle value
- Most common type
- Used for univariate data
- Straightforward interpretation
- Standard measure

### Weighted Median
- Accounts for frequency/weight
- Different from weighted mean
- Used in survey research
- Consider data importance
- More complex calculation

### Grouped Data Median
- Estimated from grouped frequencies
- Approximation when raw data unavailable
- Uses interpolation within median class
- Less precise than raw data median
- Common in reported statistics

### Spatial Median
- Multivariate extension
- Minimizes Euclidean distances
- Used in spatial statistics
- More complex computation
- Robust multivariate center

## Applications

### Income and Wealth Data
- Highly right-skewed distributions
- Extreme outliers (billionaires)
- Median more representative
- Standard economic measure
- Policy and planning use

### Real Estate
- Property prices often skewed
- Median home price reported
- Less affected by luxury properties
- Market indicator
- Buyer/seller reference

### Education
- Test score distributions
- Class performance assessment
- Grade reporting
- Educational research
- Performance monitoring

### Healthcare
- Patient recovery times
- Treatment effectiveness
- Survival analysis
- Cost distributions
- Quality metrics

## Statistical Applications

### Non-Parametric Tests
- Mann-Whitney U test
- Wilcoxon signed-rank test
- Kruskal-Wallis test
- Median-based comparisons
- Distribution-free methods

### Robust Statistics
- Median absolute deviation (MAD)
- Robust regression methods
- Outlier detection
- Quality control
- Anomaly detection

### Exploratory Analysis
- Five-number summary
- Box plots center line
- Distribution comparison
- Skewness assessment
- Data cleaning

## Practical Considerations

### Calculation
- Requires sorting data
- Computationally intensive for large datasets
- Can be approximated for streaming data
- Memory considerations
- Algorithm choice matters

### Interpretation
- Always consider context
- Compare with mean
- Examine distribution shape
- Note sample size
- Understand limitations

### Communication
- Explain why median chosen
- Provide context
- Compare to other measures
- Visualize distribution
- Discuss practical significance

## Common Mistakes

### Inappropriate Use
- Using for nominal categorical data
- When mean properties needed
- Without examining distribution
- As sole summary statistic
- For further calculations requiring mean

### Misinterpretation
- Assuming median = typical
- Ignoring distribution shape
- Overstating precision
- Not considering sample size
- Missing context

### Calculation Errors
- Not sorting data first
- Wrong position calculation
- Including non-numerical data
- Mishandling even vs. odd
- Weighting errors

## Best Practices

### Analysis
- Always examine distribution first
- Calculate both mean and median
- Compare measures
- Consider appropriate measure for context
- Report uncertainty when appropriate

### Reporting
- Specify which measure used
- Provide measure of spread
- Note sample size
- Discuss any data limitations
- Contextualize findings

### Decision Making
- Consider if median is appropriate
- Look at full distribution
- Understand outliers' impact
- Use multiple metrics
- Consider practical significance

## Advanced Topics

### Median of Medians
- Algorithm for robust median finding
- Linear time complexity
- Used in computer science
- Selection algorithm
- Divide and conquer approach

### Median in Multivariate Data
- Spatial median
- Multivariate outlier detection
- Robust clustering
- Dimension reduction
- Multivariate quality control