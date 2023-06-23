import pyodbc
import csv
import os

# Connect to the SQL Server database
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-IN94E5H\SQLEXPRESS;'
    'DATABASE=CDB;'
    
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Execute the SQL query
query = 'SELECT * FROM Customer'
cursor.execute(query)

#Fetch all the results
results = cursor.fetchall()

# Get the column names
column_names = [column[0] for column in cursor.description]

# Define the path for the CSV file
csv_path = 'C:/Users/Pawar/Desktop/projects/Fetch_data_from_sql_and_export_it_into_csv_and_send_it_on_mail/output.csv'  # Replace with your desired path

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