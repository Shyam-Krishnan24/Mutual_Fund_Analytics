from pathlib import Path
import pandas as pd
# ==========================================================
# Project Paths
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed"
csv_path = DATA_PATH / "clean_scheme_performance.csv"
# ==========================================================
# Load Dataset
# ==========================================================
performance = pd.read_csv(csv_path)
# ==========================================================
# User Input
# ==========================================================

print("=" * 60)
print("MUTUAL FUND RECOMMENDATION SYSTEM")
print("=" * 60)
print("\nSelect Risk Appetite")
print("1. Low")
print("2. Moderate")
print("3. High")
choice = input("\nEnter your choice: ")
risk_mapping = {
    "1": "Low",
    "2": "Moderate",
    "3": "High"
}
if choice not in risk_mapping:
    print("\nInvalid choice!")
    exit()
selected_risk = risk_mapping[choice]
print(f"\nSelected Risk Appetite : {selected_risk}")
# ==========================================================
# Filter Funds
# ==========================================================
recommended = performance[
    performance["risk_grade"].str.strip().str.lower()
    == selected_risk.lower()
]
# ==========================================================
# Sort by Sharpe Ratio
# ==========================================================
recommended = recommended.sort_values(
    by="sharpe_ratio",
    ascending=False
)
top3 = recommended.head(3)

# ==========================================================
# Display Recommendations
# ==========================================================

print("\nTop 3 Recommended Funds")
print("=" * 60)
if top3.empty:
    print("No matching funds found.")
else:
    print(
        top3[
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct",
                "return_5yr_pct"
            ]
        ].to_string(index=False)
    )