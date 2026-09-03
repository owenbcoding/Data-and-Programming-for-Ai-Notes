# Welcome to Data Literacy

## Establishing how to think about data will set you up for success when you start analyzing it.

## Codecademy subsections (exact order)

### 1) Introduction to Data

From your course view, this subsection contains:

- Informational: Welcome to Data Literacy
- Lesson: Case Studies in Data Literacy
- Article: Data Collection methods, ethics and free sources
- Lesson: Data Types and Quality
- Quiz: Data Types and Quality

Detailed lesson notes for this subsection:

- Data Gaps
- Addressing Bias

### 2) Thinking about Data

From your course structure (`1 Lesson, 1 Quiz, 1 Article`):

- Lesson: What is Statistics? / Numeracy *(both topics are covered inside this single lesson)*
- Article: Statistics At Work
- Quiz: Thinking about Data

Detailed lesson notes for this subsection:

- What is Statistics?
- Statistics At Work
- Numeracy

#### Quiz: Thinking about Data
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

### 3) Visualizing Data

From your course structure (`2 Lessons, 1 Quiz, 1 Article`):

- Lesson: High Stakes Visualizations
- Lesson: The Challenger Visualizations
- Article: *(supplementary visualization reading)*
- Quiz: Visualizing Data

Detailed lesson notes for this subsection:

- High Stakes Visualizations
- The Challenger Visualizations

#### Quiz: Visualizing Data
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

### 4) Analyzing Data

From your course structure (`1 Lesson, 1 Article, 1 Quiz`):

- Lesson: Causal Analysis and John Snow's cholera theory: Part 1
- Article: Causal Analysis and John Snow's cholera theory: Part 2
- Quiz: Analyzing Data

Detailed lesson notes for this subsection:

- Causal Analysis and John Snow's cholera theory: Part 1
- Causal Analysis and John Snow's cholera theory: Part 2

#### Quiz: Analyzing Data
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

### Detailed notes

### Data literacy topics

Case studies about what can go wrong – and right in data projects.
Basic assumptions of working with different types of data.
How data types affect the analysis.
Foundational statistical ideas.
Key ideas behind good (and misleading) visualizations.

After this unit, you will be able to:

Spot messy data and make a plan to clean it.
Critically evaluate whether a statistical technique is a good idea.
Apply appropriate data manipulation methods.
Spot the difference between good and bad visualizations.
Make a plan for how to transform a bad visualization into a good one.
Reference classic case studies involving perfect and poor data analysis.

### Why is data literacy important?

- How data literacy helped 19th-century doctors end cholera epidemics and discover the root cause of the disease.
- Data literacy helped reveal discrimination in hard-to-measure settings like hiring practices and advance medical knowledge by improving clinical trial data quality.
- Data literacy also helps us to produce readable work for other people. As we’ll see, even when good data is there, the inability to tell a clear story can have dire consequences.
- Data is an incredibly powerful tool.

Case studies in data literacy use real examples (health, hiring, law, and spaceflight) so you can practice asking critical questions about data quality, bias, statistics, and visualization—themes that show up throughout the outline above.

---

# Data Gaps

Garbage in, garbage out is a data-world phrase that means our data-driven conclusions are only as strong, robust, and well-supported as the data behind them.

For example: we have a lot of data on heart attacks, but there is still room for improvement when it comes to data quality. Heart disease is the leading cause of death in women, but as of 2021, women accounted for only 38% of participants in relevant research studies.

There are key differences between men’s and women’s heart attacks that affect how they are treated, but our data does not yet adequately capture those differences. That gap ultimately leads to worse treatment outcomes and a higher post-heart attack mortality rate for women.

How does data literacy factor in? Part of understanding and communicating with data is asking the right questions so we end up with useful, relevant data. We can already answer many questions about heart attacks, but we will not learn the ins and outs of women’s heart attacks by studying mostly men.

Part of practicing good data literacy means asking:

- Do we have sufficient data to answer the question at hand?
- Can my data answer my exact question?

### Image

These two questions are easier to act on when you can *see* where data is thin or missing. The figure below is one way to picture that gap.

![Illustration related to data gaps and asking whether your data fits the question](images/data-gaps/1606.svg)

# Addressing Bias

One question the data on heart attacks might prompt is: “Why did the trials have only 38% female participation?”

