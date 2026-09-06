# Correlation Coefficients

## Understanding Correlation Coefficients
Correlation coefficients are numerical measures that quantify the strength and direction of relationships between variables. Different types exist for different situations.

## Pearson Correlation Coefficient (r)

### Definition and Formula
- Measures linear relationship strength
- r = covariance(X,Y) / (σX × σY)
- Range: -1 to +1
- Requires interval/ratio data
- Most commonly used

### Interpretation Scale
- **1.0**: Perfect positive linear relationship
- **0.7 to 0.9**: Strong positive relationship
- **0.4 to 0.6**: Moderate positive relationship
- **0.1 to 0.3**: Weak positive relationship
- **0.0**: No linear relationship
- **-0.1 to -0.3**: Weak negative relationship
- **-0.4 to -0.6**: Moderate negative relationship
- **-0.7 to -0.9**: Strong negative relationship
- **-1.0**: Perfect negative linear relationship

### Assumptions
- Linear relationship
- Both variables continuous
- Normally distributed (approximately)
- Homoscedasticity (constant variance)
- No extreme outliers

### When to Use
- Both variables numerical
- Linear relationship expected
- Data approximately normal
- Outliers not problematic
- Standard parametric analysis

## Spearman Rank Correlation (ρ)

### Definition and Formula
- Non-parametric measure
- Based on ranked data
- Pearson correlation on ranks
- Range: -1 to +1
- Measures monotonic relationships

### Calculation Process
1. Rank each variable separately
2. Calculate Pearson correlation on ranks
3. Interpret same as Pearson
4. Handles ties appropriately
5. Robust to outliers

### When to Use
- Ordinal data
- Non-normal distributions
- Outliers present
- Monotonic (not necessarily linear) relationships
- Small sample sizes

### Advantages
- Robust to outliers
- Works with ordinal data
- No distributional assumptions
- Captures monotonic relationships
- More flexible than Pearson

## Kendall's Tau (τ)

### Definition and Formula
- Another non-parametric measure
- Based on concordant/discordant pairs
- Range: -1 to +1
- Different calculation approach
- Often preferred for small samples

### Calculation Process
1. Compare all pairs of observations
2. Count concordant pairs (same order)
3. Count discordant pairs (different order)
4. τ = (C - D) / (n(n-1)/2)
5. Handles ties with adjustments

### When to Use
- Small sample sizes
- Many tied ranks
- Ordinal data
- When robustness needed
- Alternative to Spearman

### Advantages
- Better for small samples
- Handles ties well
- More interpretable for some
- Robust to outliers
- Distribution-free

## Point-Biserial Correlation

### Definition
- Special case of Pearson correlation
- One dichotomous (binary) variable
- One continuous variable
- Same calculation as Pearson
- Interpreted similarly

### When to Use
- Comparing two groups on continuous measure
- Binary vs. continuous variable relationship
- Gender vs. test scores
- Treatment vs. control group outcomes
- Yes/no vs. measurement

### Interpretation
- Same as Pearson correlation
- Magnitude indicates strength
- Sign indicates direction
- Can be tested for significance
- Effect size measure

## Phi Coefficient (φ)

### Definition
- Correlation for two binary variables
- Special case of Pearson
- Range: -1 to +1
- 2×2 contingency table data
- Measures association

### When to Use
- Both variables dichotomous
- Yes/no type questions
- Presence/absence data
- Binary outcomes
- Categorical association

### Calculation
- From 2×2 contingency table
- φ = (ad - bc) / √((a+b)(c+d)(a+c)(b+d))
- Related to chi-square statistic
- φ² = χ²/n
- Same interpretation as Pearson

## Cramer's V

### Definition
- Extension of phi coefficient
- For larger than 2×2 tables
- Range: 0 to 1 (no negative)
- Measures association strength
- Normalized measure

### When to Use
- Categorical variables with >2 categories
- Larger contingency tables
- Nominal data association
- Effect size for chi-square
- Multi-category relationships

### Calculation
- V = √(χ²/(n×min(r-1,c-1)))
- r = number of rows
- c = number of columns
- n = total sample size
- Interpretation guidelines vary

## Choosing the Right Coefficient

### Decision Framework
1. **Data types**: What kind of variables?
2. **Relationship type**: Linear or monotonic?
3. **Distribution**: Normal or non-normal?
4. **Sample size**: Large or small?
5. **Outliers**: Present or absent?

### Quick Guide
- **Two continuous, linear, normal**: Pearson
- **Two continuous, monotonic, non-normal**: Spearman
- **Two continuous, small sample**: Kendall's Tau
- **Binary + continuous**: Point-biserial
- **Two binary**: Phi coefficient
- **Two categorical (>2 levels)**: Cramer's V

## Common Mistakes

### Wrong Coefficient Choice
- Using Pearson for ordinal data
- Not checking assumptions
- Ignoring data types
- Inappropriate for relationship type
- Poor statistical practice

### Over-Interpretation
- Reading too much into small correlations
- Ignoring confidence intervals
- Not considering sample size
- Overstating practical significance
- Poor communication

### Assumption Violations
- Not checking linearity
- Ignoring outliers
- Assuming normality
- Not examining distribution
- Invalid results

## Best Practices

### Selection
- Match coefficient to data types
- Check assumptions
- Consider relationship type
- Examine distributions
- Visualize first

### Calculation
- Use appropriate software
- Verify calculations
- Handle ties correctly
- Check for errors
- Document method

### Interpretation
- Consider strength, direction, significance
- Look at confidence intervals
- Examine practical significance
- Provide context
- Visualize relationship

### Reporting
- Specify coefficient type
- Report value and significance
- Provide confidence intervals
- Note sample size
- Include visualization

## Advanced Topics

### Partial Correlation
- Controls for other variables
- Understanding direct effects
- Multiple variable contexts
- Network analysis
- Causal inference

### Semi-Partial Correlation
- Unique contribution of variable
- Hierarchical regression
- Variable importance
- Model building
- Incremental validity

### Correlation Confidence Intervals
- Uncertainty quantification
- Fisher's z transformation
- Bootstrap methods
- Statistical inference
- Comparison testing