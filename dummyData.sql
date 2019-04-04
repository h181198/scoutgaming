  INSERT INTO departments (country, unit) VALUES
  ('Norway', 'Bergen'),
  ('Ukraina', 'Lviv Administration'),
  ('Ukraina', 'Lviv Development'),
  ('Ukraina', 'Lviv Stat Center');

  INSERT INTO receipts VALUES
  ('201459-1', '59', 2014),
  ('201459-2', '59', 2014),
  ('2014247', '247', 2014),
  ('2014473', '473', 2014),
  ('2014X', 'X', 2014),
  ('2015160-1', '160', 2015),
  ('2015160-2', '160', 2015),
  ('2015503', '503', 2015),
  ('2015222', '222', 2015),
  ('2015461', '461', 2015),
  ('2015449-1', '449', 2015),
  ('2015449-2', '449', 2015),
  ('2015868-2', '868', 2015),
  ('2015868-3', '868', 2015),
  ('2015868-1', '868', 2015),
  ('2015X', 'X', 2015),
  ('2016394-1', '394', 2016),
  ('2016394-2', '394', 2016),
  ('2016394-3', '394', 2016),
  ('2016AP121', 'AP121', 2016),
  ('2016BA234-1', 'BA234', 2016),
  ('2016BA234-2', 'BA234', 2016),
  ('2016BA234-3', 'BA234', 2016),
  ('20162017-221', '2017-221', 2017),
  ('2016AP84', 'AP84', 2016),
  ('2016X', 'X', 2016),
  ('20162018-X2', '2018-X2', 2018),
  ('2016BA245', 'BA245', 2016),
  ('2017BA197', 'BA197', 2017),
  ('2017AP34', 'AP34', 2017),
  ('2017AP40-2', 'AP40', 2017),
  ('2017AP40-1', 'AP40', 2017),
  ('2017AP92', 'AP92', 2017),
  ('2017X', 'X', 2017),
  ('2017ER43', 'ER43', 2017),
  ('2017AP240-2', 'AP240', 2017),
  ('2017BA99-1', 'BA99', 2017),
  ('2017BA99-2', 'BA99', 2017),
  ('2017BA99-3', 'BA99', 2017),
  ('2017BA177', 'BA177', 2017),
  ('2017AP282', 'AP82', 2017),
  ('2017AP322', 'AP322', 2017),
  ('2017212', '212', 2017),
  ('2017225', '225', 2017),
  ('2017AP331', 'AP331', 2017),
  ('2017ER98', 'ER98', 2017),
  ('2017AP375', 'AP375', 2017),
  ('2017ER129-2', 'ER129', 2017),
  ('2017ER129-1', 'ER129', 2017),
  ('2018ER10-2', 'ER10', 2018),
  ('2018ER10-1', 'ER10', 2018),
  ('2018AP33-1', 'AP33', 2018),
  ('2018AP33-2', 'AP33', 2018),
  ('2018AP33-3', 'AP33', 2018),
  ('2018AP33-4', 'AP33', 2018),
  ('2018AP49', 'AP49', 2018),
  ('2018ER3-1', 'ER3', 2018),
  ('2018ER3-2', 'ER3', 2018),
  ('2018AP66-1', 'AP66', 2018),
  ('2018AP66-2', 'AP66', 2018),
  ('2018AP66-3', 'AP66', 2018),
  ('2018AP66-4', 'AP66', 2018),
  ('2018ER32', 'ER32', 2018),
  ('2018AP115', 'AP115', 2018),
  ('2018AP111-1', 'AP111', 2018),
  ('2018AP111-2', 'AP111', 2018),
  ('2018AP111-3', 'AP111', 2018),
  ('2018AP111-4', 'AP111', 2018),
  ('2018AP111-5', 'AP111', 2018),
  ('2018ER40', 'ER40', 2018),
  ('2018AP308', 'AP308', 2018),
  ('2018AP324', 'AP324', 2018),
  ('2018ER81', 'ER81', 2018),
  ('2018ER95', 'ER95', 2018),
  ('2018269-1', '269', 2018),
  ('2018269-2', '269', 2018),
  ('2018269-3', '269', 2018),
  ('2018ER114-13', 'ER114', 2018),
  ('2018ER114-15', 'ER114', 2018),
  ('2018ER114-16', 'ER114', 2018);

____________________
CREATE TABLE employees (
    id VARCHAR(64) PRIMARY KEY,
    department_id INTEGER,
    name VARCHAR(256) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments (id)
);

