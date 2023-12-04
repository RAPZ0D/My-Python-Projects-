CREATE DATABASE world_map_1;

-- Table 1: Population table
CREATE TABLE Population (
    CountryName VARCHAR(255),
    TotalPopulation INT,
    LastUpdatedYear INT,
    PRIMARY KEY (CountryName)
);

-- Table 2: Gross Domestic Product table
CREATE TABLE GrossDomesticProduct (
    LastUpdatedYear INT,
    TotalGDP DECIMAL(18, 2),
    PRIMARY KEY (LastUpdatedYear)
);

-- Table 3: Gross National Income table
CREATE TABLE GrossNationalIncome (
    LastUpdatedYear INT,
    TotalGNI DECIMAL(18, 2),
    PRIMARY KEY (LastUpdatedYear)
);

-- Table 4: Inflation Rates table
CREATE TABLE InflationRates (
    CurrentInflationRate DECIMAL(5, 2),
    LastUpdatedYear INT,
    PRIMARY KEY (LastUpdatedYear)
);
