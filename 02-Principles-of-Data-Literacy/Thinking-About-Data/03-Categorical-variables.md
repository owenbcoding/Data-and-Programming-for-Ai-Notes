# Categorical Variables

## Understanding Categorical Variables
Categorical variables represent qualitative data that can be divided into groups or categories. They describe qualities or characteristics rather than quantities.

## Types of Categorical Variables

### Nominal Variables
Categories with no inherent order or ranking.

#### Characteristics
- No natural ordering
- Categories are mutually exclusive
- Equality/inequality only meaningful operation
- Often represented by labels

#### Examples
- Gender (male, female, non-binary)
- Race/ethnicity
- Country of residence
- Color preferences
- Product types

#### Analysis Methods
- Frequency counts
- Mode (most common category)
- Proportions and percentages
- Chi-square tests
- Association measures

### Ordinal Variables
Categories with a meaningful order but unknown intervals between categories.

#### Characteristics
- Clear ordering of categories
- Distance between categories not uniform
- Ranking is meaningful
- Limited arithmetic operations

#### Examples
- Education level (high school, bachelor's, master's, PhD)
- Satisfaction ratings (very dissatisfied to very satisfied)
- Income brackets (low, medium, high)
- Likert scales (strongly disagree to strongly agree)
- Performance ratings (poor, fair, good, excellent)

#### Analysis Methods
- Median and percentiles
- Non-parametric tests
- Spearman correlation
- Cumulative proportions
- Rank-based statistics

## Working with Categorical Data

### Data Exploration
- Frequency tables
- Mode identification
- Category distribution
- Missing category analysis
- Rare category examination

### Data Cleaning
- Standardize category labels
- Handle missing categories
- Combine rare categories
- Correct spelling variations
- Resolve inconsistent coding

### Category Management
- **Combining categories**: Merge similar groups
- **Splitting categories**: Divide broad groups
- **Other category**: Group rare responses
- **Hierarchical coding**: Multi-level classification
- **Consolidation**: Reduce number of categories

## Encoding Categorical Variables

### One-Hot Encoding
- Create binary columns for each category
- Preserves all information
- Increases dimensionality
- Suitable for nominal variables
- Common in machine learning

### Label Encoding
- Assign numeric values to categories
- Creates artificial ordering
- Reduces dimensionality
- Problematic for nominal variables
- Can be appropriate for ordinal

### Ordinal Encoding
- Assign numbers respecting order
- Maintains ordinal relationships
- Appropriate for ordinal variables
- Requires domain knowledge
- Preserves some information

### Target Encoding
- Use target variable for encoding
- Can capture relationships
- Risk of overfitting
- Requires careful validation
- Advanced technique

## Statistical Analysis

### Descriptive Statistics
- Frequency counts
- Proportions and percentages
- Mode
- Diversity indices
- Category distribution

### Inferential Statistics
- Chi-square test of independence
- Fisher's exact test
- McNemar's test
- Cochran's Q test
- Logistic regression

### Association Measures
- Cramer's V
- Phi coefficient
- Contingency coefficient
- Lambda
- Uncertainty coefficient

## Visualization Techniques

### Single Variable
- Bar charts
- Pie charts (limited use)
- Pareto charts
- Word clouds (for text categories)
- Tree maps

### Multiple Variables
- Stacked bar charts
- Grouped bar charts
- Mosaic plots
- Heat maps
- Sankey diagrams

### Comparison
- Side-by-side bar charts
- Relative frequency plots
- Proportion plots
- Diverging bar charts
- Likert scale plots

## Common Issues

### Too Many Categories
- Difficult to analyze and visualize
- Sparse data in many categories
- Reduced statistical power
- Need for consolidation
- Consider hierarchical grouping

### Rare Categories
- Limited observations
- Unstable estimates
- May need combination
- Consider "other" category
- Document consolidation decisions

### Inconsistent Coding
- Spelling variations
- Different case usage
- Abbreviations vs. full names
- Need for standardization
- Establish coding guidelines

### Missing Categories
- Unknown values
- Refused to answer
- Not applicable responses
- Need distinct handling
- Document missingness patterns

## Best Practices

### Data Collection
- Use clear, mutually exclusive categories
- Limit number of categories when possible
- Provide "other" option
- Consider ordinal vs. nominal carefully
- Test category clarity

### Data Preparation
- Document category definitions
- Create data dictionaries
- Standardize coding schemes
- Handle missing values explicitly
- Maintain category hierarchies

### Analysis Planning
- Choose appropriate statistical tests
- Consider sample size per category
- Plan for multiple comparisons
- Use visualization wisely
- Interpret results cautiously

### Communication
- Explain category definitions
- Provide context for groupings
- Show full distributions
- Acknowledge consolidation decisions
- Use clear, accessible language

## Applications

### Market Research
- Customer segments
- Product categories
- Brand preferences
- Purchase behaviors
- Demographic groups

### Healthcare
- Disease classifications
- Treatment types
- Risk categories
- Symptom presence/absence
- Patient groups

### Social Sciences
- Demographic categories
- Attitude scales
- Behavioral types
- Social classes
- Geographic regions

### Quality Control
- Defect types
- Quality grades
- Failure categories
- Inspection results
- Process states