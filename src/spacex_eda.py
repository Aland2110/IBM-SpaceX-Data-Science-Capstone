"""SpaceX Falcon 9 exploratory visualizations based on IBM's capstone EDA lab.

Run: python src/spacex_eda.py
Requires: pandas, matplotlib, seaborn
This script downloads the IBM dataset at runtime; an internet connection is required.
Charts will be saved under figures/eda/.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
OUT = Path("figures/eda")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_URL)
required = {"FlightNumber", "PayloadMass", "LaunchSite", "Orbit", "Class", "Date"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

sns.set_theme(style="whitegrid")

def categorical_scatter(x, y, title, filename):
    chart = sns.catplot(data=df, x=x, y=y, hue="Class", kind="strip",
                        aspect=2.1, height=5, jitter=True)
    chart.fig.suptitle(title, y=1.03)
    chart.savefig(OUT / filename, dpi=160, bbox_inches="tight")
    plt.close(chart.fig)

# Lab tasks 1 and 2: launch-site relationships
categorical_scatter("FlightNumber", "LaunchSite",
                    "Flight Number vs. Launch Site", "01_flight_vs_site.png")
categorical_scatter("PayloadMass", "LaunchSite",
                    "Payload Mass vs. Launch Site", "02_payload_vs_site.png")

# Lab task 3: average success rate per orbit
orbit_success = (df.groupby("Orbit", as_index=False)["Class"]
                   .mean().sort_values("Class", ascending=False))
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=orbit_success, x="Orbit", y="Class", ax=ax)
ax.set(title="Landing Success Rate by Orbit", xlabel="Orbit",
       ylabel="Success rate", ylim=(0, 1))
fig.tight_layout()
fig.savefig(OUT / "03_success_by_orbit.png", dpi=160)
plt.close(fig)

# Lab tasks 4 and 5: orbit relationships
categorical_scatter("FlightNumber", "Orbit",
                    "Flight Number vs. Orbit", "04_flight_vs_orbit.png")
categorical_scatter("PayloadMass", "Orbit",
                    "Payload Mass vs. Orbit", "05_payload_vs_orbit.png")

# Lab task 6: annual landing success trend
df["Year"] = pd.to_datetime(df["Date"]).dt.year
annual = df.groupby("Year", as_index=False)["Class"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=annual, x="Year", y="Class", marker="o", ax=ax)
ax.set(title="Annual Falcon 9 First-Stage Landing Success Rate",
       xlabel="Year", ylabel="Success rate", ylim=(0, 1))
fig.tight_layout()
fig.savefig(OUT / "06_annual_success.png", dpi=160)
plt.close(fig)

# Lab tasks 7 and 8: encode categories, then cast to float64
feature_cols = ["FlightNumber", "PayloadMass", "Orbit", "LaunchSite",
                "Flights", "GridFins", "Reused", "Legs", "LandingPad",
                "Block", "ReusedCount", "Serial"]
features = df[feature_cols].copy()
features_one_hot = pd.get_dummies(
    features,
    columns=["Orbit", "LaunchSite", "LandingPad", "Serial"],
    dtype=float,
).astype("float64")
features_one_hot.to_csv("dataset_part_3.csv", index=False)
print(f"Saved six charts in {OUT}/")
print(f"Encoded feature dimensions: {features_one_hot.shape}")
print("One-hot encoded features saved to dataset_part_3.csv")
