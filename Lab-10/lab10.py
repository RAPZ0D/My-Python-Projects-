#LAB 10 
#Testing the connection 
import psycopg2

# Database credentials
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'database': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Create a cursor to interact with the database
    cursor = conn.cursor()

    # Display a message upon successful connection
    print("Connected to PostgreSQL!")

    # Close cursor and connection
    cursor.close()
    conn.close()
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")


# importing the data
# Table 1
import pandas as pd
import psycopg2

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

# File path for the CSV dataset
file_path = 'world_development_data.csv'

# Load the CSV dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(**db_config)

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the PostgreSQL table with incremental CountryID values
for idx, row in data.iterrows():
    # Assign incremental numbers to CountryID starting from 1
    country_id = idx + 1

    # Extract data from the CSV
    country_name = row['Country']
    region = row['Region']
    sub_region = row['SubRegion']
    interm_region = row['IntermRegion']
    surf_area_sq_km = row['SurfAreaSqKm']
    pop_dens = row['PopDens']
    pop_growth = row['PopGrowth%']

    # SQL query to insert data into the CountryInfo table
    sql = """
    INSERT INTO CountryInfo (CountryID, CountryName, Region, SubRegion, IntermRegion, SurfAreaSqKm, PopDensWW, PopGrowth)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    # Execute the SQL query
    cur.execute(sql, (country_id, country_name, region, sub_region, interm_region, surf_area_sq_km, pop_dens, pop_growth))

# Commit changes to the database
conn.commit()

# Close communication with the database
cur.close()
conn.close()

# Table 2
import pandas as pd
import psycopg2

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

# File path for the CSV dataset
file_path = 'world_development_data.csv'

# Load the CSV dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(**db_config)

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the PostgreSQL table with values corresponding to the EconomicIndicators columns
success = True  # Flag to track successful insertion

for idx, row in data.iterrows():
    try:
        # Extract data from the CSV
        year = row['Year']
        country_name = row['Country']  # Assuming 'Country' column name from CSV
        gdp = row['GDP']
        gdp_growth = row['GDPGrowth%']
        adol_fert_rate = row['AdolFertRate']
        agri_val_add_gdp = row['AgriValAdd%GDP']
        dom_credit_gdp = row['DomCredit%GDP']
        exports_gdp = row['Exports%GDP']
        # Add other columns similarly...

        # Fetch the CountryID from CountryInfo table based on CountryName
        cur.execute("SELECT CountryID FROM CountryInfo WHERE CountryName = %s;", (country_name,))
        country_id = cur.fetchone()[0]

        # SQL query to insert data into the EconomicIndicators table
        sql = """
        INSERT INTO EconomicIndicators (Year, CountryID, GDP, GDPGrowth, AdolFertRate, AgriValAddGDP, DomCreditGDP, ExportsGDP)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        # Execute the SQL query
        cur.execute(sql, (year, country_id, gdp, gdp_growth, adol_fert_rate, agri_val_add_gdp, dom_credit_gdp, exports_gdp))
        # Add other columns similarly...

    except (psycopg2.Error, KeyError, TypeError) as e:
        print(f"Error occurred: {e}")
        success = False
        break

# Commit changes to the database if no errors occurred
if success:
    conn.commit()
    print("Data inserted successfully!")
else:
    print("Data insertion failed.")

# Close communication with the database
cur.close()
conn.close()

#Table 3 
import pandas as pd
import psycopg2

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

# File path for the CSV dataset
file_path = 'world_development_data.csv'

# Load the CSV dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(**db_config)

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the PostgreSQL table with values corresponding to the DemographicIndicators columns
success = True  # Flag to track successful insertion
current_country_id = 0  # Starting CountryID

for idx, row in data.iterrows():
    try:
        # Extract data from the CSV
        year = row['Year']
        life_exp_birth = row['LifeExpBirth']
        mort_rate_u5 = row['MortRateU5']
        net_migr = row['NetMigr']
        pop_total = row['PopTotal']

        # Incremental CountryID assignment
        current_country_id += 1

        # SQL query to insert data into the DemographicIndicators table
        sql = """
        INSERT INTO DemographicIndicators (Year, CountryID, LifeExpBirth, MortRateU5, NetMigr, PopTotal)
        VALUES (%s, %s, %s, %s, %s, %s);
        """

        # Execute the SQL query
        cur.execute(sql, (year, current_country_id, life_exp_birth, mort_rate_u5, net_migr, pop_total))

    except (psycopg2.Error, KeyError, TypeError) as e:
        print(f"Error occurred: {e}")
        success = False
        break

