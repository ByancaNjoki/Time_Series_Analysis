# Time_Series_Analysis


# Corporation Favorita Sales Forecasting Project

### Project Overview

Welcome to the Corporation Favorita Sales Forecasting project! My mission as a data analyst here was to ensure that Favorita stores always have the right quantity of products in stock. By predicting future sales with the help of machine learning models, they can make smarter inventory decisions, reduce waste, and better serve their customers. This project leverages data from various sources, including transactional data, store metadata, and economic indicators, following the CRISP-DM framework to guide our data science process.

### Table of Contents

- Project Overview
- Data Description
- Installation
- Project Structure
- Data Preprocessing and Exploratory Data Analysis (EDA)
- Feature Engineering
- Modeling
- Model Evaluation
- Usage

### Data Description

### Our Datasets
These are the datasets provided for usage:

1. train.csv: Historical sales data for training our models.
2. test.csv: Data to test our models and predict future sales.
3. transaction.csv: Details of daily transactions in each store.
4. sample_submission.csv: A template for our sales predictions.
5. stores.csv: Metadata about our stores, including location and type.
6. oil.csv: Daily oil prices, crucial for understanding economic impacts on sales.
7. holidays_events.csv: Information about holidays and events, which can significantly affect shopping behavior.

### Data Fields in train.csv

- date: The date of the sales data.
- store_nbr: The store number where the product was sold.
- amily: The product category.
- sales: Total sales for the product family at a specific store on a given date.
- onpromotion: Number of items in a product family that were on promotion on a given date.

### Installations
### Prerequisites
- Python 3.7+

### Summary of Installed Libraries

- Pandas: For data manipulation and analysis.
- NumPy: For numerical computations.
- Matplotlib: For data visualization.
- Seaborn: For statistical data visualization.
- Statsmodels: For statistical modeling and time series analysis.
- Scikit-learn: For machine learning algorithms and tools.
- Pmdarima: For automated ARIMA model selection.
- XGBoost: For gradient boosting models.
- Scipy: For scientific and technical computing.
- Catboost: For gradient boosting models.
- Calplot: For calendar heatmaps.
- Jupyter: For interactive notebooks.


### Project Structure

corporation-favorita-sales-forecasting
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── transaction.csv
│   ├── sample_submission.csv
│   ├── stores.csv
│   ├── oil.csv
│   └── holidays_events.csv
│
├── scripts/
│   └── fetch_data.py
│
├── notebooks/
│   ├── main_favorita.ipynb
│   
│
├── env/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── ...
│
├── .gitignore
├── README.md
|

### Data Preprocessing and Exploratory Data Analysis (EDA)

- EDA is a vital step in the workflow, helping uncover the underlying patterns and relationships in the data. By leveraging visualization libraries like Matplotlib and Seaborn, we can effectively visualize trends, seasonality, and the influence of promotions on sales to enhance our understanding of the data but and inform feature engineering efforts, ensuring the most relevant information for our predictive models are captured.


- Started by loading datasets using pandas and data fetching script for the datasets availed in the DB.

### Handling Missing Values
Missing values are handled using appropriate imputation techniques to ensure our models receive clean data.

### Date Conversion
Dates are converted to datetime objects for easier manipulation.

### Merging Datasets
We merge various datasets to create a comprehensive dataset for our models.

### Feature Engineering
These are the implemented features to boost our models' predictive power:

- Lag Features: Sales from previous days to capture temporal dependencies.
- Rolling Features: Rolling mean and standard deviation of sales.
- Date Features: Extracting day of the week, month, year, etc.
- Holiday Features: Indicators for holidays and events affecting sales.

### Modeling
- The below are te models experimented with for the analysis with each model is carefully tuned and validated using cross-validation to find the best-performing model.:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- ARIMA
- SARIMAX

### Model Evaluation

The models are evaluated using these metrics to help understand how well the models are performing and guide in selecting the best model for the analysis.:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)


