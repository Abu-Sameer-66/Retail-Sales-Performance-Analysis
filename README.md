# 📈 Retail Sales Performance Analysis

> **A Strategic Business Intelligence (BI) solution identifying key drivers of profit and operational inefficiencies across US retail regions.**
> *Leverages Python, Pandas, and Seaborn to derive actionable insights from transaction data.*

[![Status](https://img.shields.io/badge/Status-Production_Ready-success)]()
[![License](https://img.shields.io/badge/License-MIT-blue)]()

---

### 💼 Business Problem
A US Superstore is generating high revenue but facing **margin pressure**. This project engineers new financial metrics (COGS, Unit Price) to identify:
1.  **Loss-Making Products:** Which items are selling at a negative margin?
2.  **Discount Traps:** How discounting strategies are eroding profit.
3.  **Regional Inefficiencies:** Areas with high sales but low ROI.

---

### ⚙️ Feature Engineering
Unlike standard analysis, this project derives advanced business metrics:
- **`Cost` (COGS):** Calculated as `Sales - Profit` to track operational overhead.
- **`Profit Margin %`:** Evaluates efficiency per transaction.
- **`Unit Price`:** Approximated to segment Luxury vs. Economy products.
- **`Order Year/Month`:** Extracted for time-series trend analysis.

---

### 📊 Key Insights & Visualizations
The analysis pipeline generates the following strategic outputs:
- **The Discount Trap:** Heatmap revealing a strong negative correlation (`-0.22`) between Discount and Profit.
- **Category Audit:** Bar charts identifying **"Tables"** and **"Bookcases"** as primary loss-makers.
- **Growth Trajectory:** Time-series line plots tracking annual sales performance.

---

### 🚀 How to Run
1. **Clone the repo**
   ```bash
   git clone [https://github.com/Abu-Sameer-66/Retail-Sales-Performance-Analysis.git](https://github.com/Abu-Sameer-66/Retail-Sales-Performance-Analysis.git)
