CREATE DATABASE lab9;
Use lab9;
-- Table PropertyINFO 
CREATE TABLE PropertyInfo (
    Id INT PRIMARY KEY,
    PosessionStatus VARCHAR(255),
    AvailibilityStartsFrom VARCHAR(255),
    FloorNo VARCHAR(255),
    Commercial VARCHAR(1),
    Developer VARCHAR(255),
    ApprovedAuthorityName VARCHAR(225),
    UnitsAvailable FLOAT,
    Price FLOAT,
    PriceEnglish VARCHAR(20),
    FlooringType VARCHAR(255),
    ElectricityStatus VARCHAR(255),
    MaintenanceType VARCHAR(255),
    MaintenanceCharges FLOAT,
    BookingAmount FLOAT
);
-- Property Details 
CREATE TABLE PropertyDetails (
    Id INT PRIMARY KEY,
    Landmark VARCHAR(2000),
    CoveredArea FLOAT,
    ProjectName VARCHAR(255),
    SqftPrice FLOAT,
    CarpetArea FLOAT,
    AreaName VARCHAR(255),
    PropertyUniqueness VARCHAR(255),
    UnitOfCarpetArea VARCHAR(255),
    Society VARCHAR(1),
    OwnershipType VARCHAR(255),
    FurnishedType VARCHAR(255),
    Bathroom FLOAT,
    Parking VARCHAR(255),
    PropertyInfoId INT,
    FOREIGN KEY (PropertyInfoId) REFERENCES PropertyInfo(Id)
);

select * from PropertyDetails;
select * from PropertyInfo;