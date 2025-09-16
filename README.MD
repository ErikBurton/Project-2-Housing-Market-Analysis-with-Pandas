# Housing Market Analysis with Pandas

## Overview
This project analyzes a housing dataset using **Python, Pandas, and Matplotlib**.  
The focus is on understanding housing price trends across cities and over time,  
and exploring the relationship between house size and price.

---

## Dataset
- **Source**: [Kaggle Housing Dataset](https://www.kaggle.com/)  
- **Description**: Dataset includes housing prices, location (city/region), size in square feet, and year built/sold.  
- **Reason for Selection**: Housing data is well-documented and provides clear opportunities for aggregation and visualization.  

---

## Questions Answered
1. **Question 1**: What is the **average housing price per city/region**?  
   - **Method**: Used `groupby('City')` with `mean()`.  
   - **Result**: Provided a ranked list of average prices.  

2. **Question 2**: How have **housing prices changed over time**?  
   - **Method**: Grouped by year, calculated mean, and sorted chronologically.  
   - **Result**: Clear trend showing price increases/decreases over years.  

3. **Additional Requirement (Graph)**:  
   - A **line chart** of average house price over time.  
   - A **scatter plot** of price vs. square feet, showing size-to-price relationship.  

*(Insert screenshots of charts here)*  

---

## Development Environment
- **Language**: Python 3.x  
- **Libraries**: Pandas, Matplotlib  
- **Tools**: VS Code, Git, GitHub  
- **Install**:  
```bash
pip install pandas matplotlib
