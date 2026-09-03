# Data Bias Analysis Template

## Case Study: Hiring Algorithm Bias

### Scenario
A company uses an AI algorithm to screen job applicants. The algorithm was trained on 10 years of historical hiring data.

### Potential Bias Issues to Identify

#### 1. Historical Bias
- **Issue**: Training data reflects past discriminatory hiring practices
- **Example**: If the company historically hired fewer women for technical roles, the algorithm may learn to prefer male candidates
- **Detection**: Compare demographic distribution in training data vs current qualified applicant pool
- **Mitigation**: Use techniques like re-weighting or synthetic data generation

#### 2. Representation Bias
- **Issue**: Certain groups are underrepresented in the training data
- **Example**: Rural applicants may be underrepresented if the company primarily operates in urban areas
- **Detection**: Analyze geographic and demographic distribution of training data
- **Mitigation**: Ensure diverse recruitment practices and data collection

#### 3. Measurement Bias
- **Issue**: The features or labels used are biased
- **Example**: Using "years of experience" may disadvantage candidates who took career breaks
- **Detection**: Review which features are used and how they're measured
- **Mitigation**: Use alternative metrics and feature engineering

### Analysis Framework

#### Step 1: Audit Training Data
- [ ] Document data source and time period
- [ ] Analyze demographic distributions
- [ ] Check for missing data patterns
- [ ] Identify proxy variables that could introduce bias

#### Step 2: Test Model Performance
- [ ] Evaluate performance across different demographic groups
- [ ] Check for disparate impact (e.g., 80% rule)
- [ ] Analyze false positive/negative rates by group
- [ ] Review feature importance by demographic

#### Step 3: Implement Mitigation
- [ ] Pre-processing: Remove or transform biased features
- [ ] In-processing: Use fairness-aware algorithms
- [ ] Post-processing: Adjust thresholds to ensure fairness
- [ ] Monitor outcomes continuously

### Real-World Example Documentation

#### Amazon's Hiring Algorithm (2018)
- **Problem**: Algorithm penalized resumes containing the word "women's"
- **Root Cause**: Trained on 10 years of resumes, mostly from male applicants
- **Impact**: Discriminated against qualified female candidates
- **Outcome**: Project was scrapped
- **Lesson**: Historical data can perpetuate existing biases

### Your Analysis Practice

Choose a dataset and identify potential biases:
1. **Dataset Source**: 
2. **Potential Bias Type**: 
3. **Why it's a problem**: 
4. **How to detect it**: 
5. **How to mitigate it**: 

---

## Additional Bias Examples to Research

### 1. Criminal Justice Risk Assessment
- **Algorithm**: COMPAS (Correctional Offender Management Profiling for Alternative Sanctions)
- **Issue**: Found to have higher false positive rates for Black defendants
- **Reference**: ProPublica investigation, 2016

### 2. Healthcare Algorithms
- **Algorithm**: Optum health risk scoring
- **Issue**: Underestimated health needs of Black patients
- **Root Cause**: Used healthcare spending as proxy for health needs
- **Reference**: Science journal, 2019

### 3. Facial Recognition
- **Algorithm**: Various commercial systems
- **Issue**: Higher error rates for women and people of color
- **Reference**: NIST studies, 2019-2020

## Bias Prevention Checklist

- [ ] Diverse training data collection
- [ ] Regular bias audits
- [ ] Fairness metrics in evaluation
- [ ] Human oversight in high-stakes decisions
- [ ] Transparency about limitations
- [ ] Continuous monitoring
- [ ] Diversity in development team
- [ ] Stakeholder involvement in design