# Commit changes to the database if no errors occurred
if success:
    conn.commit()
    print("Data inserted successfully!")
else:
    print("Data insertion failed.")

# Close communication with the database
cur.close()
conn.close()

#Table 4 
import pandas as pd
import psycopg2

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

# File path for the CSV dataset
file_path = 'world_development_data.csv'

# Load the CSV dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(**db_config)

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the PostgreSQL table with values corresponding to the TradeIndicators columns
success = True  # Flag to track successful insertion
current_country_id = 0  # Starting CountryID

for idx, row in data.iterrows():
    try:
        # Extract data from the CSV
        year = row['Year']
        merch_trade_gdp = row['MerchTrade%GDP']  # Assuming column name; adjust if different
        # Add other column extractions based on the CSV and table structure

        # Incremental CountryID assignment
        current_country_id += 1

        # SQL query to insert data into the TradeIndicators table
        sql = """
        INSERT INTO TradeIndicators (Year, CountryID, MerchTradeGDP)
        VALUES (%s, %s, %s);
        """

        # Execute the SQL query
        cur.execute(sql, (year, current_country_id, merch_trade_gdp))

    except (psycopg2.Error, KeyError, TypeError) as e:
        print(f"Error occurred: {e}")
        success = False
        break

# Commit changes to the database if no errors occurred
if success:
    conn.commit()
    print("Data inserted successfully!")
else:
    print("Data insertion failed.")

# Close communication with the database
cur.close()
conn.close()

#Table 4
import pandas as pd
import psycopg2

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

# File path for the CSV dataset
file_path = 'world_development_data.csv'

# Load the CSV dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(**db_config)

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the PostgreSQL table with values corresponding to the TradeIndicators columns
success = True  # Flag to track successful insertion
current_country_id = 0  # Starting CountryID

for idx, row in data.iterrows():
    try:
        # Extract data from the CSV
        year = row['Year']
        merch_trade_gdp = row['MerchTrade%GDP']  # Assuming column name; adjust if different
        # Add other column extractions based on the CSV and table structure

        # Incremental CountryID assignment
        current_country_id += 1

        # SQL query to insert data into the TradeIndicators table
        sql = """
        INSERT INTO TradeIndicators (Year, CountryID, MerchTradeGDP)
        VALUES (%s, %s, %s);
        """

        # Execute the SQL query
        cur.execute(sql, (year, current_country_id, merch_trade_gdp))

    except (psycopg2.Error, KeyError, TypeError) as e:
        print(f"Error occurred: {e}")
        success = False
        break

# Commit changes to the database if no errors occurred
if success:
    conn.commit()
    print("Data inserted successfully!")
else:
    print("Data insertion failed.")

# Close communication with the database
cur.close()
conn.close()

# Table 5
import pandas as pd
import psycopg2

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

# File path for the CSV dataset
file_path = 'world_development_data.csv'

# Load the CSV dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(**db_config)

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the PostgreSQL table with values corresponding to the MiscellaneousIndicators columns
success = True  # Flag to track successful insertion
current_country_id = 0  # Starting CountryID

for idx, row in data.iterrows():
    try:
        # Extract data from the CSV
        year = row['Year']
        urban_pop_growth = row['UrbanPopGrowth%']  # Assuming column name; adjust if different
        # Add other column extractions based on the CSV and table structure

        # Incremental CountryID assignment
        current_country_id += 1

        # SQL query to insert data into the MiscellaneousIndicators table
        sql = """
        INSERT INTO MiscellaneousIndicators (Year, CountryID, UrbanPopGrowth)
        VALUES (%s, %s, %s);
        """

        # Execute the SQL query
        cur.execute(sql, (year, current_country_id, urban_pop_growth))

    except (psycopg2.Error, KeyError, TypeError) as e:
        print(f"Error occurred: {e}")
        success = False
        break

# Commit changes to the database if no errors occurred
if success:
    conn.commit()
    print("Data inserted successfully!")
else:
    print("Data insertion failed.")

# Close communication with the database
cur.close()
conn.close()

