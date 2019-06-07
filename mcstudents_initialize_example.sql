-- CREATE database People;
use People;

CREATE TABLE MCStudents (
	ID int NOT NULL AUTO_INCREMENT,
    FirstName varchar(255) NOT NULL,
    LastName varchar(255),
    Address varchar(255),
    City varchar(255),
    State varchar(255),
    ZIP varchar(255),
    Phone varchar(255),
    PRIMARY KEY (ID)
);