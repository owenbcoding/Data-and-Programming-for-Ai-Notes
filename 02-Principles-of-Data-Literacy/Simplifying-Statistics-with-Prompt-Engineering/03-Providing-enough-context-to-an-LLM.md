# Providing Enough Context to an LLM

## The Importance of Context
Providing sufficient context is crucial for getting accurate and relevant statistical analysis from AI. Without proper context, AI may make inappropriate assumptions or choose wrong methods.

## Types of Context to Provide

### Data Context
- **Data type**: Numerical, categorical, ordinal, etc.
- **Data structure**: Sample size, variables, format
- **Data source**: Where data came from
- **Data quality**: Missing values, outliers, issues
- **Data collection method**: How data was gathered

### Analysis Context
- **Research question**: What you're trying to answer
- **Analysis purpose**: Why you need the analysis
- **Decision context**: How results will be used
- **Stakeholders**: Who will use the results
- **Constraints**: Time, resources, limitations

### Statistical Context
- **Prior knowledge**: What you already know
- **Previous analyses**: What has been tried
- **Field conventions**: Standard practices in your field
- **Regulatory requirements**: Any compliance needs
- **Publication standards**: If for academic publication

### Domain Context
- **Industry/field**: Healthcare, finance, retail, etc.
- **Subject matter**: Specific domain knowledge
- **Business/operational context**: How it fits in organization
- **Technical constraints**: Software, hardware limitations
- **Expertise level**: Your statistical background

## Structuring Context in Prompts

### Context Framework
1. **Data Description**: What data do you have?
2. **Analysis Goal**: What do you want to learn?
3. **Constraints**: What limitations exist?
4. **Background**: What is already known?
5. **Output Needs**: What format do you need?

### Example Context Statement
```
I have a dataset of 1,000 customer records with the following variables:
- Age (numerical, range 18-80)
- Purchase amount (numerical, range $10-$500)
- Customer type (categorical: new, returning, VIP)
- Satisfaction score (ordinal 1-5)

I want to understand what factors influence purchase amounts.
This analysis will inform our marketing strategy.
We need results suitable for presentation to non-technical executives.
We have limited statistical expertise on the team.
Please use robust methods that don't require advanced statistical knowledge to interpret.
```

## Context Elements by Analysis Type

### Descriptive Statistics
- Sample size and population
- Variable types and ranges
- Missing data patterns
- Any known data issues
- Purpose of description

### Comparison Analysis
- Group definitions
- Why groups are being compared
- Expected differences
- Practical significance thresholds
- How results will be used

### Relationship Analysis
- Variables of interest
- Expected relationship direction
- Why relationship matters
- Confounding variables to consider
- Action implications

### Predictive Modeling
- Target variable definition
- Available predictors
- Prediction purpose
- Accuracy requirements
- Interpretability needs

## Common Context Mistakes

### Insufficient Data Information
- Not mentioning sample size
- Not specifying variable types
- Hiding data quality issues
- Not describing data structure
- **Impact**: Wrong method selection

### Missing Analysis Purpose
- Not stating why analysis is needed
- Not explaining how results will be used
- Not identifying decision context
- Not specifying audience
- **Impact**: Inappropriate recommendations

### Ignoring Constraints
- Not mentioning time/resource limits
- Not stating expertise level
- Not noting software/hardware constraints
- Not considering regulatory requirements
- **Impact**: Unrealistic suggestions

### Overlooking Domain Knowledge
- Not providing field context
- Not sharing subject matter expertise
- Not mentioning industry standards
- Not considering practical implications
- **Impact**: Theoretically correct but practically useless

## Progressive Context Building

### Start Simple
- Basic data description
- Simple analysis question
- General context
- Add detail as needed
- Refine based on responses

### Iterative Enhancement
- Begin with high-level context
- Add specifics as conversation progresses
- Respond to AI questions
- Incorporate new information
- Build comprehensive picture

### Context Layering
1. **Layer 1**: Basic data and question
2. **Layer 2**: Analysis purpose and constraints
3. **Layer 3**: Domain knowledge and requirements
4. **Layer 4**: Specific method preferences
5. **Layer 5**: Output and reporting needs

## Context Templates

### Basic Analysis Template
```
Data: [describe data type, size, variables]
Question: [what you want to know]
Purpose: [why you need this]
Constraints: [limitations or requirements]
```

### Advanced Analysis Template
```
Data Description:
- Type: [numerical/categorical/mixed]
- Size: [n observations]
- Variables: [list and describe]
- Quality: [issues, missing data, outliers]
- Collection: [how data was gathered]

Analysis Goal:
- Research question: [specific question]
- Purpose: [why analysis needed]
- Use: [how results will be applied]
- Audience: [who will see results]

Constraints:
- Expertise: [your statistical level]
- Resources: [time, software, data access]
- Requirements: [regulatory, publication, business]
- Preferences: [methods to use/avoid]

Background:
- Previous work: [what's been done]
- Domain knowledge: [relevant field info]
- Expectations: [what you anticipate]
```

## Context Quality Checklist

### Data Context
- [ ] Data types specified
- [ ] Sample size provided
- [ ] Variable ranges mentioned
- [ ] Data quality issues noted
- [ ] Collection method described

### Analysis Context
- [ ] Research question clear
- [ ] Analysis purpose stated
- [ ] Decision context explained
- [ ] Stakeholders identified
- [ ] Constraints mentioned

### Statistical Context
- [ ] Prior knowledge shared
- [ ] Previous analyses noted
- [ ] Field conventions mentioned
- [ ] Regulatory needs stated
- [ ] Publication standards referenced

### Domain Context
- [ ] Industry/field specified
- [ ] Subject matter described
- [ ] Business context provided
- [ ] Technical constraints noted
- [ ] Expertise level indicated

## Advanced Context Techniques

### Scenario-Based Context
- Describe the full scenario
- Include decision-making context
- Explain consequences of errors
- Describe stakeholder perspectives
- Paint complete picture

### Comparative Context
- Compare with similar situations
- Reference standard approaches
- Contrast with alternative methods
- Provide benchmark examples
- Include industry comparisons

### Historical Context
- Describe previous analyses
- Explain what worked/didn't work
- Note lessons learned
- Reference historical data
- Include organizational memory

## Best Practices

### Be Specific
- Use concrete numbers when possible
- Provide exact variable names
- Specify exact constraints
- Give precise requirements
- Avoid vague descriptions

### Be Relevant
- Include only necessary context
- Focus on analysis-relevant information
- Avoid unnecessary details
- Keep descriptions focused
- Prioritize important information

### Be Honest
- Acknowledge limitations
- Admit knowledge gaps
- State constraints clearly
- Don't overstate expertise
- Be transparent about needs

### Be Structured
- Organize context logically
- Use clear headings
- Present information systematically
- Follow consistent format
- Make context easy to parse

## Troubleshooting Context Issues

### AI Asks for More Information
- Provide requested details
- Ask what specific information needed
- Offer to provide additional context
- Clarify what aspects are unclear
- Engage in dialogue

### AI Provides Irrelevant Analysis
- Re-examine your context
- Add missing information
- Refine your question
- Specify constraints more clearly
- Re-state your purpose

### AI Makes Wrong Assumptions
- Explicitly state correct assumptions
- Provide contradictory examples
- Describe why assumptions are wrong
- Give specific counter-examples
- Guide AI to correct understanding