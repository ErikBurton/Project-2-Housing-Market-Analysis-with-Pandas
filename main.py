"""
Housing Market Analysis - Salt Lake County
Author: Erik Burton
"""

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description="Housing Market Analysis with Pandas")
    parser.add_argument("--csv", required=True, help="Path to the CSV file")
    parser.add_argument("--county-col", default="County", help="Column for county name")
    parser.add_argument("--county-name", default="Salt Lake County", help="County to filter")
    parser.add_argument("--city-col", default="City", help="Column for city/region")
    parser.add_argument("--year-col", default="Year", help="Column containing year (or parsed from date)")
    parser.add_argument("--date-col", default="ListingDate", help="Optional date column to derive year")
    parser.add_argument("--price-col", default="Price", help="Column for house price")
    parser.add_argument("--sqft-col", default="SqFt", help="Column for square footage")
    parser.add_argument("--outdir", default="outputs", help="Directory to save figures/CSVs")
    return parser.parse_args()


def load_dataset(path):
    try:
        df = pd.read_csv(path)
        print(f"[INFO] Loaded {len(df)} rows, {len(df.columns)} columns")
        return df
    except Exception as e:
        print(f"[ERROR] Could not load dataset: {e}")
        return pd.DataFrame()
