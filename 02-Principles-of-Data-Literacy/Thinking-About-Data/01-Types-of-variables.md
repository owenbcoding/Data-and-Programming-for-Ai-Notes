# Types of Variables

## What are Variables?
In data analysis, a variable is any characteristic, number, or quantity that can be measured or counted. Understanding variable types is fundamental because it determines appropriate analysis methods and visualization techniques.

## Main Variable Types

### Categorical Variables (Qualitative)
Variables that represent categories or groups.

#### Nominal Variables
- Categories with no inherent order
- Examples: Gender, race, color, country
- Operations: Equality/inequality only
- Analysis: Frequency counts, mode

#### Ordinal Variables
- Categories with meaningful order
- Examples: Education level, satisfaction ratings, income brackets
- Operations: Comparisons possible
- Analysis: Median, percentiles

### Numerical Variables (Quantitative)
Variables that represent measurable quantities.

#### Discrete Variables
- Countable values, often integers
- Examples: Number of children, items sold, test scores
- Gaps between possible values
- Analysis: Counts, proportions

#### Continuous Variables
- Any value within a range
- Examples: Height, weight, temperature, time
- Infinite possible values
- Analysis: Mean, standard deviation

## Variable Identification

### Context Matters
- Age can be categorical (age groups) or numerical (years)
- Income can be continuous (exact amount) or ordinal (brackets)
- Ratings can be numerical (1-5) or categorical (poor to excellent)
- Time can be continuous (seconds) or categorical (morning/afternoon)

### Research Questions Guide Classification
- "How many?" → Discrete numerical
- "How much?" → Continuous numerical
- "What type?" → Categorical
- "What level?" → Ordinal

## Variable Types in Analysis

### Statistical Operations
- **Categorical**: Mode, frequency, proportions
- **Ordinal**: Median, percentiles, non-parametric tests
- **Numerical**: Mean, standard deviation, correlation

### Visualization Choices
- **Categorical**: Bar charts, pie charts
- **Ordinal**: Bar charts with ordered categories
- **Numerical**: Histograms, scatter plots, line charts

### Modeling Considerations
- **Categorical**: One-hot encoding, label encoding
- **Ordinal**: Ordinal encoding, careful treatment
- **Numerical**: Direct use, scaling, transformation

## Common Mistakes

### Treating Ordinal as Nominal
- Losing information about order
- Inappropriate statistical tests
- Reduced analytical power

### Treating Categorical as Numerical
- Meaningless calculations (mean of zip codes)
- Incorrect statistical assumptions
- Misleading visualizations

### Ignoring Variable Type
- Choosing wrong analysis methods
- Inappropriate visualizations
- Invalid statistical conclusions

## Best Practices

### Variable Documentation
- Always document variable types
- Explain coding schemes
- Note any transformations
- Describe measurement units
- Provide example values

### Type Checking
- Verify data types match expectations
- Check for unexpected values
- Validate ranges and categories
- Test for type consistency
- Document any issues

### Analysis Planning
- Consider variable types before analysis
- Choose appropriate methods
- Plan visualizations accordingly
- Validate type assumptions
- Document type decisions

## Variable Type Transformations

### Continuous to Categorical
- Binning or discretization
- Creating age groups
- Converting to quartiles
- Useful for certain analyses

### Categorical to Numerical
- One-hot encoding
- Label encoding
- Ordinal encoding
- Required for many ML algorithms

### Numerical to Ordinal
- Creating rankings
- Converting to brackets
- Percentile-based grouping
- Simplifies complex relationships

## Advanced Considerations

### Mixed Types
- Variables that can be interpreted multiple ways
- Context-dependent classification
- Hierarchical variable structures
- Time-dependent types
- Multi-label categorical variables

### Special Cases
- Dates and times (temporal variables)
- Geographic data (spatial variables)
- Text data (unstructured variables)
- Image data (high-dimensional variables)
- Network data (relational variables)