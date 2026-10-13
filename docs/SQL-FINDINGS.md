# SQL Exploratory Analysis — Executed Results

Source: User's executed local `spacex_sql.py` output, IBM SpaceX launch SQL dataset, **101 rows**. The SQL queries and output CSVs were generated locally in VS Code.

## Key findings

| Analysis | Executed result |
|---|---|
| Unique launch sites | CCAFS LC-40; CCAFS SLC-40; KSC LC-39A; VAFB SLC-4E |
| NASA (CRS) total payload mass | **48,213 kg** |
| Average payload mass for booster F9 v1.1 | **2,928.4 kg** |
| First successful ground-pad landing | **2015-12-22** |
| Maximum recorded payload mass | **15,600 kg** (shared by several Falcon 9 Block 5 boosters) |
| Successful drone-ship landings with payload 4,000–6,000 kg | F9 FT B1022, F9 FT B1026, F9 FT B1021.2, F9 FT B1031.2 |
| Drone-ship landing failures during 2015 | **2015-01-10** (F9 v1.1 B1012) and **2015-04-14** (F9 v1.1 B1015), both at CCAFS LC-40 |

### Mission outcomes as exported

| Raw mission-outcome label | Count |
|---|---:|
| Success | 98 |
| Success (payload status unclear) | 1 |
| Success *(likely padded/whitespace variant)* | 1 |
| Failure (in flight) | 1 |

**Data-quality note:** The exported summary includes two visibly identical `Success` labels with counts 98 and 1. They likely differ by trailing whitespace. They should be normalized (e.g. `TRIM(Mission_Outcome)`) before calculating definitive category counts.

### Landing-outcome counts for 2010-06-04 through 2017-03-20

| Landing outcome | Count |
|---|---:|
| No attempt | 10 |
| Success (drone ship) | 5 |
| Failure (drone ship) | 5 |
| Success (ground pad) | 3 |
| Controlled (ocean) | 3 |
| Uncontrolled (ocean) | 2 |
| Failure (parachute) | 2 |
| Precluded (drone ship) | 1 |

### Five launch records beginning with CCA

The first five filtered records in the executed output span **2010-06-04 to 2013-03-01**, all at **CCAFS LC-40**, with payload masses of **0, 0, 525, 500, and 677 kg**.

## Reproduction

Run `python src/spacex_sql.py` from the project directory. This downloads IBM's publicly hosted dataset and produces 10 CSV reports and an aggregate `outputs/sql/sql_results.txt` file.

This document transcribes the locally executed results provided by the project owner. SQL queries are published in `src/spacex_sql.py`. The detailed CSV results still need to be uploaded to the repository.