In part, for historical reasons: in the 1950s, pregnant women in Europe and Canada were prescribed a drug called thalidomide for morning sickness. The drug caused severe birth defects and was withdrawn from the market. As a result, in 1977 the US Food and Drug Administration (FDA) recommended excluding from early-stage clinical trials all women who could become pregnant. While intended to protect women, the recommendation put them at risk in a different way, by limiting our knowledge of how drugs affect women’s bodies.

The FDA reversed these recommendations in the 1990s, and today government-funded clinical trials must include women and other minorities. Yet trials do not need to include minority groups at representative levels, and the majority of drug trials in the US are not government-funded.

In this case, participation might also be shaped by media representation. In typical TV or movie heart attacks, we almost always see a man clutching his arm or chest. Not only do women have heart attacks too (we would not know it from watching TV), they rarely experience chest pain as a symptom.

(In fact, in the top 20 “heart attack” movies\* on IMDb, only two heart attacks happen to women: one is fake, and the other is a disguised murder. So… zero real heart attacks in women in a list of top 20 “heart attack” movies!)

It might seem like a stretch from data literacy to TV heart attacks, but sound science means examining bias and controlling variables wherever possible.

Part of practicing good data literacy means asking:

- Who participated in the data?
- Who is left out?
- Who made the data?

\*Top movies with the keyword “heart attack” where a heart attack is actually mentioned or shown in the movie—not *The Exorcist*, which is on that list because people have had heart attacks while watching it… yikes!

### Image

The timeline below lines up key moments in this story—from thalidomide and the 1977 FDA guidance through later shifts in trial policy—so you can see how policy and data collection evolved together.

![Timeline of clinical trial policy and related history](images/addressing-bias/timeline.svg)

# Data Types and Quality

## Lesson: Data Types and Quality

### Introduction to Data Types and Quality
- Data quality determines how trustworthy any analysis or model will be.
- Four key quality dimensions: **accuracy**, **validity**, **completeness**, and **representativeness**.
- Before modelling, always profile your dataset: shape, dtypes, missing value counts, and value ranges.

### The Shape of Data
- **Tabular data** is organised into rows (observations / records) and columns (variables / features).
- `df.shape` → `(rows, columns)` — the first sanity check on any new dataset.
- **Wide format:** each row is one subject, each column is one measurement (common in ML feature tables).
- **Long format:** one row per observation per variable (common in time-series and Pandas `melt()`).
- Tidy data rule: one variable per column, one observation per row, one value per cell.

### Variable Types
- **Quantitative (numerical):** measurable amounts.
  - *Continuous* — any value in a range (height, temperature, salary).
  - *Discrete* — countable whole numbers (number of siblings, page count).
- **Qualitative (categorical):** labels or groups.
  - *Nominal* — no natural order (colour, country, blood type).
  - *Ordinal* — has a meaningful order but gaps between ranks are unequal (education level: high school < bachelor's < master's).
- Knowing the type tells you which statistics and charts are valid:
  - Nominal → bar chart, mode.
  - Ordinal → bar chart, median.
  - Continuous → histogram, mean, standard deviation.

### Dealing with Messy Data
- **Duplicates:** `df.duplicated().sum()` — drop with `df.drop_duplicates()`.
- **Inconsistent strings:** `"Male"`, `"male"`, `"M"` all mean the same thing → normalise with `.str.lower().str.strip()`.
- **Wrong data types:** a numeric column stored as `object` breaks aggregations → cast with `pd.to_numeric()` or `.astype()`.
- **Outliers:** values far outside the expected range. Options: cap, remove, or flag with a boolean column. Always investigate *why* the outlier exists before deleting.
- **Mixed formats:** dates as `"01/06/2024"` vs `"June 1, 2024"` → parse with `pd.to_datetime(format=...)`.

### Working with Missing Data
- Missing data shows up as `NaN` (Not a Number) in Pandas.
- `df.isnull().sum()` — count missing values per column.
- `df.isnull().mean() * 100` — percentage missing per column (quick health check).
- **Three common strategies:**
  1. **Drop** — `df.dropna()` — safe only when missingness is random and few rows are affected.
  2. **Impute with a statistic** — fill with mean (numerical) or mode (categorical): `df.fillna(df['col'].mean())`.
  3. **Flag then fill** — add a `col_was_missing` boolean column *before* imputing so the model can learn from the pattern.
