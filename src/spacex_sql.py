"""IBM SpaceX Capstone: EDA with SQLite (10 assignment tasks).

Run from your project folder:
    python spacex_sql.py

Dependencies: pandas
Needs internet access to download IBM's SpaceX.csv.
Outputs: outputs/sql/*.csv and outputs/sql/sql_results.txt
"""
from pathlib import Path
import sqlite3
import pandas as pd

DATA_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv"
)
OUT_DIR = Path("outputs/sql")
OUT_DIR.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA_URL)
df = df[df["Date"].notna()].copy()

queries = [
    ("01_unique_launch_sites", """
        SELECT DISTINCT "Launch_Site" FROM SPACEXTABLE ORDER BY "Launch_Site";
    """),
    ("02_five_ccafs_launch_records", """
        SELECT * FROM SPACEXTABLE
        WHERE "Launch_Site" LIKE 'CCA%' LIMIT 5;
    """),
    ("03_nasa_crs_payload_mass", """
        SELECT SUM("PAYLOAD_MASS__KG_") AS "Total_Payload_Mass_kg"
        FROM SPACEXTABLE WHERE "Customer" LIKE '%NASA (CRS)%';
    """),
    ("04_f9_v11_average_payload", """
        SELECT AVG("PAYLOAD_MASS__KG_") AS "Average_Payload_Mass_kg"
        FROM SPACEXTABLE WHERE "Booster_Version" = 'F9 v1.1';
    """),
    ("05_first_ground_pad_landing", """
        SELECT MIN("Date") AS "First_Successful_Ground_Pad_Landing"
        FROM SPACEXTABLE WHERE "Landing_Outcome" = 'Success (ground pad)';
    """),
    ("06_successful_drone_ship_boosters", """
        SELECT DISTINCT "Booster_Version"
        FROM SPACEXTABLE
        WHERE "Landing_Outcome" = 'Success (drone ship)'
        AND "PAYLOAD_MASS__KG_" > 4000
        AND "PAYLOAD_MASS__KG_" < 6000;
    """),
    ("07_mission_outcome_counts", """
        SELECT "Mission_Outcome", COUNT(*) AS "Mission_Count"
        FROM SPACEXTABLE GROUP BY "Mission_Outcome"
        ORDER BY "Mission_Count" DESC;
    """),
    ("08_boosters_with_maximum_payload", """
        SELECT DISTINCT "Booster_Version", "PAYLOAD_MASS__KG_"
        FROM SPACEXTABLE
        WHERE "PAYLOAD_MASS__KG_" = (
            SELECT MAX("PAYLOAD_MASS__KG_") FROM SPACEXTABLE
        );
    """),
    ("09_drone_ship_failures_2015", """
        SELECT SUBSTR("Date", 6, 2) AS "Month",
               "Date", "Landing_Outcome", "Booster_Version", "Launch_Site"
        FROM SPACEXTABLE
        WHERE "Landing_Outcome" = 'Failure (drone ship)'
          AND SUBSTR("Date", 1, 4) = '2015'
        ORDER BY "Date";
    """),
    ("10_ranked_landing_outcomes", """
        SELECT "Landing_Outcome", COUNT(*) AS "Outcome_Count"
        FROM SPACEXTABLE
        WHERE DATE("Date") BETWEEN DATE('2010-06-04') AND DATE('2017-03-20')
        GROUP BY "Landing_Outcome"
        ORDER BY "Outcome_Count" DESC;
    """),
]

with sqlite3.connect(":memory:") as con:
    df.to_sql("SPACEXTABLE", con, index=False, if_exists="replace")
    with (OUT_DIR / "sql_results.txt").open("w", encoding="utf-8") as summary:
        for title, sql in queries:
            result = pd.read_sql_query(sql, con)
            result.to_csv(OUT_DIR / f"{title}.csv", index=False)
            section = f"\n{'=' * 70}\n{title}\n{'=' * 70}\n{result.to_string(index=False)}\n"
            print(section)
            summary.write(section)

print(f"\nDONE: {len(queries)} queries executed against {len(df)} dataset rows.")
print(f"Saved results to: {OUT_DIR.resolve()}")
