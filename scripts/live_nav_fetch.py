"""
live_nav_fetch.py

Purpose:
Fetches live NAV data from MFAPI and stores the results
in the raw data directory.

Author: R SHYAAM KRISHNAN
"""

import os
import requests
import pandas as pd

# Create data/raw folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Scheme names and their AMFI codes
schemes = {
    "hdfc_top100": "125497",
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_large_cap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

print("=" * 60)
print("Downloading Live NAV Data from mfapi.in")
print("=" * 60)

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Print scheme information
        print(f"\nScheme : {data['meta']['scheme_name']}")
        print(f"Fund House : {data['meta']['fund_house']}")
        print(f"AMFI Code : {code}")

        # Convert NAV history to DataFrame
        nav_df = pd.DataFrame(data["data"])

        # Save CSV
        filename = f"data/raw/{name}.csv"
        nav_df.to_csv(filename, index=False)

        print(f"Saved : {filename}")
        print(f"Total Records : {len(nav_df)}")

    except Exception as e:
        print(f"Failed to download {name}")
        print(e)

print("\n")
print("=" * 60)
print("All downloads completed.")
print("=" * 60)