# Distributions

## What is a Distribution?
A distribution describes how values of a variable are spread or arranged. It shows the frequency or probability of different values occurring in a dataset.

## Understanding Distributions

### Key Concepts
- **Shape**: How data is distributed (symmetric, skewed, etc.)
- **Center**: Typical or central value (mean, median)
- **Spread**: How spread out values are (range, variance)
- **Tails**: Extreme values in distribution
- **Modality**: Number of peaks

### Distribution Types

#### Symmetric Distributions
- Balanced around center
- Mean ≈ Median ≈ Mode
- Left and right tails similar
- Common in natural phenomena
- Example: Normal distribution

#### Skewed Distributions
- **Right-skewed (positive)**: Long right tail
- **Left-skewed (negative)**: Long left tail
- Mean pulled toward tail
- Median better central measure
- Common in real-world data

#### Unimodal Distributions
- Single peak
- Most common pattern
- One dominant value range
- Easier to analyze
- Many natural examples

#### Bimodal/Multimodal Distributions
- Two or more peaks
- Suggests mixed populations
- May indicate subgroups
- Requires investigation
- Complex to analyze

## Common Probability Distributions

### Normal Distribution
- Bell-shaped curve
- Symmetric around mean
- Defined by mean and standard deviation
- 68-95-99.7 rule
- Foundation of many statistical methods

### Uniform Distribution
- All values equally likely
- Rectangular shape
- Constant probability
- Less common in nature
- Useful in simulations

### Binomial Distribution
- Count of successes in fixed trials
- Two possible outcomes
- Defined by n and p
- Discrete distribution
- Common in yes/no data

### Poisson Distribution
- Count of events in fixed interval
- Rare events
- Mean = variance
- Discrete distribution
- Count data modeling

### Exponential Distribution
- Time between events
- Memoryless property
- Continuous distribution
- Right-skewed
- Reliability analysis

## Describing Distributions

### Central Tendency
- **Mean**: Balance point of distribution
- **Median**: Middle value (50th percentile)
- **Mode**: Most frequent value
- Choice depends on distribution shape

### Variability
- **Range**: Max - min
- **Variance**: Average squared deviation
- **Standard deviation**: Typical deviation
- **IQR**: Middle 50% spread
- **Coefficient of variation**: Relative variability

### Shape Measures
- **Skewness**: Asymmetry of distribution
- **Kurtosis**: Peakedness vs. normal
- **Modality**: Number of peaks
- **Tail behavior**: Heavy vs. light tails

## Visualizing Distributions

### Histograms
- Bar chart of value frequencies
- Shows shape clearly
- Bin width matters
- Most common visualization
- Good for large datasets

### Density Plots
- Smooth curve estimate
- Shows shape elegantly
- Continuous representation
- Can show multiple distributions
- Modern alternative to histograms

### Box Plots
- Five-number summary
- Shows outliers clearly
- Compares groups easily
- Compact representation
- Good for skewed data

### Q-Q Plots
- Quantile-quantile comparison
- Tests distribution assumptions
- Compares to theoretical distribution
- Identifies deviations
- Statistical diagnostic tool

### Violin Plots
- Combines box plot and density
- Shows distribution shape
- Compares groups
- More informative than box plots
- Modern visualization

## Analyzing Distributions

### Normality Assessment
- Visual inspection (histograms, Q-Q plots)
- Statistical tests (Shapiro-Wilk, Kolmogorov-Smirnov)
- Skewness and kurtosis measures
- Consider sample size
- Impact on analysis choices

### Outlier Detection
- Values far from distribution center
- Using standard deviations (z-scores)
- Using IQR method
- Context-dependent definition
- Requires investigation

### Group Comparisons
- Compare distribution shapes
- Test for differences
- Consider variability
- Visual comparisons
- Statistical testing

## Distribution Transformations

### When to Transform
- Highly skewed data
- Non-normal distributions
- Heteroscedasticity
- Meeting statistical assumptions
- Improving model performance

### Common Transformations
- **Log transformation**: Right-skewed data
- **Square root**: Moderate right skew
- **Reciprocal**: Severe right skew
- **Box-Cox**: Family of transformations
- **Yeo-Johnson**: Handles negative values

### Interpretation Considerations
- Transformed scale different
- Back-transformation needed
- Interpretation becomes complex
- Choose transformations carefully
- Document transformation choices

## Real-World Applications

### Natural Phenomena
- Height, weight distributions
- Measurement errors
- Biological traits
- Environmental data
- Often approximately normal

### Business Data
- Sales often right-skewed
- Customer spending patterns
- Website traffic
- Financial returns
- Usually non-normal

### Social Data
- Income distributions (highly skewed)
- Test scores (often normal)
- Survey responses (various shapes)
- Demographic data
- Mixed distribution types

## Best Practices

### Exploration
- Always visualize distributions
- Calculate summary statistics
- Check for outliers
- Assess normality when needed
- Consider context

### Documentation
- Describe distribution characteristics
- Note any transformations
- Explain unusual patterns
- Document outlier decisions
- Provide context

### Analysis Choices
- Match methods to distribution
- Consider non-parametric alternatives
- Be cautious with small samples
- Validate assumptions
- Report limitations