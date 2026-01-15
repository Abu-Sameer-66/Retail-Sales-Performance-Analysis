<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&ColorList=0f0f0f,1c1c1c,d4af37,8b8000,f5f5f5&height=250&section=header&text=Retail%20Sales%20Performance%20Analysis&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Business%20Intelligence%20%7C%20Strategic%20Profit%20Optimization&descAlignY=60&descAlign=50" width="100%"/>
</div>



<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=D1E0DD&center=true&vCenter=true&width=600&lines=Identifying+Profit+Leakages;Engineered+COGS+and+Margin+Metrics;Optimizing+Regional+Supply+Chains;Python+%7C+Pandas+%7C+Seaborn"/>
</div>
<br/>

<div align="center">
  <a href="https://github.com/Abu-Sameer-66">
    <img src="https://img.shields.io/badge/Maintained%3F-yes-005C97.svg?style=for-the-badge"/>
  </a>
  <a href="https://github.com/Abu-Sameer-66/Retail-Sales-Performance-Analysis">
    <img src="https://img.shields.io/badge/Python-3.9+-363795.svg?style=for-the-badge&logo=python&logoColor=white"/>
  </a>
  <a href="https://github.com/Abu-Sameer-66/Retail-Sales-Performance-Analysis">
    <img src="https://img.shields.io/badge/Status-Production_Ready-success.svg?style=for-the-badge"/>
  </a>
  <a href="https://github.com/Abu-Sameer-66/Retail-Sales-Performance-Analysis">
    <img src="https://img.shields.io/badge/Domain-Business_Intelligence-blueviolet.svg?style=for-the-badge"/>
  </a>
</div>

---

### 💼 The Business Problem
A US Superstore is generating high revenue but facing **critical margin pressure**. Traditional analysis looks at *Sales*, but this project engineers financial metrics to find the *True Profit*.

| 🚨 Problem | 💡 Solution Engineered | 🎯 Goal |
| :--- | :--- | :--- |
| **Negative Margins** | Calculated **COGS (Cost of Goods Sold)** to identify products costing more than they earn. | Stop bleeding cash on bad products. |
| **Discount Traps** | Correlated `Discount %` vs `Profit` to find the exact "tipping point" where deals become losses. | Optimize pricing strategy. |
| **Regional Bloat** | Segmented performance by Region to find areas with high volume but low ROI. | Fix supply chain inefficiencies. |

---

### 🧩 System Architecture
*The data flows through a structured BI pipeline:*

```mermaid
graph LR
    A[Raw Transaction Data] -->|Pandas| B(Data Cleaning & Audit)
    B --> C{Feature Engineering}
    C -->|Calculate| D[COGS & Margin %]
    C -->|Extract| E[Temporal Trends]
    D --> F[Visual Analysis]
    E --> F
    F --> G[Strategic Report]
    style C fill:#363795,stroke:#005C97,stroke-width:2px,color:#fff
    style G fill:#005C97,stroke:#363795,stroke-width:2px,color:#fff