# Visualization 1
import psycopg2
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query to retrieve CountryID, CountryName, Year, and GDPGrowth from EconomicIndicators and CountryInfo tables
    query = """
        SELECT CI.CountryName, EI.Year, EI.GDPGrowth
        FROM CountryInfo CI
        INNER JOIN EconomicIndicators EI ON CI.CountryID = EI.CountryID;
    """
    cur.execute(query)
    combined_data = cur.fetchall()

    # Close communication with the database
    cur.close()
    conn.close()

    # Plotting
    plt.figure(figsize=(10, 6))
    for country_name in set([row[0] for row in combined_data]):  # Plot for each unique country
        country_gdp_growth = [row[2] for row in combined_data if row[0] == country_name]
        country_years = [row[1] for row in combined_data if row[0] == country_name]
        plt.plot(country_years, country_gdp_growth, label=country_name)

    plt.xlabel('Year')
    plt.ylabel('GDP Growth')
    plt.title('GDP Growth of Different Countries over Years')
    plt.legend()
    plt.grid(True)
    plt.show()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

# Visualization 2
import psycopg2
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Duke#7539',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query to retrieve SubRegion, AgriValAddGDP, and FertRate columns with non-null values
    query = """
    SELECT ci.SubRegion, ei.AgriValAddGDP, ei.FertRate
    FROM CountryInfo ci
    JOIN EconomicIndicators ei ON ci.CountryID = ei.CountryID
    WHERE ei.AgriValAddGDP IS NOT NULL AND ei.FertRate IS NOT NULL;
    """
    cur.execute(query)
    data = cur.fetchall()

    # Separate the retrieved data into separate lists for plotting
    subregions = [row[0] for row in data]
    agri_values = [row[1] for row in data]
    fert_rates = [row[2] for row in data]

    # Create a scatterplot
    plt.figure(figsize=(10, 6))
    for i, subregion in enumerate(subregions):
        plt.scatter(agri_values[i], fert_rates[i], label=subregion, alpha=0.7)

    # Add labels and title
    plt.title('Correlation between AgriValAddGDP and FertRate (Non-null values)')
    plt.xlabel('AgriValAddGDP')
    plt.ylabel('FertRate')
    plt.legend(title='SubRegion', loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Close communication with the database
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

# Visualization 3 
import folium

# Create a map centered around the USA and Canada
m = folium.Map(location=[56.1304, -106.3468], zoom_start=4)  # Centered coordinates for North America

# Add markers for USA and Canada
folium.Marker([37.0902, -95.7129], tooltip='USA').add_to(m)  # USA coordinates
folium.Marker([56.1304, -106.3468], tooltip='Canada').add_to(m)  # Canada coordinates

# Display the map
m

# Visualization 4
import psycopg2
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

# Get user input for the year
user_year = input("Enter the year: ")

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query to retrieve UrbanPopGrowth based on user input year
    query = f"SELECT mi.UrbanPopGrowth FROM CountryInfo ci JOIN MiscellaneousIndicators mi ON ci.CountryID = mi.CountryID WHERE mi.Year = {user_year};"
    cur.execute(query)
    urban_pop_growth = cur.fetchall()

    # Close communication with the database
    cur.close()
    conn.close()

    # Flatten the retrieved data to create a histogram
    urban_pop_growth = [value[0] for value in urban_pop_growth if value[0] is not None]  # Filter out None values

    # Plotting histogram
    plt.figure(figsize=(8, 6))
    plt.hist(urban_pop_growth, bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of Urban Population Growth for the year {user_year}')
    plt.xlabel('Urban Population Growth')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 5
import psycopg2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Query to retrieve specified columns from EconomicIndicators table
    query = "SELECT GDP, AgriValAddGDP, DomCreditGDP FROM EconomicIndicators;"

    # Read data directly into a pandas DataFrame
    economic_data = pd.read_sql_query(query, conn)

    # Calculate the correlation matrix
    correlation_matrix = economic_data.corr()

    # Plot heatmap using Seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Economic Indicators')
    plt.show()

    # Close communication with the database
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 6
 import psycopg2
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query to retrieve ImportsGDP column from EconomicIndicators table
    query = "SELECT ImportsGDP FROM EconomicIndicators;"
    cur.execute(query)
    importsgdp_data = cur.fetchall()

    # Close communication with the database
    cur.close()
    conn.close()

    # Extracting data from the result
    importsgdp_values = [row[0] for row in importsgdp_data if row[0] is not None]

    # Creating a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(importsgdp_values, labels=None, autopct='%1.1f%%', startangle=140)
    plt.title('Contribution of Imports to GDP')

    # Show pie chart
    plt.show()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 7 
import psycopg2
import matplotlib.pyplot as plt

# Your database configuration here...

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query to retrieve ExportGDP, ImportsGDP, and CountryID columns from EconomicIndicators table
    query = "SELECT ExportSGDP, ImportsGDP, CountryID FROM EconomicIndicators;"
    cur.execute(query)
    economic_data = cur.fetchall()

    # Close communication with the database
    cur.close()
    conn.close()

    # Data processing and filtering out None values
    data = [(row[0] or 0, row[1] or 0, row[2]) for row in economic_data]  # Replace None with 0

    # Unpack data into separate lists
    exports = [row[0] for row in data]
    imports = [row[1] for row in data]
    countries = [row[2] for row in data]

    # Plotting stacked area chart
    plt.figure(figsize=(10, 6))
    plt.stackplot(countries, exports, imports, labels=['ExportGDP', 'ImportsGDP'])
    plt.xlabel('Country ID')
    plt.ylabel('GDP')
    plt.title('ExportGDP vs ImportsGDP for different countries')
    plt.legend()
    plt.show()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 8 
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Query to retrieve MortRateU5 and CountryID columns from DemographicIndicators table
    query_demographic = "SELECT MortRateU5, CountryID FROM DemographicIndicators;"
    demographic_df = pd.read_sql(query_demographic, conn)

    # Query to retrieve Region from CountryInfo table
    query_country = "SELECT Region FROM CountryInfo;"
    region_df = pd.read_sql(query_country, conn)

    # Check the structure of the demographic data
    print(demographic_df.head())

    # Combining MortRateU5, CountryID, and Region data into a single DataFrame
    combined_df = pd.concat([demographic_df, region_df], axis=1)
    combined_df.columns = ['MortRateU5', 'CountryID', 'Region']

    # Creating a box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Region', y='MortRateU5', data=combined_df,
                order=combined_df.groupby('Region')['MortRateU5'].median().sort_values().index)
    plt.title('Mortality Rates of Children Under 5 Years Old Across Regions')
    plt.xlabel('Region')
    plt.ylabel('Mortality Rate (U5)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Close communication with the database
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 9 
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Query to retrieve GDP, LifeExpBirth, FertRate columns
    query = """
    SELECT GDP, LifeExpBirth, FertRate
    FROM EconomicIndicators ei
    JOIN DemographicIndicators di ON ei.CountryID = di.CountryID;
    """
    data = pd.read_sql(query, conn)

    # Close communication with the database
    conn.close()

    # Plotting the bubble chart
    plt.figure(figsize=(10, 6))
    plt.scatter(data['lifeexpbirth'], data['fertrate'], s=data['gdp'] / 1e9, alpha=0.5)
    plt.xlabel('Life Expectancy at Birth')
    plt.ylabel('Fertility Rate')
    plt.title('Relationship between GDP, Life Expectancy, and Fertility Rate')
    plt.grid(True)
    plt.show()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualiztion 10 
import psycopg2
import geopandas as gpd
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(**db_config)

    # Query to retrieve GDPGrowth and Region columns
    query = "SELECT GDPGrowth, Region FROM EconomicIndicators INNER JOIN CountryInfo ON EconomicIndicators.CountryID = CountryInfo.CountryID;"
    # You might need to modify the query to fit your schema

    # Fetch data
    gdp_growth_data = []
    region_data = []
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            gdp_growth_data.append(row[0])
            region_data.append(row[1])

    # Close communication with the database
    conn.close()

    # Create a DataFrame with GDP growth and region
    data = {'GDPGrowth': gdp_growth_data, 'Region': region_data}
    df = pd.DataFrame(data)

    # Load shapefile for world map
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge world map with GDP data
    merged = world.merge(df, how='left', left_on='name', right_on='Region')

    # Plot choropleth map
    merged.plot(column='GDPGrowth', cmap='YlGnBu', legend=True)
    plt.title('GDP Growth by Country')
    plt.show()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 11
 import psycopg2
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Query to retrieve GDP and DomCreditGDP columns from EconomicIndicators table
    query = "SELECT GDP, DomCreditGDP FROM EconomicIndicators;"
    cur.execute(query)

    # Fetch the data
    data = cur.fetchall()

    # Create a pandas DataFrame from the fetched data
    df = pd.DataFrame(data, columns=['GDP', 'DomCreditGDP'])

    # Remove rows with NaN values
    df.dropna(inplace=True)

    # Extracting valid rows
    X = df[['GDP']]
    y = df['DomCreditGDP']

    if len(df) > 0:
        # Create and fit the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Display model coefficients and intercept
        print("Coefficients:", model.coef_)
        print("Intercept:", model.intercept_)

        # Plotting the scatterplot and regression line
        plt.scatter(X, y, color='blue', label='Data points')
        plt.plot(X, model.predict(X), color='red', label='Regression line')
        plt.xlabel('GDP')
        plt.ylabel('Domestic Credit to GDP')
        plt.title('Linear Regression: GDP vs Domestic Credit to GDP')
        plt.legend()
        plt.show()
    else:
        print("No valid data points to fit the regression model.")

    # Close communication with the database
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualiztion 12
import matplotlib.pyplot as plt
import squarify  # For tree maps

# Example country names
countries = ['USA', 'Canada', 'Germany', 'France', 'Australia', 'Japan', 'India', 'Brazil']

# Example GDP data (random values for demonstration)
gdp_data = [400, 600, 300, 200, 800, 700, 500, 900]

# Plotting the treemap
plt.figure(figsize=(8, 6))
squarify.plot(sizes=gdp_data, label=countries, alpha=0.8)
plt.axis('off')
plt.title('GDP by Country (Treemap)')
plt.show()

#Visualization 13
import psycopg2
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Query to retrieve LifeExpBirth and MortRateU5 columns from DemographicIndicators table
    query = "SELECT LifeExpBirth, MortRateU5 FROM DemographicIndicators;"
    cur.execute(query)

    # Fetch the data
    data = cur.fetchall()

    # Extracting data into separate lists
    life_exp_birth = [row[0] for row in data]
    mort_rate_u5 = [row[1] for row in data]

    # Create a hexbin plot
    plt.hexbin(life_exp_birth, mort_rate_u5, gridsize=30, cmap='viridis')
    plt.colorbar(label='Count in bin')
    plt.xlabel('Life Expectancy at Birth')
    plt.ylabel('Mortality Rate Under 5')
    plt.title('Hexbin Visualization: Life Expectancy vs Mortality Rate Under 5')
    plt.show()

    # Close communication with the database
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 14
import psycopg2
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Query to retrieve UrbanPopGrowth and Region columns from tables
    query = """
    SELECT MI.UrbanPopGrowth, CI.Region
    FROM MiscellaneousIndicators MI
    JOIN CountryInfo CI ON MI.CountryID = CI.CountryID;
    """
    cur.execute(query)

    # Fetch the data
    data = cur.fetchall()

    # Prepare data for plotting
    regions = []
    urban_pop_growth = []
    for row in data:
        regions.append(row[1])
        urban_pop_growth.append(row[0])

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.stackplot(regions, urban_pop_growth, labels=['UrbanPopGrowth'])
    plt.xlabel('Region')
    plt.ylabel('Urban Population Growth')
    plt.title('Changing Proportions of Urban Population Growth across Regions')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Close communication with the database
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

#Visualization 15
import psycopg2
import matplotlib.pyplot as plt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'lab10',
    'port': 5432
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Query to retrieve SubRegion column from CountryInfo table
    query_subregion = "SELECT SubRegion FROM CountryInfo;"
    cur.execute(query_subregion)
    subregions = cur.fetchall()

    # Query to retrieve AdolFertRate column from EconomicIndicators table
    query_adolfert = "SELECT AdolFertRate FROM EconomicIndicators;"
    cur.execute(query_adolfert)
    adolfert_rates = cur.fetchall()

    # Close communication with the database
    cur.close()
    conn.close()

    # Extracting data into lists
    adolfert_data = [rate[0] for rate in adolfert_rates]
    subregion_data = [subregion[0] for subregion in subregions]

    # Plotting the grouped bar chart
    fig, ax = plt.subplots()
    x = range(len(adolfert_data))
    bar_width = 0.35

    bar1 = ax.bar(x, adolfert_data, bar_width, label='Fert Rate')
    bar2 = ax.bar([i + bar_width for i in x], subregion_data, bar_width, label='SubRegion')

    ax.set_xlabel('Countries')
    ax.set_ylabel('Values')
    ax.set_title('Fert Rate and SubRegion Comparison')
    ax.set_xticks([i + bar_width / 2 for i in x])
    ax.set_xticklabels(subregion_data, rotation=90)
    ax.legend()

    plt.tight_layout()
    plt.show()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)
