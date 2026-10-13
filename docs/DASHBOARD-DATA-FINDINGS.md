# Plotly Dash data findings (IBM dataset)

The user-provided `spacex_launch_dash.csv` has **56 records** with launch site, booster version, payload mass, and landing class.

| Launch site | Successful class=1 | Records | Rate |
|---|---:|---:|---:|
| KSC LC-39A | 10 | 13 | 76.9% |
| CCAFS SLC-40 | 3 | 7 | 42.9% |
| VAFB SLC-4E | 4 | 10 | 40.0% |
| CCAFS LC-40 | 7 | 26 | 26.9% |

Across all sites, 24 of 56 records are `class=1` (42.9%). Static plots were generated from this actual CSV: launch-site success counts, all-site and selected-site pies, and a payload versus landing-outcome scatter grouped by booster category.

**Limitations:** These are analysis charts derived from dashboard data, not screenshots of an executed live Dash application. The machine-learning feature matrix `dataset_part_3.csv` is 90 rows and has no `Class` target labels. The full 90-row classifier comparison cannot be verified without the corresponding `dataset_part_2.csv` labels.
