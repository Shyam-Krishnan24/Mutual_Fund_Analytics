"""
run_pipeline.py

Runs the complete Mutual Fund Analytics pipeline.

Author: R SHYAAM KRISHNAN
"""

import subprocess
import sys

scripts = [
    "scripts/data_ingestion.py",
    "scripts/live_nav_fetch.py",
    "scripts/data_cleaning.py",
    "scripts/database_setup.py",
    "scripts/load_to_sqlite.py",
    "scripts/queries.py",
    "scripts/recommender.py"
]

print("=" * 60)
print("MUTUAL FUND ANALYTICS PIPELINE")
print("=" * 60)

for script in scripts:
    print(f"\nRunning {script}...\n")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\nError while executing {script}")
        sys.exit(1)

print("\n" + "=" * 60)
print("Pipeline executed successfully.")
print("=" * 60)