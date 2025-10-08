# ETL-Sales-Insights-Dashboard

### 🧠 Sales Performance Dashboard — Power BI + MySQL + Python
### 📊 Project Overview

This project showcases a Sales Performance Dashboard built using Power BI connected to a MySQL database.
The goal is to demonstrate a full ETL (Extract, Transform, Load) data pipeline — from data cleaning in Python,
storing in MySQL, and creating interactive dashboards in Power BI.

It’s designed to simulate a real-world data workflow that a Data Engineer or Analyst would perform.

### ⚙️ Tech Stack
-> Python → Data cleaning and preprocessing (using pandas)
-> MySQL → Data storage and querying
-> Power BI → Data visualization and dashboard creation

### 📦 ETL-SALES-INSIGHTS-DASHBOARD
 ┣ 📁 data/
 ┃ ┗ superstore.csv           
 ┣ 📁 script/
 ┃ ┗ main.py      
 ┣ 📁 powerbi/
 ┃ ┗ SalesDashboard.pbix      
 ┣ 📄 requirements.txt         
 ┣ 📄 README.md                

### 🚀 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/sales-performance-dashboard.git
cd sales-performance-dashboard

2️⃣ Install Python Dependencies
pip install -r requirements.txt

3️⃣ Load the Data into MySQL
Create a MySQL database named etl_project
Run your MySQL server
Execute the Python script:
python scripts/clean_sales_data.py

4️⃣ Connect Power BI to MySQL
Open Power BI Desktop
Click Get Data → MySQL Database
Enter your MySQL credentials
(Host: localhost, Database: sales_db)
Load the data and explore the dashboard

### 📈 Dashboard Features
✅ Total Sales & Profit Overview
✅ Top Performing Products
✅ Regional Sales Breakdown
