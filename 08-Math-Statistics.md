# Math and Statistics for ML/AI Engineers

This module is the foundation for understanding *why* ML methods work, not just how to call them.

**Learning path:** This is step 8 in [00-START-HERE.md](00-START-HERE.md). Previous: [07-Exploratory-Data-Analysis.md](07-Exploratory-Data-Analysis.md). Next: [09-Final-Portfolio.md](09-Final-Portfolio.md).

---

## Codecademy subsections (exact order)

### 1) Probability for ML/AI Engineers

**Core probability concepts:**

| Concept | Definition | Example |
|---|---|---|
| Event | A subset of possible outcomes | Rolling a 6 on a die |
| Probability P(A) | Likelihood of event A; range [0, 1] | P(6) = 1/6 ≈ 0.167 |
| Complement P(A') | P(not A) = 1 − P(A) | P(not 6) = 5/6 |
| Joint P(A ∩ B) | Both A and B occur | P(rain and cold) |
| Union P(A ∪ B) | A or B (or both) occur | P(A) + P(B) − P(A ∩ B) |
| Conditional P(A\|B) | P(A) given B has occurred | P(smoker\|high charges) |
| Independence | P(A ∩ B) = P(A) × P(B) | Coin flips |

**Bayes' Theorem:**
```
P(A|B) = [ P(B|A) × P(A) ] / P(B)
```
- **Prior:** P(A) — our belief before seeing evidence.
- **Likelihood:** P(B|A) — how probable the evidence is if A is true.
- **Posterior:** P(A|B) — updated belief after seeing evidence.
- Used in spam filters, medical diagnosis, and Naive Bayes classifiers.

**Practice examples:**
```python
# Simulate 10,000 coin flips and estimate P(heads)
import random
random.seed(42)
flips = [random.choice(["H", "T"]) for _ in range(10_000)]
p_heads = flips.count("H") / len(flips)
print(f"Estimated P(H) = {p_heads:.4f}")  # ≈ 0.5

# Conditional probability from a DataFrame
p_high_charge_given_smoker = (
    df[(df["smoker"] == "yes") & (df["charges"] > 20000)].shape[0]
    / df[df["smoker"] == "yes"].shape[0]
)
```

**Confusions to revisit:**
- `P(A|B) ≠ P(B|A)` — the prosecutor's fallacy (confusing these in court has wrongly convicted people).
- Independent does not mean mutually exclusive: two events can be independent but still both happen.

---

### 2) Sampling for ML/AI Engineers

**Sampling methods:**

| Method | How | When to use |
|---|---|---|
| Simple random | Pick n rows at random | General purpose; small datasets |
| Stratified | Random sample within each subgroup | Class-imbalanced data; ensures every group is represented |
| Systematic | Every k-th row | Large ordered datasets |
| Cluster | Randomly pick whole subgroups | Expensive data collection |
| Bootstrapping | Sample with replacement | Estimating uncertainty; cross-validation |

```python
# Simple random sample (Pandas)
sample = df.sample(n=200, random_state=42)

# Stratified sample (equal proportion from each region)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    df.drop("charges", axis=1), df["charges"],
    test_size=0.2, random_state=42, stratify=df["region"]
)
```

**Sampling bias risks:**
- **Selection bias:** the sample is not drawn from the full population (e.g. only surveying online users).
- **Survivorship bias:** only seeing data on "survivors" — e.g. studying successful startups and ignoring failed ones.
- **Response bias:** survey respondents differ systematically from non-respondents.
- **Undercoverage:** some subgroups are less likely to be sampled.

**Inference takeaways:**
- The **Central Limit Theorem (CLT):** the sampling distribution of the mean approaches a normal distribution as n → ∞, regardless of the original distribution. This is why so many statistical tests assume normality.
- **Standard error (SE) = σ / √n** — measures how precise a sample mean is as an estimate of the population mean. Larger n → smaller SE.
- **Confidence interval:** `mean ± z * SE` — a 95% CI means that if we repeated the sampling 100 times, ~95 intervals would contain the true population mean.

---

### 3) Linear Algebra

**Vector / matrix concepts:**

| Object | Shape notation | Python |
|---|---|---|
| Scalar | 1×1 | `x = 5.0` |
| Vector | n×1 or 1×n | `np.array([1, 2, 3])` |
| Matrix | m×n | `np.array([[1,2],[3,4]])` |

```python
import numpy as np

# Vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b          # element-wise addition → [5, 7, 9]
a * 3          # scalar multiplication → [3, 6, 9]
np.dot(a, b)   # dot product = 1×4 + 2×5 + 3×6 = 32

# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A @ B          # matrix multiplication (preferred over np.dot for matrices)
A.T            # transpose
np.linalg.inv(A)  # inverse (only for square matrices)
np.linalg.det(A)  # determinant
```

**Dot product and matrix multiplication notes:**
- Dot product of two vectors: `a · b = Σ aᵢbᵢ` — measures alignment/similarity.
- Matrix multiplication `(m×n) @ (n×p) → (m×p)` — inner dimensions must match.
- In ML, a layer of a neural network is `output = activation(W @ x + b)` where W is a weight matrix.

**Why this matters in ML:**
- Features are vectors; a dataset is a matrix X of shape (n_samples, n_features).
- Linear regression solution: `β = (XᵀX)⁻¹ Xᵀy` — involves transpose and matrix inverse.
- Covariance matrices, PCA, and SVD all use matrix decompositions.
- Distance metrics (Euclidean, cosine similarity) are built from vector operations.

---

### 4) Differential Calculus

**Derivative intuition:**
- The derivative f′(x) is the instantaneous rate of change of f at x — the slope of the tangent line.
- If f′(x) > 0, f is increasing at x. If f′(x) < 0, f is decreasing.
- At a minimum: f′(x) = 0 and f″(x) > 0.

**Common derivatives to memorise:**

| Function f(x) | Derivative f′(x) |
|---|---|
| c (constant) | 0 |
| xⁿ | nxⁿ⁻¹ (power rule) |
| eˣ | eˣ |
| ln(x) | 1/x |
| sin(x) | cos(x) |

**Chain rule** (crucial for backpropagation):
```
d/dx [f(g(x))] = f′(g(x)) · g′(x)
```

**Gradient notes:**
- The **gradient** ∇f is a vector of partial derivatives — one per parameter.
- It always points in the direction of steepest *increase*.
- In ML we want to *minimise* the loss, so we move in the **negative gradient** direction.

**Gradient descent:**
```python
# Minimise f(x) = x² using gradient descent
# f'(x) = 2x

x = 10.0          # starting point
learning_rate = 0.1

for step in range(50):
    gradient = 2 * x          # derivative of x²
    x = x - learning_rate * gradient
    if step % 10 == 0:
        print(f"step {step}: x = {x:.4f}, f(x) = {x**2:.4f}")

# step 0: x = 8.0000, f(x) = 64.0000
# step 10: x = 1.0737, f(x) = 1.1528
# step 40: x = 0.0000, f(x) = 0.0000  ← converged to minimum
```

**Optimisation connections:**
- The loss function (e.g. MSE, cross-entropy) maps model parameters → a single error number.
- Backpropagation computes gradients of the loss w.r.t. every weight using the chain rule.
- **Learning rate:** too large → overshoots minimum; too small → training is very slow.
- **Stochastic Gradient Descent (SGD):** compute gradient on a random mini-batch instead of all data → faster and often better generalisation.

---

## Formula reference card

| Name | Formula | Used in |
|---|---|---|
| Mean | μ = Σxᵢ / n | Imputation, normalisation |
| Variance | σ² = Σ(xᵢ − μ)² / n | Feature scaling |
| Standard deviation | σ = √variance | Z-score, confidence intervals |
| Z-score | z = (x − μ) / σ | Outlier detection, normalisation |
| MSE | (1/n) Σ(yᵢ − ŷᵢ)² | Regression loss |
| RMSE | √MSE | Interpretable error in original units |
| Dot product | a · b = Σ aᵢbᵢ | Similarity, matrix mult |
| Gradient descent update | θ ← θ − α∇L | All neural networks |

---

## See also

- Previous: [07-Exploratory-Data-Analysis.md](07-Exploratory-Data-Analysis.md)
- Next: [09-Final-Portfolio.md](09-Final-Portfolio.md)
