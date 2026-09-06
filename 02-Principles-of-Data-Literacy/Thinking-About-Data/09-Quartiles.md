# Quartiles

## What are Quartiles?
Quartiles divide a ranked dataset into four equal parts. Each quartile represents 25% of the data, providing insights into the distribution's spread and central tendency.

## Types of Quartiles

### First Quartile (Q1)
- 25th percentile
- 25% of data below this value
- Lower quartile
- End of first quarter
- Formula depends on method

### Second Quartile (Q2)
- 50th percentile
- 50% of data below this value
- Same as median
- Middle quartile
- Divides data in half

### Third Quartile (Q3)
- 75th percentile
- 75% of data below this value
- Upper quartile
- End of third quarter
- Starting point for top 25%

### Fourth Quartile (Q4)
- Technically the maximum value
- Top 25% of data
- Upper extreme
- Not always explicitly calculated
- Sometimes refers to data above Q3

## Calculating Quartiles

### Methods of Calculation
Different methods exist for calculating quartile positions:

#### Method 1 (Inclusive)
- Position = (n + 1) × p
- Linear interpolation if needed
- Used in some statistical software
- Slightly different results
- Method choice matters

#### Method 2 (Exclusive)
- Position = n × p
- Different interpolation
- Common in some contexts
- Results vary slightly
- Consistency important

#### Method 3 (Tukey's Hinges)
- Split data at median
- Find medians of halves
- Used in box plots
- Robust method
- Simple calculation

### Example Calculation
```python
import numpy as np
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Q1 = np.percentile(data, 25)  # 6.0
Q2 = np.percentile(data, 50)  # 10.0 (median)
Q3 = np.percentile(data, 75)  # 14.0
```

## Interquartile Range (IQR)

### Definition
- IQR = Q3 - Q1
- Middle 50% of data
- Robust measure of spread
- Not affected by outliers
- Key variability metric

### Applications
- Outlier detection
- Box plot construction
- Robust statistics
- Non-parametric tests
- Data quality assessment

### Outlier Detection Rule
- Lower fence: Q1 - 1.5 × IQR
- Upper fence: Q3 + 1.5 × IQR
- Values outside fences are potential outliers
- Common rule (Tukey's rule)
- Adjust multiplier for sensitivity

## Applications

### Box Plots
- Q1: bottom of box
- Q2 (median): line in box
- Q3: top of box
- IQR: height of box
- Whiskers extend to fences

### Data Exploration
- Understanding distribution shape
- Identifying skewness
- Detecting outliers
- Comparing groups
- Quality assessment

### Statistical Analysis
- Non-parametric tests
- Robust estimators
- Confidence intervals
- Hypothesis testing
- Effect size measures

### Quality Control
- Process variation assessment
- Capability analysis
- Control chart limits
- Specification limits
- Process monitoring

## Quartiles vs. Other Measures

### Comparison with Mean and Standard Deviation
- Quartiles: robust, non-parametric
- Mean/SD: sensitive to outliers
- Quartiles: work with ordinal data
- Mean/SD: require interval data
- Quartiles: describe distribution shape

### Comparison with Percentiles
- Quartiles: specific percentiles (25, 50, 75)
- Percentiles: any percentage
- Quartiles: standard summary
- Percentiles: flexible, detailed
- Quartiles: common communication tool

### Decision Framework
- Consider data type
- Evaluate outlier presence
- Think about robustness needs
- Consider audience
- Match to analysis goals

## Practical Considerations

### Sample Size
- Small samples: quartiles less stable
- Large samples: more reliable
- Minimum sample size considerations
- Confidence intervals for quartiles
- Sampling variability

### Calculation Method
- Choose method and be consistent
- Document method used
- Different software may differ
- Results can vary slightly
- Method affects interpretation

### Interpretation
- Consider distribution shape
- Look at spacing between quartiles
- Compare with central tendency
- Examine sample size
- Contextualize findings

## Common Mistakes

### Calculation Errors
- Wrong method for position
- Incorrect interpolation
- Sorting errors
- Including invalid data
- Mishandling ties

### Interpretation Mistakes
- Assuming equal spacing
- Ignoring distribution shape
- Overstating precision
- Not considering sample size
- Missing context

### Application Errors
- Using quartiles inappropriately
- Wrong outlier detection rule
- Inconsistent methods
- Ignoring method differences
- Miscommunication

## Best Practices

### Analysis
- Always examine full distribution
- Use multiple variability measures
- Check calculation method
- Consider sample size
- Document methodology

### Reporting
- Specify calculation method
- Provide context for interpretation
- Compare with other measures
- Note any data limitations
- Discuss practical significance

### Communication
- Explain quartiles clearly
- Use visualizations (box plots)
- Provide business context
- Note method if non-standard
- Consider audience understanding

## Advanced Topics

### Percentiles Beyond Quartiles
- Deciles (10 percentiles)
- Percentiles (1 percent increments)
- Custom percentiles
- Tail percentiles
- Distribution-specific percentiles

### Quartiles in Multivariate Data
- Multivariate quartiles
- Depth-based quartiles
- Spatial quartiles
- Robust multivariate analysis
- Advanced applications

### Quartile Confidence Intervals
- Bootstrap methods
- Order statistics
- Distribution-free intervals
- Sample size considerations
- Statistical inference