import pyodbc
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the DB_USERNAME and DB_PASSWORD environment variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_SERVER = os.getenv("DB_SERVER")

# Connect to the SQL Server database
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    f'SERVER={DB_SERVER};'
    f'DATABASE={DB_NAME};'
    f'UID={DB_USERNAME};'
    f'PWD={DB_PASSWORD};'
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Execute the SQL query
query = 'SELECT * FROM [dbo].[BOstatus]'
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Get the column names
column_names = [column[0] for column in cursor.description]

# Define the path for the CSV file
# Replace with your desired path
csv_path = 'C:/Users/user/Desktop/enctest/output.csv'

# Create the directory if it does not exist
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Write the results to the CSV file
with open(csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the column names to the CSV file
    writer.writerow(column_names)

    # Write the data rows to the CSV file
    writer.writerows(results)

# Close the cursor and connection
cursor.close()
conn.close()