1 ('Norway', 'Bergen'),
2  ('Ukraina', 'Lviv Administration'),
3  ('Ukraina', 'Lviv Development'),
4  ('Ukraina', 'Lviv Stat Center');
_________________

  INSERT INTO employees VALUES
  ('1', 1, 'Tove Nordtveit', '2017-01-01', null),
  ('3', 1, 'Andreas Sundal', '2017-01-01', null),
  ('5', 1, 'Antonina Forkun Sundal', '2017-01-01', null),
  ('7', 1, 'Mathias Sundal', '2018-09-17', null),
  ('8', 1, 'Tony A. Sæle', '2017-01-01', null),
  ('9', 1, 'Øystein Østebø Olsen', '2017-01-01', null),
  ('10', 1, 'Loken Makwana', '2017-01-01', null),
  ('11', 1, 'Bjørn Furnes Fjellby', '2017-01-01', null),
  ('12', 1, 'Hege Remme', '2017-01-01', null),
  ('13', 1, 'Torbjørn Angeltveit', '2017-01-01', null),
  ('14', 1, 'Stian Skjøndal', '2017-01-01', null),
  ('15', 1, 'Terje Elde', '2017-06-01', null),
  ('16', 1, 'Mathias Sangolt', '2017-07-03', '2017-08-31'),
  ('18', 1, 'Jemit Butt', '2017-06-19', '2017-06-30'),
  ('20', 1, 'Stian Lysvold Haugse', '2017-07-24', null),
  ('21', 1, 'Helene Konstantine Thømt Dunlop', '2017-10-09', null),
  ('22', 1, 'Aristotelis Giannopoulos', '2017-11-01', '2019-01-03'),
  ('23', 1, 'Emil Møller', '2018-01-08', null),
  ('24', 1, 'Nikolas van Etten', '2018-03-01', '2018-12-10'),
  ('25', 1, 'Eirik Ulversoy', '2018-09-03', null),
  ('26', 1, 'Mikal Meltvik', '2018-09-03', null),
  ('27', 1, 'Jan Olav Sjåvik', '2018-09-06', null),
  ('28', 1, 'Kevin Trivedi', SETT INN VERDI, null),


MÅ SETTE INN RESTEN :) :)

  ('3', 2, 'Helene', '2018-03-21', null),
  ('4', 3, 'Nora', '2018-04-23', null);


CREATE TABLE equipments (
    id SERIAL PRIMARY KEY,
    price INTEGER NOT NULL,
    model VARCHAR(128),
    buy_date DATE,
    receipt_id VARCHAR(64),
    description VARCHAR(256),
    note VARCHAR(256),
    FOREIGN KEY (receipt_id) REFERENCES receipts (id)
);



  INSERT INTO equipments (price, model, buy_date, receipt_id, description, note) VALUES
  (3196, null, '2014-01-23', '201459-1', 'P8 DT Pen-G3220/12G/1T/GT62', null),
  (3196, null, '2014-01-23', '201459-2', 'P8 DT Pen-G3220/12G/1T/GT62', null),
  (6517, '2013', '2014-02-23', '2014247', 'Asus N56JR 15,6" i7/8GB/750GB HDD/SSD', 'Ødelagt skjerm'),
  (5192, '2013', '2014-11-11', '2014473', 'Komplett Office i7-4770S/8GB/120GB', null),
  (0, '2014', '2014-12-01', '2014X', 'Macbook Pro i5 8GB', 'Kjøpt i desember på ebay iflg. Loken'),
  (5432, '2014', '2015-04-16', '2015160-1', 'Mac mini MGEN2D', 'Lviv'),
  (5432, '2014', '2015-04-16', '2015160-2', 'Mac mini MGEN2D', 'Lviv'),
  (5432, '2014', '2015-04-16', '2015503', 'Mac mini MGEN2DH/A', 'Lviv'),
  (6399, '2014', '2015-04-23', '2015222', 'Asus UX305FA-FC004H 13.3" laptop', 'Andreas?'),
  (11992, '2014', '2015-06-29', '2015461', 'Macbook Pro 15" MGXA2HA', 'knust skjerm, brukes som stasjonær'),
  (6072, '2014', '2015-09-01', '2015449-1', 'Iphone 6 64GB Space Gray', null),
  (3112, '2013', '2015-09-01', '2015449-2', 'Iphone 5C 8GB Blue', null),
  (4444, null, '2015-09-01', '2015868-1', 'LG 55"LED/FHD/50Hz/T2CS2', null),
  (4444, null, '2015-09-01', '2015868-2', 'LG 55"LED/FHD/50Hz/T2CS2', 'Utviklerrommet'),
  (4444, null, '2015-09-01', '2015868-3', 'LG 55"LED/FHD/50Hz/T2CS2', 'Utviklerrommet'),

  (4, '2013', '2015-09-01', '2015449-1', '', null),
  (, null, '2014-01-23', '', '', null),
  (, null, '2014-01-23', '', '', null),
  (, null, '2014-01-23', '', '', null),
  (, null, '2014-01-23', '', '', null),
  (, null, '2014-01-23', '', '', null),


  (2000, '2019', '2019-03-13', 22019, 'GamingPc Windows10', 'Ha i felles areal'),
  (2000, '2019', '2019-03-13', 22019, 'GamingPc Windows10', 'Ha i felles areal'),
  (2000, '2019', '2019-03-13', 22018, 'Flatskjerm', 'Ha i felles areal');

  INSERT INTO transactions (equipment_id, employee_id, transfer_date) VALUES
  (1, '1', '2018-01-22'),
  (1, '1', '2018-01-22'),
  (2, '2', '2018-01-22'),
  (3, '3', '2018-01-22'),
  (4, '4', '2018-01-22');
