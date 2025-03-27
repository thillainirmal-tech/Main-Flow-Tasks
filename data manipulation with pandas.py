import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('your_dataset.csv')  # Replace with your dataset path

# Display basic info
print("Basic Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

### 1. Data Cleaning and Handling Missing Data ###
# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Fill missing values
df['column_name'] = df['column_name'].fillna(df['column_name'].mean())  # Replace 'column_name' with actual column name

# Drop rows with any missing values
df.dropna(inplace=True)

### 2. Data Transformation ###
# Creating new columns
df['new_column'] = df['existing_column1'] * df['existing_column2']  # Example of creating a derived column

# Converting data types
df['column_name'] = df['column_name'].astype(float)

# Grouping data and calculating aggregate statistics
grouped_df = df.groupby('category_column')['numeric_column'].sum()  # Replace 'category_column' and 'numeric_column'

print("\nGrouped Data Summary:")
print(grouped_df)

### 3. Data Filtering and Sorting ###
# Filtering data
filtered_df = df[(df['column1'] > 50) & (df['column2'] == 'specific_value')]  # Replace with your conditions

# Sorting data
sorted_df = df.sort_values(by='numeric_column', ascending=False)

print("\nTop Entries After Sorting:")
print(sorted_df.head())

### 4. Advanced Data Visualization ###
# Set up Seaborn style
sns.set(style="whitegrid")

# Histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['numeric_column'], kde=True, color='skyblue')
plt.title("Distribution of Numeric Column")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Box plot for outlier detection
plt.figure(figsize=(8, 6))
sns.boxplot(x='category_column', y='numeric_column', data=df)
plt.title("Box Plot of Numeric Column by Category")
plt.xlabel("Category")
plt.ylabel("Numeric Column Value")
plt.show()

# Heatmap for correlation matrix
plt.figure(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='numeric_column1', y='numeric_column2', data=df, scatter_kws={'s':10}, line_kws={"color":"red"})
plt.title("Scatter Plot with Regression Line")
plt.xlabel("Numeric Column 1")
plt.ylabel("Numeric Column 2")
plt.show()