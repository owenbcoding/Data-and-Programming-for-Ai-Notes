# Selecting the Correct Graph

## Choosing the Right Visualization
Selecting the appropriate graph type is crucial for effective data communication. The right choice depends on data type, analysis goals, and audience needs.

## Decision Framework

### Key Questions
1. **What type of data do you have?**
   - Numerical vs. categorical
   - Time series vs. cross-sectional
   - Single vs. multiple variables

2. **What is your goal?**
   - Comparison
   - Distribution
   - Relationship
   - Composition
   - Geographical

3. **Who is your audience?**
   - Technical vs. non-technical
   - Executive vs. operational
   - Internal vs. external
   - Size and diversity

## Visualization Types by Purpose

### Comparison Visualizations

#### Bar Charts
- **Use**: Comparing values across categories
- **Data**: Categorical + numerical
- **Variants**: Vertical, horizontal, grouped, stacked
- **Best for**: Few categories, clear comparisons
- **Avoid**: Too many categories, continuous data

#### Column Charts
- **Use**: Similar to bar charts, vertical orientation
- **Data**: Categorical + numerical
- **Best for**: Time-based categories, ranking
- **Avoid**: Long category labels

#### Line Charts
- **Use**: Showing trends over time
- **Data**: Time series numerical data
- **Best for**: Continuous time data, trends
- **Avoid**: Categorical data, few time points

#### Scatter Plots
- **Use**: Showing relationships between two numerical variables
- **Data**: Two numerical variables
- **Best for**: Correlation, patterns, outliers
- **Avoid**: Categorical data, dense data (consider alternatives)

### Distribution Visualizations

#### Histograms
- **Use**: Showing distribution of numerical data
- **Data**: Single numerical variable
- **Best for**: Understanding distribution shape, outliers
- **Avoid**: Small samples, categorical data

#### Box Plots
- **Use**: Showing distribution summary and outliers
- **Data**: Numerical data (often by category)
- **Best for**: Comparing distributions, outlier detection
- **Avoid**: Showing detailed distribution shape

#### Density Plots
- **Use**: Smooth distribution display
- **Data**: Single numerical variable
- **Best for**: Smooth distribution representation
- **Avoid**: Small samples, discrete data

#### Violin Plots
- **Use**: Combining box plot and density
- **Data**: Numerical data (often by category)
- **Best for**: Detailed distribution comparison
- **Avoid**: Very small samples

### Composition Visualizations

#### Pie Charts
- **Use**: Showing part-to-whole relationships
- **Data**: Categorical + numerical (percentages)
- **Best for**: Few categories, simple composition
- **Avoid**: Many categories, precise comparisons

#### Donut Charts
- **Use**: Similar to pie charts with center space
- **Data**: Categorical + numerical
- **Best for**: Modern aesthetic, space for summary
- **Avoid**: Same limitations as pie charts

#### Stacked Bar Charts
- **Use**: Showing composition across categories
- **Data**: Categorical + numerical (multiple series)
- **Best for**: Comparing totals and composition
- **Avoid**: Many categories, hard to compare middle segments

#### Treemaps
- **Use**: Hierarchical composition display
- **Data**: Hierarchical categorical + numerical
- **Best for**: Large hierarchies, space-efficient
- **Avoid**: Precise comparisons, small values

### Relationship Visualizations

#### Scatter Plots
- **Use**: Relationship between two numerical variables
- **Data**: Two numerical variables
- **Best for**: Correlation, patterns, clusters
- **Avoid**: Categorical data, very dense data

#### Bubble Charts
- **Use**: Three-variable relationship
- **Data**: Three numerical variables
- **Best for**: Adding dimension to scatter plot
- **Avoid**: Overlapping bubbles, hard to compare size

#### Heat Maps
- **Use**: Relationships in matrix format
- **Data**: Two categorical + numerical
- **Best for**: Patterns across categories, time series
- **Avoid**: Precise value reading, many categories

#### Correlation Matrices
- **Use**: Multiple variable correlations
- **Data**: Multiple numerical variables
- **Best for**: Overview of relationships
- **Avoid**: Causal interpretation, too many variables

### Geographical Visualizations

#### Choropleth Maps
- **Use**: Data by geographic regions
- **Data**: Geographic + numerical
- **Best for**: Regional patterns, comparisons
- **Avoid**: Precise values, misleading with varying region sizes

#### Dot Maps
- **Use**: Individual data points on map
- **Data Geographic + numerical/categorical
- **Best for**: Distribution patterns, density
- **Avoid**: Overcrowding, precise counting

#### Flow Maps
- **Use**: Movement between locations
- **Data**: Origin, destination, magnitude
- **Best for**: Migration, trade, movement
- **Avoid**: Complex overlapping flows

## Data Type Decision Tree

### Single Numerical Variable
- Distribution → Histogram, density plot, box plot
- Central tendency → Reference line, mean/median marker
- Over time → Line chart, time series plot

### Single Categorical Variable
- Frequency → Bar chart, pie chart (few categories)
- Proportion → Pie chart, donut chart (few categories)
- Ranking → Bar chart (ordered)

### Two Numerical Variables
- Relationship → Scatter plot
- Comparison → Grouped box plot, small multiples
- Time series → Line chart (if one variable is time)

### Two Categorical Variables
- Relationship → Stacked bar chart, heat map
- Comparison → Grouped bar chart
- Composition → Stacked bar chart

### Categorical + Numerical
- Comparison → Bar chart, box plot
- Distribution → Box plot, violin plot
- Composition → Stacked bar chart

### Time Series
- Trend → Line chart
- Comparison → Multiple line charts, small multiples
- Seasonality → Seasonal decomposition plot
- Distribution → Seasonal box plots

## Common Mistakes

### Wrong Chart Type
- Using pie charts for comparison
- Line charts for categorical data
- Scatter plots for categorical data
- **Solution**: Match chart to data type and purpose

### Too Complex
- Trying to show too much
- Overly complicated designs
- Too many categories
- **Solution**: Simplify, use multiple charts

### Misleading Scales
- Truncated axes
- Inconsistent scales
- Non-zero baselines for bar charts
- **Solution**: Use appropriate scales, be transparent

### Poor Design
- Cluttered layouts
- Ineffective color use
- Poor labeling
- **Solution**: Apply design principles, simplify

## Best Practices

### Start Simple
- Begin with basic chart type
- Add complexity only if needed
- Test with audience
- Iterate based on feedback

### Know Your Data
- Understand data types
- Check data quality
- Consider sample size
- Identify patterns

### Know Your Audience
- Match complexity to audience
- Use familiar chart types
- Provide context
- Allow exploration

### Test and Iterate
- Get feedback
- Test understanding
- Refine based on results
- Document decisions

## Alternative Approaches

### Small Multiples
- Multiple similar charts
- Easy comparison
- Reduced complexity per chart
- Pattern recognition across charts

### Interactive Visualizations
- User-driven exploration
- Drill-down capability
- Filtering and selection
- Dynamic complexity

### Hybrid Approaches
- Combination of chart types
- Multiple views of same data
- Linked visualizations
- Comprehensive overviews