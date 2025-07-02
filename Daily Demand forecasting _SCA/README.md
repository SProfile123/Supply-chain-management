🏭 Supply Chain Analytics Project – Manufacturing Domain

This project demonstrates how data analytics can improve real-world supply chain operations in the **manufacturing industry**. Using simulated multi-ERP data, we forecast demand, analyze cost fluctuations, evaluate supplier performance, and identify inefficiencies in inventory planning such as MOQ breaches — all visualized through powerful Power BI dashboards.

---

## 📌 Project Objective

To build a data-driven decision support tool for **Supply Chain Analysts** in the manufacturing domain by:

- Forecasting order volume using historical demand data  
- Tracking **Purchase Price Variance (PPV)** and **duties cost trends**  
- Identifying **items breaching MOQ** through order frequency analysis  
- Creating **automated supplier scorecards** to improve vendor performance  

---

## 🧰 Tools & Technologies Used

- **Python**: Data processing, Prophet forecasting  
- **Power BI**: Dashboards for cost, inventory and supplier insights  
- **Pandas / Matplotlib**: EDA & KPI analysis  
- **Prophet**: Time series forecasting  
- **Simulated ERP Data**: SKU, order and supplier datasets

## 📊 Power BI Dashboards

### 1. 📉 Forecast Dashboard
- Displays actual vs predicted demand  
- Built using Prophet’s 90-day forecast  
- Highlights demand trends and confidence intervals  

### 2. 💰 Cost & PPV Dashboard
- Visualizes purchase price variance by category  
- Tracks duties paid and average unit cost  
- Helps uncover pricing fluctuations across suppliers or categories  

### 3. 📦 MOQ & Order Frequency Analysis
- Highlights items breaching their minimum order quantity  
- Analyzes SKU ordering patterns vs their MOQ  
- Heatmap shows risk of stock-outs or excess stock  

### 4. 🤝 Supplier Scorecard
- Tracks KPIs like On-Time Delivery, Fill Rate, Cost Compliance  
- Ranks suppliers for sourcing optimization  
- Helps drive supplier accountability


## 📈 Forecasting Methodology

We used **Facebook Prophet** to predict daily demand based on historical orders:

- Input: `orders.csv` (date & total order count)
- Output: `forecast_output.csv` (yhat, lower/upper bounds)
- Visualized inside Power BI


## ✅ Business Value

- 📉 Reduce costs by controlling PPV and duties
- 📦 Optimize inventory with MOQ adherence tracking
- 🔍 Identify low-performing suppliers early
- 📊 Empower stakeholders with real-time dashboards

## 🚀 How to Run This Project

1. Clone the repo
2. Install Python dependencies: pip install -r requirements.txt
3. Open and run the notebook: notebooks/forecast_model.ipynb
4. Load CSVs into Power BI and recreate dashboards (or use included screenshots)
