# Color Usage

## Understanding Color in Data Visualization
Color is a powerful tool in data visualization but must be used thoughtfully. Effective color use enhances understanding, while poor color choices can confuse or mislead.

## Color Perception

### Human Color Vision
- **Trichromatic vision**: Three types of cone cells
- **Color discrimination**: Limited ability to distinguish colors
- **Context effects**: Colors appear different based on surroundings
- **Cultural differences**: Color meanings vary across cultures
- **Individual differences**: Color blindness affects many people

### Color Blindness
- **Types**: Protanopia, Deuteranopia, Tritanopia
- **Prevalence**: ~8% of men, ~0.5% of women
- **Impact**: Red-green color blindness most common
- **Consideration**: Design for colorblind accessibility
- **Testing**: Use colorblind simulators

## Color Functions in Visualization

### Categorical Colors
- **Purpose**: Distinguish discrete categories
- **Requirements**: Distinct, distinguishable colors
- **Limit**: Maximum 5-7 categories
- **Palettes**: Qualitative color palettes
- **Example**: Different product categories

### Sequential Colors
- **Purpose**: Show ordered data (low to high)
- **Requirements**: Perceptually uniform gradient
- **Use cases**: Heat maps, choropleth maps
- **Palettes**: Sequential color palettes
- **Example**: Temperature scale

### Diverging Colors
- **Purpose**: Show deviation from midpoint
- **Requirements**: Two sequential palettes meeting at neutral
- **Use cases**: Positive/negative values, differences
- **Palettes**: Diverging color palettes
- **Example**: Profit/loss, above/below average

### Highlighting
- **Purpose**: Draw attention to specific elements
- **Requirements**: Contrast with other colors
- **Use cases**: Outliers, key data points
- **Approach**: Neutral palette + highlight color
- **Example**: Highlighting one bar in a bar chart

## Color Palettes

### Qualitative Palettes
- **Purpose**: Categorical data
- **Characteristics**: Distinct, no inherent order
- **Examples**: Set1, Set2, Set3 (ColorBrewer)
- **Guidelines**: Maximum 5-7 colors
- **Accessibility**: Colorblind-friendly options

### Sequential Palettes
- **Purpose**: Ordered data
- **Characteristics**: Perceptually uniform gradient
- **Examples**: Blues, Greens, Oranges (ColorBrewer)
- **Guidelines**: Light to dark or dark to light
- **Considerations**: Lightness should increase monotonically

### Diverging Palettes
- **Purpose**: Data with meaningful midpoint
- **Characteristics**: Two hues meeting at neutral
- **Examples**: RdBu, PRGn, PiYG (ColorBrewer)
- **Guidelines**: Equal lightness steps
- **Neutral color**: Often light gray or white

## Common Mistakes

### Rainbow Color Schemes
- **Problem**: Not perceptually uniform
- **Impact**: Misleading perception of data
- **Solution**: Use perceptually uniform palettes
- **Exception**: Cyclical data (hours, directions)

### Too Many Colors
- **Problem**: Hard to distinguish
- **Impact**: Confusing visualization
- **Solution**: Limit categories, group similar items

### Insufficient Contrast
- **Problem**: Colors hard to distinguish
- **Impact**: Accessibility issues
- **Solution**: Ensure sufficient contrast ratios

### Inconsistent Color Use
- **Problem**: Same color means different things
- **Impact**: Confusing interpretation
- **Solution**: Consistent color coding across charts

### Ignoring Color Blindness
- **Problem**: Inaccessible to many viewers
- **Impact**: Excludes portion of audience
- **Solution**: Use colorblind-friendly palettes

## Best Practices

### Planning
- **Purpose**: Define color function
- **Audience**: Consider accessibility
- **Data type**: Match to appropriate palette
- **Context**: Cultural considerations
- **Testing**: Test with colorblind simulators

### Implementation
- **Palette selection**: Choose appropriate palette
- **Consistency**: Use colors consistently
- **Contrast**: Ensure sufficient contrast
- **Legend**: Clear legend when needed
- **Labels**: Direct labeling when possible

