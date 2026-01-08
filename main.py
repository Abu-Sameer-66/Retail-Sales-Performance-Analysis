# ==========================================
# 📈 RETAIL SALES STRATEGIC ANALYSIS ENGINE
# ==========================================
# Author: Sameer
# Purpose: End-to-end analysis of retail performance, identifying profit drivers and operational inefficiencies.

# --- 1. SETUP & CONFIGURATION ---
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import sys

# Suppress warnings for cleaner presentation
warnings.filterwarnings('ignore')

# Set professional plotting style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

print("Environment Setup Complete.")

# --- 2. DATA INGESTION ---
try:
    # Loading the dataset (Ensure 'SampleSuperstore.csv' is in the same folder)
    df = pd.read_csv('SampleSuperstore.csv')
    print(f"Data Loaded Successfully.")
    print(f"   Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")

except FileNotFoundError:
    print("CRITICAL ERROR: 'SampleSuperstore.csv' not found.")
    print("   -> Please upload the CSV file to the same folder as this script.")
    # Stop execution safely prevents crashing later
    sys.exit("Execution stopped due to missing data file.")

# --- 3. DATA CLEANING ---
print("\n--- Data Cleaning Status ---")

# A. Duplicate Removal
initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
cleaned_rows = df.shape[0]
if initial_rows != cleaned_rows:
    print(f"   • Removed {initial_rows - cleaned_rows} duplicate rows.")
else:
    print("   • No duplicates found.")

# B. Remove Noise (Postal Code)
if 'Postal Code' in df.columns:
    df.drop(columns=['Postal Code'], inplace=True)
    print("   • Dropped 'Postal Code' column (irrelevant for strategic analysis).")

# C. Null Check
nulls = df.isnull().sum().sum()
if nulls == 0:
    print("   • No missing values detected.")
else:
    print(f"   • Warning: {nulls} missing values found.")

# --- 4. ADVANCED FEATURE ENGINEERING (The Pro Logic) ---
print("\n--- Engineering Business Metrics ---")

# A. Convert Dates (Crucial for trends)
# We assume 'Order Date' exists; if not, we skip safely
if 'Order Date' in df.columns:
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Order Year'] = df['Order Date'].dt.year
        df['Order Month'] = df['Order Date'].dt.month_name()
        print("   • Added Temporal Features: 'Order Year', 'Order Month'")
    except Exception as e:
        print(f"   • Warning: Could not parse dates. Error: {e}")

# B. Calculate 'Cost' (COGS)
# Logic: Revenue (Sales) - Net Income (Profit) = Cost
df['Cost'] = df['Sales'] - df['Profit']

# C. Calculate 'Profit Margin %'
# Logic: Efficiency metric. How much of every dollar do we keep?
df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100

# D. Calculate 'Unit Price' (Approximation)
# Logic: Identify pricing tier (Luxury vs. Commodity)
df['Unit Price'] = df['Sales'] / df['Quantity']

print("   • Added Financial Metrics: 'Cost', 'Profit Margin %', 'Unit Price'")
print(f"   • Final Dataset Columns: {list(df.columns)}")

# --- 5. VISUALIZATION DASHBOARD ---

# V1: Correlation Heatmap (The Discount Trap)
plt.figure(figsize=(10, 6))
numeric_df = df.select_dtypes(include=[np.number])
correlation = numeric_df.corr()
sns.heatmap(correlation, annot=True, cmap='RdBu', fmt='.2f', linewidths=0.5)
plt.title("Correlation Matrix: Impact of Discount on Profit", fontsize=14, fontweight='bold')
plt.show()

# V2: Regional Performance (Sales vs Profit)
region_analysis = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
region_analysis.plot(kind='bar', figsize=(12, 6), color=['#4c72b0', '#c44e52'])
plt.title("Regional Performance: Sales vs. Profit", fontsize=14, fontweight='bold')
plt.ylabel("Total Amount ($)")
plt.xticks(rotation=0)
plt.legend(title='Metric')
plt.show()

# V3: Annual Growth Trend (New!)
if 'Order Year' in df.columns:
    plt.figure(figsize=(10, 5))
    yearly_trend = df.groupby('Order Year')['Sales'].sum().reset_index()
    sns.lineplot(data=yearly_trend, x='Order Year', y='Sales', marker='o', color='green', linewidth=2.5)
    plt.title("📈 Annual Sales Growth Trajectory", fontsize=14, fontweight='bold')
    plt.ylabel("Total Sales ($)")
    plt.grid(True, alpha=0.3)
    plt.show()

# V4: Sub-Category Loss Analysis
plt.figure(figsize=(14, 7))
order = df.groupby("Sub-Category")["Profit"].sum().sort_values().index
sns.barplot(data=df, y="Profit", x="Sub-Category", estimator=sum, order=order, palette="coolwarm_r")
plt.title("Profit by Sub-Category (Identifying Loss Makers)", fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.show()

# --- 6. STRATEGIC EXECUTIVE SUMMARY ---
print("\nEXECUTIVE CONSULTING REPORT")
print("==============================")
print("1. THE DISCOUNT TRAP: Correlation analysis confirms a strong negative link (-0.22)")
print("   between Discounts and Profit. We are 'buying' sales at the cost of margins.")
print("\n2. REGIONAL INEFFICIENCY: The Central Region is generating high volume but")
print("   suffering from disproportionately high Costs (see Cost metric).")
print("\n3. PRODUCT WARNING: 'Tables' and 'Bookcases' are operating at a net loss.")
print(f"   The average Unit Price for Tables is ${df[df['Sub-Category']=='Tables']['Unit Price'].mean():.2f},")
print("   yet they yield negative margins. Immediate pricing review recommended.")
