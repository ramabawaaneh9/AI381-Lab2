# Model Selection

## The question

This model predicts whether a customer is likely to leave a telecom company (customer churn). Wrong predictions may cause the company to lose customers or waste resources on unnecessary retention offers.

## Candidates

| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |
|---|---|---|---|---|---|---|---|
| Logistic Regression | Simple, fast baseline model | 0.792 | 0.587 | 0.182 (two-year) | 9.761 | 3.532 | 3074958b... |
| Random Forest | Tests a more complex ensemble model | 0.725 | 0.520 | 0.000 (two-year) | 24.55 | 3427.1 | aa483bd0... |
| Gradient Boosting | Tests sequential boosting to improve predictions | 0.731 | 0.531 | 0.182 (two-year) | 14.34 | 141.2 | 7e17eef5... |

## The champion

I selected **Logistic Regression** as the champion because it achieved the highest overall F1 score (0.587) and AUC (0.792).

It also had the lowest p95 latency (9.761 ms) and the smallest model size (3.532 KB).

The trade-off is that its F1 score for one-year contracts (0.375) was slightly lower than Random Forest and Gradient Boosting (0.400).

I accepted this trade-off because Logistic Regression performed better overall and was faster and smaller.

## My promotion rules

- **Latency budget (p95): 50 ms**, because the service should provide fast predictions while allowing some performance variation between my laptop and GitHub Actions runners.

- **Minimum gain to replace the champion (F1 points): 0.01**, because a new model should improve F1 by at least one percentage point in absolute terms before replacing the existing champion. This avoids promoting models for very small improvements.

## What I would check next

I would investigate the low F1 scores for customers with two-year contracts. I would check whether this group contains enough churn examples and monitor performance as customer behavior changes in production.