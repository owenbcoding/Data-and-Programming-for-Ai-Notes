# Numerical Variables

## Understanding Numerical Variables
Numerical variables represent quantities that can be measured and expressed as numbers. They are fundamental to statistical analysis and form the basis for many data science techniques.

## Types of Numerical Variables

### Discrete Numerical Variables
Variables that can only take specific, countable values.

#### Characteristics
- Countable values
- Often whole numbers
- Gaps between possible values
- Result from counting

#### Examples
- Number of children in a family
- Items sold per day
- Test scores (integer)
- Website visitors
- Defects in manufacturing

#### Analysis Approaches
- Frequency counts
- Poisson distribution
- Binomial distribution
- Count data models

### Continuous Numerical Variables
Variables that can take any value within a range.

#### Characteristics
- Infinite possible values
- Measured rather than counted
- Can be divided infinitely
- Result from measurement

#### Examples
- Height and weight
- Temperature
- Time duration
- Financial amounts
- Chemical concentrations

#### Analysis Approaches
- Normal distribution
- Continuous probability distributions
- Regression analysis
- Correlation analysis

## Properties of Numerical Variables

### Central Tendency
- **Mean**: Average value
- **Median**: Middle value
- **Mode**: Most frequent value
- Appropriate measures depend on distribution

### Variability
- **Range**: Difference between max and min
- **Variance**: Average squared deviation
- **Standard deviation**: Square root of variance
- **Interquartile range**: Middle 50% spread

### Distribution Shape
- **Symmetric**: Balanced around center
- **Skewed**: Asymmetric distribution
- **Kurtosis**: Peakedness of distribution
- **Modality**: Number of peaks

## Working with Numerical Data

### Data Exploration
- Calculate summary statistics
- Create histograms
- Check for outliers
- Examine distribution shape
- Identify patterns

### Data Cleaning
- Handle missing values
- Remove or investigate outliers
- Correct impossible values
- Standardize units
- Validate ranges

### Data Transformation
- **Log transformation**: For skewed data
- **Standardization**: Z-scores
- **Normalization**: Scale to 0-1
- **Binning**: Convert to categories
- **Aggregation**: Summarize by groups

## Common Issues

### Outliers
- Extreme values that differ significantly
- Can be legitimate or errors
- Impact statistical measures
- Require investigation
- May need special handling

### Skewed Distributions
- Not symmetric around mean
- Mean may not be representative
- Median often better measure
- May need transformation
- Common in real-world data

### Missing Values
- Gaps in numerical data
- Can bias analysis
- Various imputation methods
- Need careful handling
- Document approach taken

### Measurement Error
- Inaccuracy in measurement
- Systematic vs. random error
- Can affect conclusions
- Consider precision
- Validate measurements

## Statistical Operations

### Descriptive Statistics
- Mean, median, mode
- Standard deviation, variance
- Percentiles and quartiles
- Range and IQR
- Skewness and kurtosis

### Inferential Statistics
- Hypothesis testing
- Confidence intervals
- Regression analysis
- ANOVA
- Correlation analysis

### Probability Distributions
- Normal distribution
- t-distribution
- Chi-square distribution
- F-distribution
- Specialized distributions

## Visualization Techniques

### Distribution Visualization
- Histograms
- Density plots
- Box plots
- Violin plots
- Q-Q plots

### Relationship Visualization
- Scatter plots
- Line charts
- Heat maps
- Correlation matrices
- Pair plots

### Comparison Visualization
- Bar charts for means
- Box plots for groups
- Error bars
- Forest plots
- Ridgeline plots

## Best Practices

### Data Quality
- Validate numerical ranges
- Check for impossible values
- Verify measurement units
- Test for consistency
- Document data sources

### Analysis Planning
- Choose appropriate statistical tests
- Consider distribution assumptions
- Plan for outliers
- Determine sample size needs
- Pre-register analysis when possible

### Communication
- Use appropriate precision
- Include uncertainty measures
- Choose clear visualizations
- Explain statistical concepts
- Contextualize numerical findings

## Applications

### Business Analytics
- Sales forecasting
- Customer metrics
- Financial analysis
- Performance tracking
- Risk assessment

### Scientific Research
- Experimental measurements
- Observational data
- Clinical trials
- Environmental monitoring
- Quality control

### Social Sciences
- Survey data analysis
- Demographic studies
- Economic indicators
- Educational assessment
- Public health research