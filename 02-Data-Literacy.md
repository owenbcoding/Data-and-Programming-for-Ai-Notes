# Welcome to Data Literacy
## Establishing how to think about data will set you up for success when you start analyzing it.
### Data Literacy topics

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

# Welcome to Data Literacy
## Why is data literacy important?
- How data literacy helped 19th-century doctors end cholera epidemics and discover the root cause of the disease.
- Data Litreracy helped reveal discrimination in hard-to-measure settings like hiring practices and advance medical knowledge by improving clinical trial data quality.
- Data literacy also helps us to produce readable work for other people. As we’ll see, even when good data is there, the inability to tell a clear story can have dire consequences.
- Data is an incredibly powerful tool.

Case Studies in Data Literacy
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

