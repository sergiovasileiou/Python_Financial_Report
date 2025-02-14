# 📊 Financial Ratios Analysis Project

## 👨‍💻 **Author**  
Sergios Vasileiou

## 🔎 Overview

This project involves analyzing financial data from two Excel files: **Income_Statement.xlsx** and **Balance_Sheet.xlsx**. The goal is to compute key financial ratios, group them by industry (using the `comp_type` field), and answer specific business questions. The analysis focuses on identifying:

- The company type with the lowest profitability ratio.
- The company type with the highest leverage ratio.
- The relationship between leverage and profitability for real estate companies.

## 🔑 Key Features

- **Data Files**:  
  - *Income_Statement.xlsx*: Contains income statement data such as `Gross Profit`, `Total Revenue`, and `Operating Income`.  
  - *Balance_Sheet.xlsx*: Includes balance sheet data such as `Total Assets`, `Total Liabilities`, and `Total Stockholder Equity`.

- **Financial Ratios Computed**:  
  - **Leverage Ratio**:  
    Computed as the Debt-to-Equity ratio:  
    \[
    \text{Debt-to-Equity Ratio} = \frac{\text{Total Liabilities}}{\text{Total Stockholder Equity}}
    \]
    This value is stored in a column named `leverage_ratio`.  

  - **Profitability Ratio**:  
    Computed as the Gross Margin Ratio:  
    \[
    \text{Gross Margin Ratio} = \frac{\text{Gross Profit}}{\text{Total Revenue}}
    \]
    This value is stored in a column named `profitability_ratio`.

- **Insights Generated**:  
  - Identification of the company type with the lowest average profitability ratio (stored in `lowest_profitability`).
  - Determination of the company type with the highest average leverage ratio (stored in `highest_leverage`).
  - Analysis of the relationship between leverage and profitability for real estate companies, evaluated using Pearson's correlation coefficient and stored in `relationship` as "positive", "negative", or "no relationship".

## 🛠️ Technologies Used

- **Python**
- **pandas**: For data manipulation and merging.
- **matplotlib** & **seaborn**: For data visualization.

## 🏁 Getting Started

1. **Data Import and Merging**:  
   - Use `pandas.read_excel()` to import the Excel files.  
   - Merge the datasets on `Year`, `Company`, and `comp_type` to create a complete dataset with both income and balance sheet measures.

2. **Computing Financial Ratios**:  
   - **Leverage Ratio**: Compute using the Debt-to-Equity formula.  
   - **Profitability Ratio**: Compute using the Gross Margin formula.

3. **Grouping and Analysis by Industry**:  
   - Group the merged data by the `comp_type` field using a pivot table to calculate average ratios for each company type.
   - Extract the key insights:
     - `lowest_profitability`: The company type with the lowest average profitability ratio.
     - `highest_leverage`: The company type with the highest average leverage ratio.

4. **Analyzing Real Estate Companies**:  
   - Filter the dataset where `comp_type` is "real_est".  
   - Visualize the relationship between leverage and profitability using a scatter plot with a regression line.  
   - Compute the Pearson correlation coefficient to determine the relationship:
     - If positive, the relationship is "positive".
     - If negative, the relationship is "negative".
     - If near zero, the relationship is "no relationship".
   - Store this result in the variable `relationship`.

5. **Final Outputs**:  
   - The project stores the computed key outputs in the variables:
     - `lowest_profitability`
     - `highest_leverage`
     - `relationship`
       
![Screenshot 2025-02-11 162418](https://github.com/user-attachments/assets/f1fe9351-8425-4678-add3-d982f7481a9f)

## 🚀 How to Run the Code

1. **Environment Setup**:  
   Ensure that Python and the required libraries (`pandas`, `matplotlib`, and `seaborn`) are installed. Install them via pip if necessary:

2. **File Preparation**:  
Place **Income_Statement.xlsx** and **Balance_Sheet.xlsx** in the same directory as your Python script.

3. **Execute the Script**:  
Run your Python script. The script will:
- Read and merge the data.
- Compute the financial ratios.
- Generate the regression plot for real estate companies.
- Print out the final insights.

## 📈 Conclusion

This project effectively integrates an income statement and a balance sheet data to ucnover critical financial ratios and generate actionable insights by industry. It highlights which sectors exhibit extreme leverage and profitability but also explores the dynamic relationship between these metrics. Such analysis provides managers with valuable information for informed decision-making.
