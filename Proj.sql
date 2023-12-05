 CREATE DATABASE parking_system; -- creating database
-----------
USE parking_system;
----------
-- After that create the Members table
CREATE TABLE Members (   
   name VARCHAR(100),
   floridatechID  INT(100),
    email VARCHAR(100),
    phoneNumber INT(20)
);

-- Create the ParkingPasses table
CREATE TABLE ParkingPasses (
    passNumber INT(20),
    numberPlate VARCHAR(10),
    expirationDate DATE
    );
-- Create the ParkingLots table
CREATE TABLE ParkingLots (
    lot_name VARCHAR(100) ,
    lot_type ENUM('OnCampus', 'OffCampus', 'Staff'),
    capacity INT,
    current_occupancy INT,
    location VARCHAR(100)
);

   INSERT INTO Members (name, floridatechID, email, phoneNumber)
    VALUES ('Mr Bean', 900, 'bean2023@my.fit.edu', 1234567890);
   
   INSERT INTO ParkingPasses (passNumber, numberPlate, expirationDate)
   VALUES (987654, 'ABC123', '2023-12-31');

   INSERT INTO ParkingLots (lot_name, lot_type, capacity, current_occupancy, location)
   VALUES ('Lot B', 'OnCampus', 100, 75, 'Clemente');