- **MCAR / MAR / MNAR** — Missing Completely At Random / At Random / Not At Random. MNAR is most dangerous because the fact that it's missing *is* informative.

### Accuracy
- **Accuracy** = the data value matches the real-world value.
- Inaccurate data often comes from manual entry errors, sensor faults, or unit mismatches (cm vs inches).
- Quick checks: compare min/max to plausible ranges, cross-reference against a trusted source.
- Example: a patient recorded as 7 feet 2 inches when they are 5 feet 2 inches — possible data entry error (7 vs 5).

### Validity
- **Validity** = the data value is a legal value for that variable.
- A valid value can still be inaccurate (e.g. a valid age of 25 entered for a 35-year-old).
- Enforce validity with constraints: age ≥ 0, email contains `@`, category values in an allowed set.
- In Python: `df['age'].between(0, 120).all()` is a simple validity check.

### Representative Samples
- A **representative sample** mirrors the distribution of the full population you want to study.
- An unrepresentative sample causes **sampling bias** — conclusions will not generalise.
- Example: surveying only university students about average income would underestimate the national mean.
- Strategies to improve representativeness: stratified sampling (sample each subgroup proportionally), random sampling, oversampling underrepresented groups.
- Always ask: **who is in this dataset, and who is missing?**

### Review of Data Types and Quality
- Key takeaways:
  - Identify variable type first → it dictates every downstream analysis choice.
  - Profile missing data before modelling — impute thoughtfully, not blindly.
  - Accuracy and validity are different: both must be checked.
  - A representative sample is the foundation of a generalisable model.
- What I still need to revise: MNAR imputation strategies, advanced outlier detection (IQR method, z-score).

## Quiz: Data Types and Quality
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

# What is Statistics?

Now let’s look at a case study that showcases the value of data literacy in the legal system.

Big, amorphous injustices like hiring discrimination are hard to prove in court. Hiring discrimination is a pattern of biased behavior toward candidates. That bias results in qualified candidates not being hired because of their traits.

Throughout the 1900s, companies in the US were able to justify hiring on a case-by-case basis. After all, it is legal to hire or not hire candidates based in part on soft qualities such as “fit” and “office culture.” But if those qualities mask factors like a candidate’s race, gender, or religion, the company has broken anti-discrimination laws.

Usually, a lawyer would have to show many individual cases proving a company was discriminatory. Instead, lawyer Elaine W. Shoben shifted the burden of proof to companies. How was she able to do this with data literacy? She used the power of statistics. Statistics helps us judge whether what we observe is likely due to random chance or to a systematic pattern.

What does that actually mean? For example, you are more likely to see more cars on the road at 8 a.m. on Wednesday than at 8 a.m. on Sunday. That is not a random occurrence—the increase in traffic lines up with rush hour and standard business hours. It is statistically more likely to see many cars during rush hour than at other times.

We’ll see in the next exercise exactly how Elaine Shoben used statistics to change how we assess bias in hiring.

### Image

Traffic can look messy, yet it still follows recurring timing and structure. The clip below is a simple visual cousin of the rush-hour example: statistics is partly about separating a pattern like that from pure coincidence.

![Cars on a road, suggesting heavier traffic at some times than others](images/statistics/cars-moving.gif)

# Statistics At Work

So how did Elaine Shoben show that discrimination was at play in hiring decisions? It is a bit heavy on the legal jargon, but we can break it down to see how it works.

First, she argued that we can use statistics to see whether the hiring results of subjective interviews are so unlikely that they could not have happened by chance. In other words, is it even possible (in statistical terms) that the pattern of who got the job could be based on random chance?

If the results could not have happened by chance, then the alternative is that they must happen by “purposeful exclusion.” In other words, it would mean people are excluded from the job by discriminatory hiring practices.

If employers are aware of the “exclusionary effect,” and they continue to use that same hiring process, then they are showing a “reckless disregard” for the rights of individual candidates not to be discriminated against in the hiring process. (Read it a few times if you need to!)

Once we acknowledge that, the burden shifts to employers to show why their hiring requirements are valid and necessary. We no longer assume the hiring practices are legitimate and make job candidates prove otherwise.

