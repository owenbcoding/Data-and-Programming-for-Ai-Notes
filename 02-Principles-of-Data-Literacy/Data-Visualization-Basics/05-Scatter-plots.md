# Scatter Plots

## Understanding Scatter Plots
Scatter plots display values for two numerical variables as points on a Cartesian coordinate system, revealing relationships, patterns, and correlations between variables.

## When to Use Scatter Plots

### Appropriate Situations
- Exploring relationships between two numerical variables
- Identifying correlations
- Detecting patterns and clusters
- Finding outliers
- Assessing linearity

### Inappropriate Situations
- Categorical data (use bar charts)
- Time series (use line charts)
- Distribution of single variable (use histograms)
- Part-to-whole relationships (use pie charts)
- Ranking (use bar charts)

## Types of Scatter Plots

### Basic Scatter Plot
- Two numerical variables
- Simple point display
- Most common type
- Clear relationship visualization
- Easy to understand

### Grouped Scatter Plot
- Points colored by category
- Multiple groups shown
- Pattern comparison
- Can become cluttered
- Legend essential

### Bubble Chart
- Point size shows third variable
- Three dimensions displayed
- Can be cluttered
- Size perception challenges
- Rich information display

### Scatter Plot Matrix
- Multiple scatter plots in grid
- Many variable pairs shown
- Overview of relationships
- Pattern detection
- Exploratory tool

### Connected Scatter Plot
- Points connected in sequence
- Shows path/trajectory
- Time or order component
- Specialized use
- Storytelling potential

## Design Best Practices

### Axes and Scales
- Appropriate scale for both axes
- Consider aspect ratio
- Clear axis labels with units
- Grid lines optional but helpful
- Origin at (0,0) if meaningful

### Point Styling
- Appropriate point size
- Semi-transparent for overlapping points
- Consistent point styling
- Distinct colors for groups
- Avoid decorative elements

### Color Usage
- Colorblind-friendly palette
- Distinct colors for groups
- Consistent color coding
- Use color meaningfully
- Avoid too many colors

### Overplotting Solutions
- Transparency/alpha blending
- Jitter (small random position)
- Hexbin plots
- Contour plots
- Sampling

## Interpreting Scatter Plots

### Relationship Patterns
- **Positive**: Points trend upward (left to right)
- **Negative**: Points trend downward
- **No correlation**: Random scatter
- **Linear**: Points follow straight line
- **Non-linear**: Curved pattern

### Strength Assessment
- **Strong**: Points close to pattern
- **Moderate**: Some deviation
- **Weak**: Much scatter
- **None**: Random distribution
- Consider context

### Outlier Detection
- Points far from main pattern
- Can influence correlation
- May indicate errors
- Could be important findings
- Require investigation

### Cluster Identification
- Groups of points
- May indicate subgroups
- Suggests mixed populations
- Important for analysis
- Segmentation opportunity

## Common Mistakes

### Overplotting
- Too many points overlap
- Patterns obscured
- **Solution**: Use transparency, jitter, or alternative plots

### Wrong Scale
- Distorted relationships
- Misleading patterns
- **Solution**: Use appropriate scales, consider aspect ratio

### Ignoring Outliers
- Missing important information
- Biased correlation
- **Solution**: Identify and investigate outliers

### Over-Interpretation
- Seeing patterns in random data
- **Solution**: Calculate correlation, consider sample size

### Poor Color Choices
- Indistinguishable groups
- Colorblindness issues
- **Solution**: Use distinct, accessible colors

## Creating Effective Scatter Plots

### Data Preparation
- Clean numerical data
- Handle missing values
- Consider transformations
- Identify categorical groups
- Prepare labels

### Chart Selection
- Basic vs. grouped
- Add size dimension (bubble)
- Consider overplotting
- Plan color scheme
- Add trend line if appropriate

### Design Implementation
- Set appropriate scales
- Style points clearly
- Add transparency if needed
- Include clear labels
- Add legend if grouped

### Review and Refine
- Check for overplotting
- Ensure readability
- Test with audience
- Add trend line if helpful
- Finalize design

## Advanced Techniques

### Trend Lines
- Linear regression line
- LOESS smoothing
- Polynomial fits
- Multiple trend lines
- Confidence intervals

### Marginal Distributions
- Histograms on axes
- Box plots on axes
- Distribution context
- Combined visualization
- Enhanced understanding

### Annotation
- Label specific points
- Highlight outliers
- Add context notes
- Explain patterns
- Guide interpretation

### Interactive Features
- Hover for details
- Zoom and pan
- Filter points
- Link to other plots
- Exploration tools

### 3D Scatter Plots
- Three numerical variables
- Can be hard to interpret
- Interactive rotation helpful
- **Alternative**: Use 2D projections
- Use with caution

## Scatter Plot Alternatives

### Hexbin Plots
- Binned into hexagons
- Color shows density
- Good for dense data
- Reduces overplotting
- Pattern preservation

### Contour Plots
- Density contours
- Smooth pattern display
- Good for large datasets
- Continuous representation
- Aesthetic choice

### 2D Density Plots
- Smooth density estimate
- Similar to contour
- Kernel density estimation
- Elegant display
- Pattern emphasis

## Correlation and Scatter Plots

### Visual Correlation Assessment
- Strong positive: tight upward pattern
- Weak positive: loose upward pattern
- No correlation: random scatter
- Weak negative: loose downward pattern
- Strong negative: tight downward pattern

### Correlation Coefficient
- Calculate Pearson or Spearman
- Relate to visual pattern
- Consider outliers' influence
- Statistical significance
- Contextual interpretation

### Linearity Assessment
- Points follow straight line?
- Curved pattern present?
- Consider transformations
- Non-linear alternatives
- Model selection guide

## Applications

### Scientific Research
- Variable relationship exploration
- Hypothesis generation
- Experimental data analysis
- Pattern discovery
- Publication quality figures

### Business Analytics
- Sales driver analysis
- Customer behavior patterns
- Performance metrics
- Risk assessment
- Decision support

### Quality Control
- Process parameter relationships
- Quality characteristic correlations
- Outlier detection
- Process optimization
- Capability analysis

## Tools and Implementation

### Software Options
- Excel/Google Sheets
- Tableau, Power BI
- R (ggplot2)
- Python (matplotlib, seaborn)
- JavaScript libraries (D3.js, Plotly)

### Code Examples
- Basic scatter plot
- Grouped scatter plot
- Bubble chart
- Trend line addition
- Custom styling

## Best Practices Summary

### Do
- Use for two numerical variables
- Handle overplotting appropriately
- Identify and investigate outliers
- Add trend lines when helpful
- Use accessible colors

### Don't
- Use for categorical data
- Ignore overplotting
- Over-interpret random patterns
- Use 3D unless necessary
- Make points too large