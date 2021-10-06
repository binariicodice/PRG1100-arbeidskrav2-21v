DROP SCHEMA IF EXISTS oblig2021;
CREATE SCHEMA IF NOT EXISTS oblig2021;

USE oblig2021;

CREATE TABLE Student
(
Studentnr VARCHAR(6) NOT NULL,
Fornavn VARCHAR(30) NOT NULL,
Etternavn VARCHAR(20) NOT NULL,
Epost VARCHAR(40),
Telefon VARCHAR(8),
CONSTRAINT StudentPK PRIMARY KEY(Studentnr)
);


CREATE TABLE Emne
(
Emnekode CHAR(8) NOT NULL,
Emnenavn CHAR(40) NOT NULL,
Studiepoeng DECIMAL(3, 1),
CONSTRAINT EmnekodePK PRIMARY KEY(Emnekode)
);


CREATE TABLE Rom
(
Romnr CHAR(4) NOT NULL,
Antallplasser INTEGER(3) NOT NULL,
CONSTRAINT RomPK PRIMARY KEY(Romnr)
);

CREATE TABLE Eksamen
(
Emnekode CHAR(8) NOT NULL,
Dato DATE NOT NULL,
Romnr CHAR(4) NOT NULL,
CONSTRAINT EksamenPK PRIMARY KEY(Dato,Emnekode),
CONSTRAINT EksamenEmneFK FOREIGN KEY(Emnekode) REFERENCES Emne(Emnekode),
CONSTRAINT EksamenRomFK FOREIGN KEY(Romnr) REFERENCES Rom(Romnr)
);


CREATE TABLE Eksamensresultat
(
Studentnr CHAR(6) NOT NULL,
Emnekode CHAR(8) NOT NULL,
Dato DATE NOT NULL,
Karakter CHAR(1),
CONSTRAINT EksamensresultatPK PRIMARY KEY(Studentnr,Emnekode,Dato),
CONSTRAINT EksamensresultatStudentFK FOREIGN KEY(Studentnr) REFERENCES Student(Studentnr),
CONSTRAINT EksamensresultatEmneFK FOREIGN KEY(Emnekode) REFERENCES Emne(Emnekode),
CONSTRAINT EksamensresultatEksamenFK FOREIGN KEY(Dato) REFERENCES Eksamen(Dato)
);

INSERT INTO Student (Studentnr, Fornavn, Etternavn, Epost, Telefon) VALUES
('225087', 'Bjørnar', 'Borge', '225087@usn.no', '94888826'),
('139959', 'Alexander', 'Aas', '139959@usn.no', '99033932'),
('240202', 'Halvor', 'Asbjørnhus Skøien', '240202@student.usn.no', '45798628'),
('884642', 'Even Kåre', 'Myklebust', '884642@usn.no', '90505208'),
('240225', 'Henrik Holstad', 'Hauge', '240225@usn.no', '32138942');

INSERT INTO Emne (Emnekode, Emnenavn, Studiepoeng) VALUES
("PRG1000", "Grunnleggende programmering 1", 7.5),
("PRG1100", "Grunnleggende programmering 2", 7.5),
("WEB1100", "Webutvikling og HCI", 7.5),
("SYS1000", "Systemutvikling", 7.5),
("ORL1100", "Organisering", 7.5);

INSERT INTO Rom (Romnr, Antallplasser) VALUES
("A101", 22),
("A102", 25),
("A103", 25),
("A201", 50);

INSERT INTO Eksamen(Dato, Emnekode, Romnr) VALUES
("20210505", "PRG1000", "A101"),
("20210506", "PRG1100", "A101"),
("20210507", "SYS1000", "A101"),
("20210606", "PRG1000", "A201"),
("20210505", "SYS1000", "A103"),
("20211020", "ORL1100", "A103");

INSERT INTO Eksamensresultat(Karakter,Studentnr,Emnekode,Dato) VALUES
("A","240202","PRG1000","20210505"),
("C","240202","PRG1100","20210506"),
("B","240202","SYS1000","20210507"),
("A","225087","PRG1100","20210506"),
(NULL,"225087","SYS1000","20210507"),
(NULL,"240225","SYS1000","20210507"),
(NULL,"884642","SYS1000","20210507"),
("C","139959","PRG1000","20210505"),
("B","240202","PRG1000","20210606");

-- Lage bruker og gi full tilgang
CREATE USER "Eksamenssjef"@"localhost" IDENTIFIED BY "oblig2021";
GRANT ALL ON oblig2021.* TO "Eksamenssjef"@"localhost";

SELECT Eksamensresultat.*, Emnenavn, Studiepoeng
FROM Eksamensresultat, Emne
WHERE Eksamensresultat.Emnekode = Emne.Emnekode 
ORDER BY RIGHT (Eksamensresultat.Emnekode, 4) ASC;

SELECT Eksamensresultat.*, Emnenavn, Studiepoeng
FROM Eksamensresultat, Emne
WHERE Eksamensresultat.Emnekode = Emne.Emnekode
	AND Eksamensresultat.Karakter IS NOT NULL
ORDER BY RIGHT (Eksamensresultat.Emnekode, 4) ASC;

SELECT Vare1.VNr, Vare1.Betegnelse, Vare1.KatNr, Vare1.Pris
FROM Vare AS Vare1
WHERE Vare1.Pris = 
	(SELECT MIN(Vare2.Pris)
    FROM Vare AS Vare2
    WHERE Vare1.KatNr = Vare2.KatNr)
ORDER BY KatNr;

SELECT *
FROM Student;
SELECT Eksamen.Romnr 
FROM Eksamen;
SELECT *
FROM Eksamen;

SELECT Eksamen.Dato,Eksamen.Romnr 
FROM Eksamen 
WHERE Eksamen.Dato = '2021-05-05' AND Eksamen.Romnr = 'A101';

SELECT *
FROM Emne;

SELECT Eksamen.Dato,Eksamen.Romnr FROM Eksamen WHERE Eksamen.Dato = '2021-05-05' AND Eksamen.Romnr = 'A101';

SELECT Studentnr, Emnekode, Dato 
FROM Student, Eksamen;

SELECT *
FROM Eksamen
WHERE Dato BETWEEN '2021-05-05' AND '2021-05-07'
ORDER BY Dato;

SELECT *
FROM Eksamensresultat;

SELECT Studentnr, Emnekode, Dato, Karakter
FROM Eksamensresultat
WHERE Emnekode ='PRG1100' AND Dato = '2021.05.06';