Statistics at work! That is definitely a bit of legal jargon—but how cool is it to use statistics to reveal a systematic pattern of discrimination, rather than trying to piece together a case from individual experiences? That is really what statistics is all about.

## Logic step 1 : Could the hiring results have happened by random chance? Or is that statistically impossible?
Example: Step 1
In the last 5 years, StarComm Corporation had 1,000 candidates and hired 200 people. Of the 1,000 candidates, 400 were women (40%). Of the 200 people hired, only 20 were women (10%).

## Logic step 2 : If the hiring results have happened by chance they must have happened by "purposeful exclusion"
Example: Step 2
Statisticians determine that the probability of getting these hiring results by chance is essentially zero. Lawyers can then conclude that the low number of women hired isn't accidental, but purposeful in some way.

## Logic step 3 : If the employer is aware of this "purposeful exclusion" they show "reckless disregard" for the rights of individual candidates not to be discriminated against.
Example: Step 3
StarComm Corporation is now aware that their hiring practice discriminates against women. So lawyers can argue that SCC violated the rights of women candidates to have a fair shot (without discrimination) in the hiring process.

## Logic step 4: The burden of proof shifts to the employer to prove why hiring requirements are valid and necessary.
Example: Step 4
The burden is now on StarComm Corporation to get its hiring process into legal shape OR to prove why its hiring process has to be the way it is. It's no longer the job of individual women candidates to prove they are up against an unfair process.

# High Stakes Visualizations

Okay, we’ve walked through recognizing data quality and bias in healthcare and using statistics to answer big legal questions. Where else does data literacy come into play?

Data visualization is one of the most visible and obvious places we interact with data. It helps us explore and understand data-driven arguments and is a powerful tool for communication.

While most data visualization we see is of the “everyday” variety, in this case study we’ll look at a highly consequential visualization: one of the charts that NASA-contracted engineers used to argue that the Challenger space shuttle should not launch on January 28, 1986.

The Challenger carried seven US astronauts who were supposed to deploy a satellite and study Halley’s Comet while in orbit. Less than two minutes after liftoff, however, the shuttle exploded, killing all seven crew members.

The explosion was caused by a failure of two O-rings: small rubber rings that helped create an airtight seal between the space shuttle and its launch fuel supply. Before the launch, engineers were concerned about how the low-temperature forecast would affect the O-rings’ ability to make a proper seal.

The engineers made their arguments in favor of postponing the launch using, in part, a series of data visualizations that showed launch success rates at various temperatures. Tragically, their arguments did not prevent the launch from proceeding.

### Image

The Challenger story is a stark reminder that how we show data can carry life-or-death weight. The figure below is a simple space-themed illustration to pair with this case.

![Rocket illustration](images/high-stakes-visualizations/rocketship.svg)

# The Challenger Visualizations

Before we pick apart this visualization, it is worth saying that hindsight is 20/20. If it were as simple as “obviously, the O-rings were going to fail,” then the Challenger would never have been launched. This event was the culmination of several years of context, not an isolated incident, so many other factors were at play.

Following the incident, a Presidential Commission was initiated to investigate the causes of the catastrophe. The commission determined that the disaster was directly the result of O-ring failure. However, the commission also concluded that management from both NASA and Morton Thiokol (the company NASA had contracted to design and maintain its rocket boosters) had ignored evidence that indicated significant risk of O-ring failure at low launch temperatures. Additionally, the commission noted that NASA and Morton Thiokol had failed to adequately test the equipment they were using, despite consistent requests from engineers for several years preceding the incident.

In short, it is unlikely that this particular visualization played a pivotal role in the decision-making conversation that ended with management deciding to launch as scheduled.

From a data literacy standpoint, though, we can definitely see how a better visualization would make the trend of the data more apparent. The engineers had the data to know that O-rings began to fail at lower temperatures. But their visualization was not created in a way that made that danger clear.

The visualization of rocket launches was organized by date, which made it hard to see the pattern of launch failures at lower temperatures (see the top-right image). When Edward Tufte later organized the rockets by temperature, that pattern became much more obvious (see the lower image). Additionally, including all of the rocket symbols for decoration did not make the argument clearer, but instead added distracting visuals to the page.

The visualization would have been easier to interpret with fewer distracting lines and a more direct link between temperature and launch failures.

