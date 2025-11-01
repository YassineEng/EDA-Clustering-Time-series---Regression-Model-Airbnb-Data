# Airbnb Data Analysis and Price Prediction

This project analyzes Airbnb data from a local SQL Server data warehouse. It performs feature engineering, exploratory data analysis (EDA), clustering, and builds a regression model to predict listing prices.

## Project Overview

The project is structured as a data pipeline that processes raw Airbnb data into a format suitable for analysis and modeling. The pipeline consists of the following steps:

1.  **Data Extraction and Feature Engineering:** Data is extracted from a SQL Server database. A SQL view (`vw_listing_features`) is created to join calendar and listing data and to engineer new features. This view is then materialized into a table (`listing_features`) for performance.
2.  **Exploratory Data Analysis (EDA):** The `01_EDA.ipynb` notebook performs a thorough exploratory data analysis of the dataset. This includes visualizing data distributions, identifying correlations, and gaining insights into the factors that influence Airbnb prices.
3.  **Price Prediction Modeling:** The `02_price_pred.ipynb` notebook builds a regression model to predict Airbnb listing prices. This involves feature selection, model training, and evaluation.

## Data

The project uses two main tables from the data warehouse:

*   `fact_calendar`: Contains information about the availability of listings over time.
*   `dim_listings`: Contains detailed information about each listing, such as price, location, number of reviews, etc.

These tables are joined to create the `listing_features` table, which is the main dataset used for analysis and modeling.

## Data Pipeline

The data pipeline is orchestrated by a series of Python scripts in the `scripts/` directory:

1.  `00_connect_test.py`: Tests the connection to the SQL Server database.
2.  `01_create_view.py`: Creates the `vw_listing_features` view by joining the `fact_calendar` and `dim_listings` tables and calculating new features.
3.  `02_create_table_from_view.py`: Materializes the `vw_listing_features` view into a table named `listing_features`.
4.  `03_create_indexes.py`: Creates indexes on the `listing_features` table to improve query performance.

## Exploratory Data Analysis (EDA)

The EDA is performed in the `notebooks/01_EDA.ipynb` notebook. The analysis explores the relationships between different variables and their impact on listing prices.

## Modeling

The price prediction model is built in the `notebooks/02_price_pred.ipynb` notebook. The notebook covers the following steps:

*   Feature selection and preprocessing
*   Model training (using CatBoost, as indicated by the `catboost_info` directory)
*   Model evaluation and interpretation

## How to Run

1.  **Set up the database:**
    *   Make sure you have a SQL Server instance running with the Airbnb data.
    *   Create a `.env` file in the root directory and populate it with your database credentials. See the `config/db_config.py` file for the required variables. An example `.env` file would look like this:

        ```
        SERVER_NAME=<your_server_name>
        MDF_FILE=<path_to_your_mdf_file>
        DB_NAME=<your_database_name>
        ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the data pipeline:**

    ```bash
    python scripts/00_connect_test.py
    python scripts/01_create_view.py
    python scripts/02_create_table_from_view.py
    python scripts/03_create_indexes.py
    ```

4.  **Run the notebooks:**
    *   Open and run the `notebooks/01_EDA.ipynb` notebook to perform the exploratory data analysis.
    *   Open and run the `notebooks/02_price_pred.ipynb` notebook to train and evaluate the price prediction model.

## Dependencies

*   `pyodbc`
*   `sqlalchemy`
*   `pandas`
*   `numpy`
*   `scikit-learn`
*   `matplotlib`
*   `seaborn`
*   `python-dotenv`
*   `catboost`