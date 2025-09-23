"""
Salt Lake County Housing Market Analysis
Author: Erik Burton
Description:
    Analyze Utah real estate data (2024) with Pandas + Matplotlib.
    Focuses on Salt Lake County dataset fields:
        - listPrice (Price)
        - sqft (Square footage)
        - lastSoldOn (Date of sale)
        - year_built (Year house was built)

    Questions:
        1. What is the average price by year built?
        2. How have average prices changed over sale years?
        3. Scatter plot: price vs. square footage
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


# ---------- Load & Clean ----------

def load_dataset(csv_path: str) -> pd.DataFrame:
    """Load the housing dataset into a DataFrame."""
    try:
        df = pd.read_csv(csv_path)
        print(f"[INFO] Loaded dataset: {csv_path} with {len(df):,} rows")
        return df
    except Exception as e:
        print(f"[ERROR] Could not load dataset: {e}")
        return pd.DataFrame()


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Convert data types and drop missing price values."""
    # Ensure numeric fields
    df["listPrice"] = pd.to_numeric(df["listPrice"], errors="coerce")
    df["sqft"] = pd.to_numeric(df["sqft"], errors="coerce")
    df["year_built"] = pd.to_numeric(df["year_built"], errors="coerce")

    # Parse dates
    df["lastSoldOn"] = pd.to_datetime(df["lastSoldOn"], errors="coerce")

    before = len(df)
    df = df.dropna(subset=["listPrice", "sqft", "lastSoldOn"])
    after = len(df)
    print(f"[INFO] Dropped {
        before - after} invalid rows. Remaining: {after:,}")
    return df


# ---------- Analyses ----------

def avg_price_by_year_built(df: pd.DataFrame) -> pd.DataFrame:
    """Average price by year built."""
    result = (
        df.groupby("year_built")["listPrice"]
        .mean()
        .reset_index(name="AveragePrice")
        .sort_values("year_built")
    )
    print("[RESULT] Avg Price by Year Built (first 10 rows):")
    print(result.head(10))
    return result


def avg_price_by_sale_year(df: pd.DataFrame) -> pd.DataFrame:
    """Average price by sale year (from lastSoldOn)."""
    df["SaleYear"] = df["lastSoldOn"].dt.year
    result = (
        df.groupby("SaleYear")["listPrice"]
        .mean()
        .reset_index(name="AveragePrice")
        .sort_values("SaleYear")
    )

    if not result.empty:
        max_year = result["SaleYear"].max()
        min_year = max_year - 19
        result = result[result["SaleYear"].between(min_year, max_year)]

    print("[RESULT] Avg Price by Sale Year (last 20 years):")
    print(result)
    return result


# ---------- Plots ----------

def plot_price_trend(trends: pd.DataFrame, outdir: str):
    """Line chart of avg price by sale year."""
    path = os.path.join(outdir, "price_trend.png")
    plt.figure(figsize=(8, 5))
    plt.plot(trends["SaleYear"], trends[
        "AveragePrice"], marker="o", color="blue")
    plt.title("Average Housing Price Over Sale Years")
    plt.xlabel("Year")
    plt.ylabel("Average Price ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    print(f"[SAVE] {path}")


def plot_price_vs_sqft(df: pd.DataFrame, outdir: str):
    """Scatter plot of price vs. square footage."""
    path = os.path.join(outdir, "price_vs_sqft.png")
    plt.figure(figsize=(8, 5))
    plt.scatter(df["sqft"], df["listPrice"], alpha=0.5, color="green")
    plt.title("Price vs. Square Feet")
    plt.xlabel("Square Feet")
    plt.ylabel("Price ($)")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    print(f"[SAVE] {path}")


# ---------- Main ----------

def main():
    data_path = "data/real_estate_utah_2024.csv"
    outdir = "outputs"
    os.makedirs(outdir, exist_ok=True)

    df = load_dataset(data_path)
    if df.empty:
        return
    df = clean_dataset(df)

    # Q1: Average price by year built
    avg_by_year_built = avg_price_by_year_built(df)
    avg_by_year_built.to_csv(
        os.path.join(outdir, "avg_price_by_year_built.csv"), index=False)

    # Q2: Average price by sale year
    avg_by_sale_year = avg_price_by_sale_year(df)
    avg_by_sale_year.to_csv(
        os.path.join(outdir, "avg_price_by_sale_year.csv"), index=False)

    # Graphs
    plot_price_trend(avg_by_sale_year, outdir)
    plot_price_vs_sqft(df, outdir)


if __name__ == "__main__":
    main()