While most of us will (thankfully) never be in the position of making or interpreting life-or-death data visualizations, good data literacy helps us make informed decisions every day. Should I bring an umbrella? Should I postpone my trip to avoid public health risks? Should I buy stock in Blockbuster? Whatever the questions, improving our data literacy can help us reach the answers.

### Image

Tufte’s reorganization of the launch data (temperature on one axis, clearer grouping) illustrates how the same facts can read very differently depending on layout—compare the discussion above with the figure below.

![Tufte-style Challenger launch data visualization](images/challenger-visualizations/tufte-challenger-viz1.svg)

# Numeracy

## Lesson: Statistical Thinking

Let’s imagine we are working for the city government of the fictional city of Melody Metropolis. The mayor of Melody Metropolis wants to know more about the musicians who currently live in the city. The learning environment shows a dataset we have on musicians living in the city as of last year. How would you describe this dataset? See if you can answer any of the following questions:

What does a typical musician’s income look like?
Is there a wide range of musician ages?
What proportion of the musicians in the dataset play guitar?
We can try to make generalizations by looking over the rows and columns, but it’s difficult to answer these questions precisely. We need some kind of “data vocabulary” that can help us measure and describe the 
variables
Preview: Docs Loading link description
 in the dataset. Summary statistics can be used for exactly this purpose!

With a basic understanding of summary 
statistics
Preview: Docs Statistics is the science that is concerned with methods for collecting, organizing, analyzing, and interpreting data.
, we can communicate and understand a lot more specific information about the musicians in the city. But learning statistics is often associated with a lot of negativity:

Memorization of lots of math formulas
Long calculations done by hand
Confusing or meaningless interpretations
None of these struggles need to be part of learning to use statistics. In this lesson, we’ll gain a conceptual understanding of how summary statistics can easily help us communicate and interpret our dataset.

Before moving to the next exercise, familiarize yourself with the following names and descriptions of the variables in the dataset:

age: age in years
income: yearly income in US dollars
title: primary job title
experience: years of experience in the field of music
instrument: primary instrument
band: whether in a band (1 = yes, 0 = no)
What are you interested in learning about the musicians of Melody Metropolis?

### Introduction to Statistical Thinking
- **Statistical thinking** is the ability to understand and critically evaluate statistical arguments and data.
- It involves asking the right questions about data, understanding uncertainty, and recognizing patterns vs. random variation.
- Key skill: distinguishing between correlation and causation.

### Types of Statistical Questions
- **Descriptive statistics**: What does the data look like? (mean, median, mode, standard deviation)
- **Inferential statistics**: What can we conclude from the data? (hypothesis testing, confidence intervals)
- **Predictive statistics**: What will happen next? (regression, machine learning)

### Key Statistical Concepts
- **Variation**: Data naturally varies; understanding this variation is crucial.
- **Randomness**: Not all variation is meaningful; some is due to chance.
- **Sample vs. Population**: We often study samples to make inferences about populations.
- **Bias**: Systematic errors that can lead to incorrect conclusions.

### Statistical Literacy in Everyday Life
- **News headlines**: "Eating chocolate makes you smarter" - correlation ≠ causation
- **Medical studies**: Understanding relative vs. absolute risk
- **Polls and surveys: Margins of error and confidence intervals
- **Financial data**: Understanding averages vs. medians in income reports

### Common Statistical Fallacies
- **Correlation implies causation**: Just because two things are related doesn't mean one causes the other.
- **The gambler's fallacy**: Thinking that past random events affect future ones.
- **Survivor bias**: Drawing conclusions from those who "survived" a process, ignoring those who didn't.
- **Base rate fallacy**: Ignoring the underlying probability when evaluating specific evidence.

### Statistical Thinking Process
1. **Formulate the question**: What exactly are we trying to learn?
2. **Collect data**: Ensure data is relevant and representative.
3. **Analyze data**: Use appropriate statistical methods.
4. **Interpret results**: Consider limitations and alternative explanations.
5. **Communicate findings**: Present results clearly and honestly.

### Practical Applications
- **Business**: A/B testing, customer segmentation, sales forecasting
- **Healthcare**: Clinical trials, disease outbreak tracking, treatment effectiveness
- **Sports**: Player performance analysis, strategy optimization
- **Public policy**: Evaluating program effectiveness, resource allocation

