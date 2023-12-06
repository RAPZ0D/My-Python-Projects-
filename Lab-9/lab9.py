# Connecting to MySQL database
import mysql.connector

# Your database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'lab9'
}

try:
    with mysql.connector.connect(**db_config) as connection:
        print("Connected to MySQL database!")
        # Perform your operations here

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

# Inserting values In PropertyInfo Table
import pandas as pd
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'lab9'
}

# Columns to extract from CSV and their corresponding names in the database table
columns_to_insert = {
    'ID': 'Id',
    'Possession Status': 'PosessionStatus',
    'Availability Starts From': 'AvailibilityStartsFrom',
    'Floor No': 'FloorNo',
    'Commercial': 'Commercial',
    'Developer': 'Developer',
    'Approved Authority Name': 'ApprovedAuthorityName',
    'Units Available': 'UnitsAvailable',
    'Price': 'Price',
    'Price (English)': 'PriceEnglish',
    'Flooring Type': 'FlooringType',
    'Electricity Status': 'ElectricityStatus',
    'Maintenance Type': 'MaintenanceType',
    'Maintenance Charges': 'MaintenanceCharges',
    'Booking Amount': 'BookingAmount'
}

# Read the CSV file with appropriate settings to handle mixed types
file_path = 'lab9_data.csv'
data = pd.read_csv(file_path, usecols=columns_to_insert.keys(), na_values=['nan'], dtype=str)

try:
    # Establish connection to MySQL
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Insert values into PropertyInfo table
    for index, row in data.iterrows():
        formatted_row = [row[column] if pd.notnull(row[column]) else None for column in columns_to_insert.keys()]  # Arrange columns as per PropertyInfo
        
        sql = f"INSERT INTO PropertyInfo ({', '.join(columns_to_insert.values())}) VALUES ({', '.join(['%s'] * len(columns_to_insert))})"
        cursor.execute(sql, tuple(formatted_row))

    connection.commit()
    print("Data inserted successfully!")

except mysql.connector.Error as e:
    print(f"Error inserting data into MySQL: {e}")

finally:
    if 'connection' in locals() or 'connection' in globals():
        # Close the connection
        connection.close()
        print("MySQL connection closed")

# Inserting values into Property Details Table
import pandas as pd
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'lab9'
}

# Columns to extract from CSV and their corresponding names in the database table
columns_to_insert_details = {
    'ID': 'Id',
    'Landmark': 'Landmark',
    'Covered Area': 'CoveredArea',
    'Project Name': 'ProjectName',
    'sqft Price ': 'SqftPrice',
    'Carpet Area': 'CarpetArea',
    'Area Name': 'AreaName',
    'Property Uniqueness': 'PropertyUniqueness',
    'Unit of Carpet Area': 'UnitOfCarpetArea',
    'Society': 'Society',
    'Ownership Type': 'OwnershipType',
    'furnished Type': 'FurnishedType',
    'Bathroom': 'Bathroom',
    'Parking': 'Parking'
}

# Read the CSV file with appropriate settings to handle mixed types
file_path = 'lab9_data.csv'
data = pd.read_csv(file_path, usecols=columns_to_insert_details.keys(), na_values=['nan'], dtype=str)

try:
    # Establish connection to MySQL
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Insert values into PropertyDetails table
    for index, row in data.iterrows():
        formatted_row = [row[column] if pd.notnull(row[column]) else None for column in columns_to_insert_details.keys()]  # Arrange columns as per PropertyDetails
        
        sql = f"INSERT INTO PropertyDetails ({', '.join(columns_to_insert_details.values())}) VALUES ({', '.join(['%s'] * len(columns_to_insert_details))})"
        cursor.execute(sql, tuple(formatted_row))

    connection.commit()
    print("Data inserted into PropertyDetails successfully!")

except mysql.connector.Error as e:
    print(f"Error inserting data into PropertyDetails in MySQL: {e}")

finally:
    if 'connection' in locals() or 'connection' in globals():
        # Close the connection
        connection.close()
        print("MySQL connection closed")

# Visualization 2
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'lab9'
}

try:
    # Establish connection to MySQL
    connection = mysql.connector.connect(**db_config)

    # Fetching MaintenanceCharges column from PropertyInfo table
    query_info = "SELECT MaintenanceCharges FROM PropertyInfo"
    df_info = pd.read_sql(query_info, connection)

    # Fetching Landmark column from PropertyDetails table
    query_details = "SELECT Landmark FROM PropertyDetails"
    df_details = pd.read_sql(query_details, connection)

    # Drop rows with missing values
    df_info.dropna(subset=['MaintenanceCharges'], inplace=True)
    df_details.dropna(subset=['Landmark'], inplace=True)

    # Plotting the bar chart for average maintenance charges by Landmark
    plt.figure(figsize=(10, 6))
    df_merged = pd.concat([df_info, df_details], axis=1)
    avg_maintenance = df_merged.groupby('Landmark')['MaintenanceCharges'].mean().reset_index()
    plt.bar(avg_maintenance['Landmark'], avg_maintenance['MaintenanceCharges'], color='skyblue')
    plt.xlabel('Landmark')
    plt.ylabel('Average Maintenance Charges')
    plt.title('Average Maintenance Charges for Properties by Landmark')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

except mysql.connector.Error as e:
    print(f"Error accessing data from MySQL: {e}")

finally:
    if 'connection' in locals() or 'connection' in globals():
        # Close the connection
        connection.close()
        print("MySQL connection closed")

#Visualziation 3 
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'lab9'
}

try:
    # Establish connection to MySQL
    connection = mysql.connector.connect(**db_config)

    # Fetching FlooringType and Price columns from PropertyInfo table
    query_info = "SELECT FlooringType, Price FROM PropertyInfo"
    df_info = pd.read_sql(query_info, connection)

    # Drop rows with missing values
    df_info.dropna(subset=['FlooringType', 'Price'], inplace=True)

    # Grouping by FlooringType and summing up the Price for each type
    grouped_data = df_info.groupby('FlooringType')['Price'].sum().reset_index()

    # Pivot the data to plot a stacked area chart
    pivot_data = grouped_data.pivot(columns='FlooringType', values='Price').fillna(0)

    # Create a stacked area chart
    pivot_data.plot(kind='area', stacked=True, figsize=(10, 6))
    plt.xlabel('Property')
    plt.ylabel('Price')
    plt.title('Stacked Area Visualization of Price by Flooring Type')
    plt.legend(title='Flooring Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

except mysql.connector.Error as e:
    print(f"Error accessing data from MySQL: {e}")

finally:
    if 'connection' in locals() or 'connection' in globals():
        # Close the connection
        connection.close()
        print("MySQL connection closed")