### Review
- **Accessibility**: Test for color blindness
- **Clarity**: Ensure colors distinguishable
- **Consistency**: Check across visualizations
- **Effectiveness**: Test with audience
- **Refinement**: Adjust as needed

## Accessibility

### Color Blindness
- **Types**: Consider all types
- **Simulation**: Use simulators to test
- **Palettes**: Use colorblind-friendly palettes
- **Alternatives**: Provide non-color alternatives
- **Testing**: Include colorblind users in testing

### Contrast Ratios
- **Standard**: WCAG AA or AAA
- **Text**: Higher contrast needed
- **Graphics**: Lower contrast acceptable
- **Tools**: Use contrast checkers
- **Guidelines**: Follow accessibility standards

### Alternative Encoding
- **Patterns**: Add patterns to colors
- **Labels**: Direct labeling
- **Symbols**: Different shapes
- **Texture**: Add texture differences
- **Multiple cues**: Use multiple visual channels

## Color in Different Chart Types

### Bar Charts
- **Use**: Categorical or highlighting
- **Guidelines**: Distinct colors for categories
- **Highlight**: One color different from others
- **Consistency**: Same colors across comparison charts

### Line Charts
- **Use**: Distinguish multiple lines
- **Guidelines**: Maximum 5-7 lines
- **Alternatives**: Different line styles if needed
- **Legend**: Essential for multiple lines

### Scatter Plots
- **Use**: Distinguish groups
- **Guidelines**: Distinct colors for groups
- **Transparency**: Use for overlapping points
- **Size**: Can use size as additional dimension

### Heat Maps
- **Use**: Sequential or diverging
- **Guidelines**: Perceptually uniform palette
- **Legend**: Essential for interpretation
- **Neutral**: Appropriate for missing data

### Maps
- **Use**: Sequential, diverging, or qualitative
- **Guidelines**: Match to data type
- **Considerations**: Geographic context
- **Legend**: Critical for interpretation

## Tools and Resources

### Color Palette Tools
- **ColorBrewer**: Standard for palettes
- **Viridis**: Perceptually uniform palettes
- **Coolors**: Palette generator
- **Adobe Color**: Professional tool
- **Paletton**: Color scheme designer

### Accessibility Tools
- **Coblis**: Color blindness simulator
- **Toptal**: Color filter
- **WebAIM**: Contrast checker
- **Sim Daltonism**: Mac simulator
- **Chrome extensions**: Various tools

### Implementation
- **R**: ColorBrewer, viridis packages
- **Python**: matplotlib, seaborn palettes
- **Tableau**: Built-in palettes
- **Power BI**: Custom color themes
- **D3.js**: Full color control

## Cultural Considerations

### Color Meanings
- **Red**: Danger (West), luck (Asia)
- **White**: Purity (West), mourning (some Asian cultures)
- **Black**: Mourning (West), different meanings elsewhere
- **Green**: Nature, money (varies)
- **Context**: Always consider cultural context

### International Audiences
- **Research**: Understand cultural meanings
- **Testing**: Test with target audience
- **Flexibility**: Be prepared to adjust
- **Documentation**: Explain color choices
- **Alternatives**: Provide multiple options

## Advanced Techniques

### Conditional Formatting
- **Rules**: Color based on values
- **Thresholds**: Meaningful breakpoints
- **Gradients**: Smooth transitions
- **Highlighting**: Emphasize key values
- **Automation**: Dynamic color assignment

### Interactive Color
- **Hover effects**: Highlight on interaction
- **Selection**: Emphasize selected items
- **Filtering**: Dim non-selected items
- **Animation**: Smooth color transitions
- **User control**: Allow color palette changes

### Multi-Dimensional Color
- **Hue**: Categorical information
- **Lightness**: Ordered information
- **Saturation**: Intensity/attention
- **Combination**: Multiple dimensions in one
- **Caution**: Can become complex