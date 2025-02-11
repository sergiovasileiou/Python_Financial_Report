# Financial Ratios Analysis Project

## Overview

This project involves analyzing financial data provided in two Excel files (`Income_Statement.xlsx` and `Balance_Sheet.xlsx`). The goal is to compute key financial ratios and use them to generate insights for the manager. Specifically, the project focuses on calculating a leverage ratio and a profitability ratio, grouping these ratios by industry (denoted by the `comp_type` field), and then answering three specific questions regarding which company type exhibits the lowest profitability, the highest leverage, and the nature of the relationship between leverage and profitability for real estate companies.

## Data Files

- **Income_Statement.xlsx**  
  Contains income statement data, including:
  - Year
  - Company type (`comp_type`)
  - Company name (`company`)
  - Cost Of Goods Sold
  - Gross Profit
  - Operating Income
  - Total Operating Expenses
  - Total Revenue

- **Balance_Sheet.xlsx**  
  Contains balance sheet data, including:
  - Year
  - Company type (`comp_type`)
  - Company name (`company`)
  - Various balance sheet items such as Total Assets, Total Liabilities, and Total Stockholder Equity, among others

## Problem Description

The project requires you to perform the following tasks:

1. **Compute Financial Ratios:**
   - **Leverage Ratio:**  
     Use either:
     - **Debt-to-Equity Ratio:** \( \text{Debt-to-Equity Ratio} = \frac{\text{Total Liab}}{\text{Total Stockholder Equity}} \) 
     
     The computed value is stored in a column named `leverage_ratio` in a DataFrame called `df_ratios`.

   - **Profitability Ratio:**  
     Use either:
     - **Gross Margin Ratio:** \( \text{Gross Margin Ratio} = \frac{\text{Gross Profit}}{\text{Total Revenue}} \), or
     - **Operating Margin Ratio** (if preferred)  
     
     The computed value is stored in a column named `profitability_ratio` in the same `df_ratios` DataFrame.

2. **Answer the Following Questions:**
   - Which company type (`comp_type`) has the **lowest profitability ratio**? Save this value as a string in a variable called `lowest_profitability`.
   - Which company type has the **highest leverage ratio**? Save this value as a string in a variable called `highest_leverage`.
   - What is the relationship between leverage and profitability for **real estate** companies? Determine if the relationship is `"positive"`, `"negative"`, or `"no relationship"`, and store the result in a variable called `relationship`.

## Approach and Implementation Steps

### 1. Importing and Merging Data
- **Import** the required Excel files using `pandas.read_excel()`.
- **Merge** the `Income_Statement.xlsx` and `Balance_Sheet.xlsx` datasets on common keys, including `company`, `Year`, and `comp_type`, to ensure a complete dataset with both income and balance sheet measures.

### 2. Computing Financial Ratios
- **Leverage Ratio:**  
  Compute the ratio using the formula \( \text{Equity Multiplier} = \frac{\text{Total Assets}}{\text{Total Stockholder Equity}} \)
  
- **Profitability Ratio:**  
  Compute the ratio using the formula \( \text{Gross Margin Ratio} = \frac{\text{Gross Profit}}{\text{Total Revenue}} \) and add this as a new column named `profitability_ratio`.

### 3. Grouping and Analyzing Data by Company Type
- **Group** the data by the `comp_type` field using a pivot table to get the average leverage and profitability ratios for each company type.
- **Extract**:
  - The company type with the lowest average profitability ratio (stored in `lowest_profitability`).
  - The company type with the highest average leverage ratio (stored in `highest_leverage`).

### 4. Analyzing the Relationship for Real Estate Companies
- **Filter** the dataset for real estate companies (where `comp_type` is typically `"real_est"`).
- **Visualize** the relationship between leverage and profitability via a scatter plot with a regression line (using tools like Seaborn) to inspect the trend.
- **Compute** the Pearson correlation coefficient between the two ratios:
  - If the correlation coefficient is positive, the relationship is `"positive"`.
  - If negative, the relationship is `"negative"`.
  - If near zero, the relationship is `"no relationship"`.
- Store the result in the variable `relationship`.

### 5. Final Outputs
- The required outputs are stored in the following variables:
  - `lowest_profitability` – holds the company type with the lowest average profitability ratio.
  - `highest_leverage`    – holds the company type with the highest average leverage ratio.
  - `relationship`        – holds the qualitative relationship for real estate companies ("positive", "negative", or "no relationship").

![Screenshot 2025-02-11 162418](https://github.com/user-attachments/assets/f1fe9351-8425-4678-add3-d982f7481a9f)

## How to Run the Code

1. Ensure that you have Python installed, along with the required packages:
   - `pandas`
   - `matplotlib`
2. Place the provided Excel files (`Income_Statement.xlsx` and `Balance_Sheet.xlsx`) in the same directory as your script.
3. Run the Python script. The script will read the Excel files, merge the data, compute the ratios, produce the regression plot for real estate companies, and print out the final results.

## Conclusion

This project efficiently combines income and balance sheet data, computes critical financial ratios, and groups the results by industry to generate actionable insights. The analysis highlights which sectors demonstrate extreme leverage and profitability measures, as well as the relationship between these metrics among real estate companies.

