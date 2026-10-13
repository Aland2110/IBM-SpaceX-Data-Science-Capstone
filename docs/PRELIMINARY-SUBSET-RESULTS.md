# Preliminary dashboard and classification evidence (subset)

The analysis in the accompanying report appendix uses **56 launch records** pasted from the IBM geography dataset. It is distinct from the official **90-row** classification dataset and **101-row** SQL dataset.

## Observed site statistics

| Site | class=1 | Records | Rate |
|---|---:|---:|---:|
| CCAFS LC-40 | 7 | 26 | 26.9% |
| CCAFS SLC-40 | 3 | 7 | 42.9% |
| KSC LC-39A | 10 | 13 | 76.9% |
| VAFB SLC-4E | 4 | 10 | 40.0% |

## Preliminary classification benchmark

Predictors: Flight Number and one-hot encoded Launch Site. Stratified 44/12 train/test split with random_state 42, and three-fold cross-validation on training data.

| Model | CV accuracy | Held-out accuracy |
|---|---:|---:|
| Logistic Regression | 66.0% | 58.3% |
| SVM | 68.4% | 66.7% |
| Decision Tree | 79.5% | 75.0% |
| KNN | 68.4% | 66.7% |

Decision Tree is selected by its cross-validation accuracy. Its held-out accuracy of 75.0% corresponds to 9 correct predictions among 12 test records.

**Limitations:** The short subset omits later launches, and omits payload mass, orbit, booster reuse and other predictors. The mapping dataset also contains a class label that appears inconsistent with its landing-outcome description. Site-specific rates are heavily influenced by sample composition. These values **must not be presented as official full-dataset IBM machine-learning scores**. The all-site pie and site success rate charts are static derived figures, not screenshots of a live Plotly Dash application.

The full-dataset Dashboard and ML scripts were separately prepared but have not yet been run against their public IBM CSV sources. The final report still requires official full-dataset dashboard screenshots, full-feature classifier evaluation, and a validated proximity map before it should be treated as fully complete.
