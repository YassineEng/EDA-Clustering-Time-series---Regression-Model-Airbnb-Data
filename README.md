# 🏠 Airbnb Data Analysis and Price Prediction  

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Data%20Warehouse-red?logo=microsoftsqlserver)
![CatBoost](https://img.shields.io/badge/CatBoost-Model-orange?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)
---

## 📘 Project Overview  

This project analyzes **Airbnb data** from a local **SQL Server data warehouse**. It performs **feature engineering**, **exploratory data analysis (EDA)**, **clustering**, and builds a **regression model** to predict listing prices.  

The project is structured as a **data pipeline** that processes raw Airbnb data into a format suitable for analysis and modeling.  

### 🔄 Pipeline Steps  

1. **Data Extraction and Feature Engineering**  
   - Data is extracted from a SQL Server database.  
   - A SQL view (`vw_listing_features`) is created to join calendar and listing data and to engineer new features.  
   - This view is then materialized into a table (`listing_features`) for performance.  

2. **Exploratory Data Analysis (EDA)**  
   - The `01_EDA.ipynb` notebook performs a thorough exploratory data analysis of the dataset.  
   - This includes visualizing data distributions, identifying correlations, and gaining insights into the factors that influence Airbnb prices.  

3. **Price Prediction Modeling**  
   - The `02_price_pred.ipynb` notebook builds a regression model to predict Airbnb listing prices.  
   - This involves feature selection, model training, and evaluation.  

---

## 🧱 Data  

The project uses two main tables from the **data warehouse**:

| Table | Description |
|--------|--------------|
| `fact_calendar` | Contains information about the availability of listings over time. |
| `dim_listings` | Contains detailed information about each listing, such as price, location, number of reviews, etc. |

These tables are joined to create the **`listing_features`** table, which is the main dataset used for analysis and modeling.  

---

## ⚙️ Data Pipeline  

The data pipeline is orchestrated by a series of Python scripts in the `scripts/` directory:

| Script | Description |
|---------|--------------|
| `00_connect_test.py` | Tests the connection to the SQL Server database. |
| `01_create_view.py` | Creates the `vw_listing_features` view by joining the `fact_calendar` and `dim_listings` tables and calculating new features. |
| `02_create_table_from_view.py` | Materializes the `vw_listing_features` view into a table named `listing_features`. |
| `03_create_indexes.py` | Creates indexes on the `listing_features` table to improve query performance. |

---

## 📊 Exploratory Data Analysis (EDA)  

The EDA is performed in the **`notebooks/01_EDA.ipynb`** notebook.  
It explores the relationships between different variables and their impact on listing prices, including:  
- Price distributions  
- Review trends  
- Correlation between features  
- Geographical and neighborhood-level effects  

---

## 🤖 Modeling  

The **price prediction model** is built in the **`notebooks/02_price_pred.ipynb`** notebook.  
The notebook covers the following steps:  

- Feature selection and preprocessing  
- Model training (using **CatBoost**)  
- Model evaluation and interpretation  

---

## 🚀 How to Run  

### 1️⃣ Set up the database  

- Ensure a **SQL Server** instance is running with the Airbnb data.  
- Create a `.env` file in the root directory and populate it with your database credentials.  
  Refer to `config/db_config.py` for required variables.  

**Example `.env` file:**  

```bash
SERVER_NAME=<your_server_name>
MDF_FILE=<path_to_your_mdf_file>
DB_NAME=<your_database_name>
