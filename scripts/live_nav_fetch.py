import requests
import pandas as pd

# ==========================================================
# Download NAV history for a single mutual fund scheme
# ==========================================================

scheme_code = 125497
url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print(data)

    nav = pd.DataFrame(data["data"])

    nav.to_csv(
        "data/raw/hdfc_top100_live_nav.csv",
        index=False
    )

    print("Single scheme NAV downloaded successfully.\n")

else:
    print("Failed to download data.")

# ==========================================================
# Download NAV history for multiple mutual fund schemes
# ==========================================================

codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

print("Downloading NAV history for multiple schemes...\n")

for code in codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav = pd.DataFrame(data["data"])

        nav.to_csv(
            f"data/raw/{code}.csv",
            index=False
        )

        print(f"{code} downloaded successfully.")

    else:
        print(f"{code} download failed.")

# ==========================================================
# Explore Fund Master Dataset
# ==========================================================

print("\n" + "=" * 60)
print("FUND MASTER DATASET")
print("=" * 60)

fund = pd.read_csv("data/raw/01_fund_master.csv")

print("\nDataset Shape")
print(fund.shape)

print("\nColumns")
print(fund.columns.tolist())

print("\nFund Houses")
print(fund["fund_house"].unique())

print("\nCategories")
print(fund["category"].unique())

print("\nSub Categories")
print(fund["sub_category"].unique())

print("\nRisk Categories")
print(fund["risk_category"].unique())

# ==========================================================
# Display basic information about downloaded NAV data
# ==========================================================

print("\n" + "=" * 60)
print("DOWNLOADED NAV DATA")
print("=" * 60)

print(nav.head())

print("\nColumns")
print(nav.columns.tolist())

print("\nDate Range")
print("Earliest Date :", nav["date"].min())
print("Latest Date   :", nav["date"].max())

print("\nTotal NAV Records")
print(len(nav))

print("\nScript completed successfully.")