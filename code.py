import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Import datasets
income_statement = pd.read_excel('Income_Statement.xlsx', sheet_name='Sheet1')
balance_sheet = pd.read_excel('Balance_Sheet.xlsx', sheet_name='Sheet1')

# Step 2: Merge the data on common keys.
# Including 'comp_type' in the merge key ensures that we do not end up with duplicate comp_type columns.
df = pd.merge(income_statement, balance_sheet, on=['company', 'Year', 'comp_type'])

# Step 3: Compute Financial Ratios
# Leverage ratio: using the equity multiplier method: Total Assets / Total Stockholder Equity
df['leverage_ratio'] = df['Total Assets'] / df['Total Stockholder Equity']

# Profitability ratio: using the gross margin ratio: Gross Profit / Total Revenue
df['profitability_ratio'] = df['Gross Profit'] / df['Total Revenue']

# Create a new DataFrame for the ratios
df_ratios = df[['company', 'comp_type', 'leverage_ratio', 'profitability_ratio']]

# Step 4: Group Average Ratios by Company Type
# Using pivot_table to compute average ratios for each comp_type
avg_ratios = df_ratios.pivot_table(values=['leverage_ratio', 'profitability_ratio'],
                                   index='comp_type',
                                   aggfunc='mean').reset_index()

# Identify the company type with the lowest average profitability ratio.
lowest_profitability = avg_ratios.loc[avg_ratios['profitability_ratio'].idxmin(), 'comp_type']

# Identify the company type with the highest average leverage ratio.
highest_leverage = avg_ratios.loc[avg_ratios['leverage_ratio'].idxmax(), 'comp_type']

# Step 5: Analyze Relationship Between Leverage and Profitability in Real Estate Companies
# Filter the dataset for real estate companies; note that 'real_est' is used as the comp_type value.
df_real_est = df_ratios[df_ratios['comp_type'] == 'real_est']

# Create a regression plot to visually inspect the relationship.
sns.regplot(x='leverage_ratio', y='profitability_ratio', data=df_real_est)
plt.title('Leverage vs Profitability in Real Estate Companies')
plt.xlabel('Leverage Ratio')
plt.ylabel('Profitability Ratio')
plt.show()

# Compute the Pearson correlation coefficient between the ratios.
correlation = df_real_est[['leverage_ratio', 'profitability_ratio']].corr().iloc[0, 1]

# Determine the nature of the relationship based on the correlation coefficient.
if correlation > 0:
    relationship = "positive"
elif correlation < 0:
    relationship = "negative"
else:
    relationship = "no relationship"

# Final outputs: variables for lowest profitability company type, highest leverage company type,
# and the qualitative relationship between leverage and profitability for real estate companies.

print("Lowest Profitability Company Type:", lowest_profitability)
print("Highest Leverage Company Type:", highest_leverage)
print("Relationship between Leverage and Profitability in Real Estate:", relationship)