### Statistical Tools and Concepts
- **Measures of center**: Mean, median, mode - when to use each
- **Measures of spread**: Range, interquartile range, standard deviation
- **Distributions**: Normal distribution, skewed distributions
- **Probability**: Basic rules, conditional probability
- **Sampling**: Random sampling, stratified sampling, sampling bias

### Critical Questions to Ask
- What is the source of the data?
- How was the data collected?
- What is the sample size?
- Are there any outliers?
- What assumptions are being made?
- What are the limitations of the analysis?
- Could there be alternative explanations?

**Numeracy** is the comfort and skill you use when working with numbers in context—not just doing arithmetic, but knowing *what* a number means and whether it is the right number for the question. It supports everything earlier in this note: interpreting headlines about percentages in trials, judging whether a gap in data is large or small, and reading axes and scales on charts without being misled.

In practice, numeracy shows up when you check whether a fraction and a percent tell the same story, estimate orders of magnitude, notice when units are missing or inconsistent, and ask whether a claim is based on counts, rates, or both. Pair those habits with the questions from the **Data Gaps** and **Addressing Bias** sections, and you have a solid foundation for the statistical and visualization ideas that follow.

## Causal Analysis and John Snow’s cholera theory: Part 1

In the world of data, we’ll hear time and time again that “correlation does not imply causation.” In other words, two variables can move together without one *causing* the other.

A “causal link” means evidence that one factor actually brings about or materially changes another—not merely that both rose or fell together. One of the most important applications of this idea over the last few centuries has been epidemiology, the study of disease in populations. Establishing sound causal links has driven major advances in how we prevent and treat illness.

Let’s take a look at one of the earliest instances of successful causal analysis in medicine, which starts with a man called John Snow. (Not the fantasy-famous Lord of the North, but a real nineteenth-century London doctor.)

Until Dr. Snow’s work in the mid-nineteenth century, many people believed that cholera was caused by vapors—the “miasma” theory—rising from the burial grounds of plague victims from centuries earlier. That fit what people knew then, but cholera is actually a waterborne disease caused by bacteria found in sewage. It causes severe dehydration and, without treatment, often killed more than half of those who became severely ill in historical outbreaks.

By studying earlier cholera epidemics and organizing his data analysis around his hunch that cholera was waterborne, Dr. Snow was able to tie an 1854 cholera outbreak in London to a contaminated water pump—making a strong case for a causal link between contaminated water and cholera before germ theory was widely accepted.

### Image

His famous map plots cholera deaths by location in Soho; the concentration around the Broad Street pump made the waterborne story visible in a way tables alone could not.

![John Snow’s map of the 1854 Broad Street cholera outbreak, deaths shown by location](images/Snow-cholera-map-1.jpg)

## Causal Analysis and John Snow's cholera theory: Part 2

Dr. John Snow’s causal analysis breakthrough started with how he visualized his data: he organized cholera death records by location rather than by time, which was more common. He made a map, and discovered that the deaths centered around a water pump on Broad Street.

From there, Dr. Snow used death records that seemed to contradict his theory to strengthen his explanation. For instance, a woman who died of cholera in a completely different neighborhood had just visited her aunt’s house near Broad Street and drunk water from the pump.

Dr. Snow also found that a workhouse and a brewery near the pump both had few or no cholera deaths. Upon investigation, he learned that the workhouse had its own water supply, and that the brewers not only had access to a well at the brewery, but that they drank only malt liquor and never visited the Broad Street pump.

Snow advised that the handle be taken off the Broad Street pump to prevent people from drinking the contaminated water. The handle was removed, and this action coincided with the end of that outbreak. The number of deaths was already trailing off (more than 75% of residents had left the area to avoid “choleric vapors”), but this public health intervention prevented the disease from recurring as people returned, and the epidemic ended.

The built-in test cases helped Snow isolate variables and prove that the key variable was that people who developed cholera had drunk water from the contaminated pump. From there, repeated studies of cholera and modern lab experiments have only confirmed the causal link he discovered.

In modern lab science, we use controlled experiments to isolate variables and prove causation. Controlled experiments are often not possible outside of lab settings, though, so data scientists do the best they can to isolate and control variables and get comfortable working with some amount of error.

