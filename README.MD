# Overview

As a software engineer, I am using this project to strengthen my skills in data analysis, data cleaning, and visualization using Python.  
The dataset analyzed comes from Kaggle: **[Real Estate Data Utah 2024](https://www.kaggle.com/datasets/kanchana1990/real-estate-data-utah-2024)**.  
It contains over 4,400 real estate listings across Utah, including fields such as `year_built`, `beds`, `baths`, `sqft`, `lastSoldOn`, `listPrice`, and more.  

For this project, I focused on answering questions related to **housing trends in Salt Lake County**, using `listPrice` (price), `sqft` (square footage), `lastSoldOn` (sale date), and `year_built` (year constructed).  

The purpose of this software is to uncover patterns in the housing market, such as how home prices vary depending on when they were built, how they’ve changed over time, and the relationship between home size and price. This demonstrates how to use Pandas for filtering, grouping, and aggregating data, along with Matplotlib for visualizations.  

[Software Demo Video](http://youtube.link.goes.here)

---

# Data Analysis Results

The following questions were asked and answered from the dataset (Salt Lake County):  

1. **What is the average housing price by year built?**  
   - *Method:* Grouped by `year_built` and calculated the mean of `listPrice`.  
   - *Result:* Homes built before 1950 generally showed lower average prices, reflecting smaller size and fewer modern features. Properties constructed after 2000 tended to command significantly higher values, with average prices increasing steadily for newer builds. This trend confirms that newer construction typically adds value in the Salt Lake County market.  

2. **How have housing prices changed over sale years (last 20 years)?**  
   - *Method:* Converted `lastSoldOn` into `SaleYear`, calculated average `listPrice` per year, and filtered to the last 20 years (2005–2024).  
   - *Result:* Average home prices showed consistent growth during this period, with notable acceleration after 2015. In 2023, the average home price was approximately **$749,000**, rising to about **$850,000** in 2024. This reflects the strong upward trend in the Salt Lake County housing market over the last two decades.  

3. **What is the relationship between house size (square feet) and price?**  
   - *Method:* Scatter plot comparing `sqft` vs. `listPrice`.  
   - *Result:* Larger homes generally sell for higher prices, though several outliers exist where smaller homes achieved premium prices, likely due to location, luxury features, or recent renovations. This reinforces that square footage is an important driver of price, but not the only factor in home valuation.  

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
