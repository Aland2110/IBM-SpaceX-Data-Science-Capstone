# Exploratory Data Analysis — Observed Findings

These observations are based on six charts generated locally by running `src/spacex_eda.py` on IBM's Falcon 9 dataset (90 launches). The image files were reviewed in chat but have not yet been uploaded to this repository.

## Findings

1. **Flight Number vs Launch Site:** CCAFS SLC 40 has the densest sequence of launches; KSC LC 39A and VAFB SLC 4E also appear. Successful landings are more common among later flights.
2. **Payload Mass vs Launch Site:** All three sites serve a range of payload masses. Both successful and unsuccessful outcomes occur in overlapping mass ranges, so payload mass alone cannot determine the outcome.
3. **Landing Success Rate by Orbit:** The GEO, HEO, SSO and ES-L1 categories show a plotted success rate of 100%, but some categories have very few samples. GTO has a substantially lower plotted success rate, around 52%. **Small sample sizes limit interpretation of perfect scores.**
4. **Flight Number vs Orbit:** Later flights generally show more successful landing outcomes across several orbit categories.
5. **Payload Mass vs Orbit:** The GTO category has a broad range of payloads and mixed outcomes; VLEO includes some of the heaviest payloads shown.
6. **Annual Landing Success Trend:** Success starts at 0% for 2010–2013, increases to approximately 33% in 2014–2015, then rises to approximately 83% in 2017, 90% in 2019, and 84% in 2020. There are fluctuations, but the overall trend is upward.

## Verification status

The plotting script ran successfully in a Windows VS Code Python environment. The local console reported:
- `Saved six charts in figures/eda/`
- `Encoded feature dimensions: (90, 80)`
- `One-hot encoded features saved to dataset_part_3.csv`

**Note:** These 80 feature columns reflect the downloaded data and script run. Results can differ with other dataset versions. The six PNG files should be added under `figures/eda/` before the report is submitted.
