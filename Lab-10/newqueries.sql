CREATE TABLE CountryInfo (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(100),
    Region VARCHAR(50),
    SubRegion VARCHAR(50),
    IntermRegion VARCHAR(50),
    SurfAreaSqKm FLOAT,
    PopDensWW FLOAT,
    PopGrowth FLOAT
);

CREATE TABLE EconomicIndicators (
    Year INT,
    CountryID INT,
    GDP FLOAT,
    GDPGrowth FLOAT,
    AdolFertRate FLOAT,
    AgriValAddGDP FLOAT,
    DomCreditGDP FLOAT,
    ExportsGDP FLOAT,
    FertRate FLOAT,
    FDINetBoP FLOAT,
    GNICapAtlas FLOAT,
    GNIAtlas FLOAT,
    GrossCapFormGDP FLOAT,
    ImportsGDP FLOAT,
    IndValAddGDP FLOAT,
    PRIMARY KEY (Year, CountryID),
    FOREIGN KEY (CountryID) REFERENCES CountryInfo(CountryID)
);

CREATE TABLE DemographicIndicators (
    Year INT,
    CountryID INT,
    LifeExpBirth FLOAT,
    MortRateU5 FLOAT,
    NetMigr FLOAT,
    PopTotal FLOAT
    PRIMARY KEY (Year, CountryID),
    FOREIGN KEY (CountryID) REFERENCES CountryInfo(CountryID)
);

CREATE TABLE TradeIndicators (
    Year INT,
    CountryID INT,
    MerchTradeGDP FLOAT
    PRIMARY KEY (Year, CountryID),
    FOREIGN KEY (CountryID) REFERENCES CountryInfo(CountryID)
);

CREATE TABLE MiscellaneousIndicators (
    Year INT,
    CountryID INT,
    UrbanPopGrowth FLOAT
    PRIMARY KEY (Year, CountryID),
    FOREIGN KEY (CountryID) REFERENCES CountryInfo(CountryID)
);

select * from countryinfo;
select * from demographicindicators;
select * from economicindicators;
select * from miscellaneousindicators;
select * from tradeindicaotrs; 