# Housing Market Analysis with Pandas

## Overview

As a software engineer, I am using this project to strengthen my skills in data analysis, data cleaning, and visualization using Python.  
The dataset analyzed comes from Kaggle: **[Real Estate Data Utah 2024](https://www.kaggle.com/datasets/kanchana1990/real-estate-data-utah-2024)**.  
It contains over 4,000 real estate listings across Utah, including key fields such as `County`, `City`, `Price`, `SqFt`, `Bedrooms`, `Bathrooms`, and `ListingDate`.  

For this project, I focused on **Salt Lake County** specifically, filtering the dataset to analyze housing trends in this area.  

The purpose of this software is to uncover patterns in the Salt Lake County housing market, including average prices by city, price trends over time, and the relationship between house size and price. This analysis demonstrates how to use Pandas for filtering, grouping, and aggregating data, along with Matplotlib for visualizations.  

[Software Demo Video](http://youtube.link.goes.here)

---

# Data Analysis Results

The following questions were asked and answered from the dataset (Salt Lake County only):  

1. **What is the average housing price per city in Salt Lake County?**  
   - *Method:* Used `groupby("City")` with `mean("Price")`.  
   - *Result:* (Insert your top 5–10 cities with average prices here after running code.)  

2. **How have housing prices in Salt Lake County changed over time?**  
   - *Method:* Derived year from `ListingDate`, grouped by year, calculated average price.  
   - *Result:* (Insert summary of trend here; e.g., prices steadily increased since 2018 with a peak in 2022.)  

3. **What is the relationship between house size (square feet) and price?**  
   - *Method:* Scatter plot comparing `SqFt` vs. `Price`.  
   - *Result:* (Summarize correlation; e.g., larger homes tend to cost more, but with some high-priced outliers.)  

---

# Development Environment

- **Tools**: Visual Studio Code, Git, GitHub  
- **Programming Language**: Python 3.x  
- **Libraries**:  
  - [Pandas](https://pandas.pydata.org/) – data manipulation and analysis  
  - [Matplotlib](https://matplotlib.org/) – data visualization  

To install dependencies:  
```bash
pip install -r requirements.txt

