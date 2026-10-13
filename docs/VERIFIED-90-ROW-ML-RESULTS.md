# Verified 90-row machine-learning evaluation

The matching IBM datasets `dataset_part_2.csv` (90 labeled rows) and `dataset_part_3.csv` (90 rows, 80 encoded features) were supplied by the project owner. We paired them by original row order.

**Method:** 80/20 stratified train/test split (`random_state=42`): 72 train, 18 test. Model hyperparameters selected using stratified five-fold GridSearchCV on training data only. Numeric features standardized inside pipelines for Logistic Regression, SVM and KNN.

| Classifier | Best validation accuracy | Held-out test accuracy |
|---|---:|---:|
| Logistic Regression | 83.43% | **83.33% (15/18)** |
| Decision Tree | 84.57% | 77.78% (14/18) |
| K-Nearest Neighbors | 77.90% | 77.78% (14/18) |
| Support Vector Machine | 84.86% | 66.67% (12/18) |

Best held-out result was Logistic Regression. However **SVM was the top cross-validation classifier**; test accuracy should not be used for hyperparameter/model selection in operational deployment. The model comparison and confusion matrix were generated programmatically and included in the latest PDF report.

**Reproducibility:** Full source script `spacex_ml.py` can be run locally after replacing its remote CSV URLs with the downloaded paths if IBM hosting is unavailable. Different random splits or tuning grids can yield different results. The data is small and historical.

**Status:** These are verified evaluations using the full 90-row IBM feature dataset, not the separate 56-row dashboard/mapping dataset.
