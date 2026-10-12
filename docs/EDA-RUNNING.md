# Running the SpaceX EDA analysis

The file `src/spacex_eda.py` implements the exploratory data visualization and feature-engineering steps based on the IBM capstone EDA lab.

## Requirements

Python 3.10+ with pandas, matplotlib, and seaborn.

```bash
python -m pip install pandas matplotlib seaborn
python src/spacex_eda.py
```

The script fetches IBM's public `dataset_part_2.csv`, generates six charts in `figures/eda/`, and saves encoded features as `dataset_part_3.csv`.

**Execution status:** Code has been published, but has **not** yet been verified against the remote dataset in this environment. No generated results should be inferred from its presence in the repository.

## Next steps

- Run script where the IBM dataset is accessible.
- Check the six charts and the printed feature dimensions.
- Add generated figures and executed notebooks.
- Complete SQL, Folium, Dash, and machine-learning analysis before submitting the final Capstone presentation.
