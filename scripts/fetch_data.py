import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

# Connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Test the connection
try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

# Establish the connection
conn = pyodbc.connect(connection_string)

# Fetch dbo.oil
query_oil = "SELECT * FROM dbo.oil"
df_oil = pd.read_sql(query_oil, conn)

# Fetch dbo.holidays_events
query_holidays_events = "SELECT * FROM dbo.holidays_events"
df_holidays_events = pd.read_sql(query_holidays_events, conn)

# Fetch dbo.stores
query_stores = "SELECT * FROM dbo.stores"
df_stores = pd.read_sql(query_stores, conn)

# Close the connection
conn.close()

# Save to CSV
df_oil.to_csv('oil.csv', index=False)
df_holidays_events.to_csv('holidays_events.csv', index=False)
df_stores.to_csv('stores.csv', index=False)

print("Datasets have been successfully downloaded and saved as CSV files.")