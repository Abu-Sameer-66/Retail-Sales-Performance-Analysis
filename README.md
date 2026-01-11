<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=c44e52,4c72b0&height=250&section=header&text=Retail%20Sales%20Performance%20Analysis&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Business%20Intelligence%20%7C%20Strategic%20Profit%20Optimization&descAlignY=60&descAlign=50" width="100%"/>
</div>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=C44E52&center=true&vCenter=true&width=600&lines=Identifying+Profit+Leakages;Engineered+COGS+and+Margin+Metrics;Optimizing+Regional+Supply+Chains;Python+%7C+Pandas+%7C+Seaborn"/>
</div>

<br/>

<div align="center">
  <a href="https://github.com/Abu-Sameer-66">
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge"/>
  </a>
  <a href="https://github.com/Abu-Sameer-66/Retail-Sales-Performance-Analysis">
    <img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white"/>
  </a>
  <a href="https://github.com/Abu-Sameer-66/Retail-Sales-Performance-Analysis">
    <img src="https://img.shields.io/badge/Status-Production_Ready-orange.svg?style=for-the-badge"/>
  </a>
</div>

---

### 💼 The Business Problem
A US Superstore is generating high revenue but facing **critical margin pressure**. Traditional analysis looks at *Sales*, but this project engineers financial metrics to find the *True Profit*.

| 🚨 Problem | 💡 Solution Engineered |
| :--- | :--- |
| **Negative Margins** | Calculated **COGS (Cost of Goods Sold)** to identify products costing more than they earn. |
| **Discount Traps** | Correlated `Discount %` vs `Profit` to find the exact "tipping point" where deals become losses. |
| **Regional Bloat** | Segmented performance by Region to find areas with high volume but low ROI. |

---

### ⚙️ Advanced Feature Engineering
*Beyond standard EDA, this engine derives new business metrics:*

```python
# Key Financial Metrics Added to Dataset
df['Cost'] = df['Sales'] - df['Profit']                # Operational Overhead
df['Profit Margin %'] = (df['Profit'] / df['Sales'])   # Efficiency Ratio
df['Unit Price'] = df['Sales'] / df['Quantity']        # Pricing Tier Segmentation
