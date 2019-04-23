  INSERT INTO departments (country, unit) VALUES
  ('Norway', 'Bergen'),
  ('Ukraina', 'Lviv Administration'),
  ('Ukraina', 'Lviv Development'),
  ('Ukraina', 'Lviv Stat Center');

  INSERT INTO receipts VALUES
  ('None','',0000),
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

  INSERT INTO employees (employee_number, department_id, name, start_date, end_date) VALUES
  ('N', NULL, 'None', NULL ,NULL ),
  ('D', NULL, 'DELETED', NULL, NULL),
  ('S', NULL, 'SOLD', NULL, NULL),
  ('G', NULL, 'GONE', NULL, NULL),
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
  ('28', 1, 'Kevin Trivedi', null, null),
  ('UA50', 2, 'Alexandru Gris', '2018-09-17', null),
  ('UA7', 2, 'Anastasiya Kanunikova', null, null),
  ('UA8', 2, 'Mariya-Anna Hryniv', '2015-11-02', null),
  ('UA1', 3, 'Ruslan Banakh', null, null),
  ('UA10', 3, 'Violetta Kubytska', null, '2018-09-28'),
  ('UA11', 3, 'Roxolana Ihorivna Baran', null, null),
  ('UA12', 3, 'Sergiy Melnyk', null, null),
  ('UA13', 3, 'Maksym Vovik', null, null),
  ('UA14', 3, 'Orysia Rudyk', null, null),
  ('UA15', 3, 'Anhelina Kiryk', null, null),
  ('UA16', 3, 'Olha Burak', null, null),
  ('UA17', 3, 'Volodymyr Yatsiuk', null, null),
  ('UA20', 3, 'Ihor Pylypyak', null, null),
  ('UA28', 3, 'Vadym Shevchenko', null, '2018-07-28'),
  ('UA29', 3, 'Olena Muzyka', null, null),
  ('UA30', 3, 'Yuriy Milyan', null, null),
  ('UA31', 3, 'Khrystyna Grebenyuk', null, null),
  ('UA32', 3, 'Andriy Holubokyy', null, null),
  ('UA37', 3, 'Vladyslav Chenstov', '2018-09-25', '2018-03-30'),
  ('UA4', 3, 'Olha Khomyak', null, null),
  ('UA42', 3, 'Oleksandr Zyablikov', '2018-04-16', null),
  ('UA44', 3, 'Marta Kishchak', null, '2018-08-31'),
  ('UA48', 3, 'Oleksandr Lashch', '2018-09-05', null),
  ('UA5', 3, 'Taras Khmelovskyi', null, null),
  ('UA53', 3, 'Ivan Krasnonosov', '2018-09-17', null),
  ('UA54', 3, 'Oleh Murha', '2018-09-24', null),
  ('UA55', 3, 'Rinat Botchenko', '2018-10-03', null),
  ('UA6', 3, 'Roman Husar', null, null),
  ('UA9', 3, 'Olga Tkachenko', null, '2018-08-17'),
  ('UA SC', 4, 'Stat Center', null, null),
  ('UA18', 4, 'Roman Kosmirak', null, '2018-09-26'),
  ('UA19', 4, 'Bogdan Dumych', '2018-06-20', '2018-08-20'),
  ('UA21', 4, 'Maksym Maksymov', null, null),
  ('UA22', 4, 'Mykola Protsko', null, null),
  ('UA23', 4, 'Pavlo Krombet', null, null),
  ('UA24', 4, 'Oleksii Svirskyy', null, null),
  ('UA27', 4, 'Ivan Luzhetskyi', null, null),
  ('UA33', 4, 'Max Asafatov', null, null),
  ('UA34', 4, 'Andriy Bartkiv', null, null),
  ('UA35', 4, 'Ruslan Marchenko', null, null),
  ('UA36', 4, 'Taras Henda', null, null),
  ('UA38', 4, 'Roman Protsko', null, null),
  ('UA39', 4, 'Severyn Stetsyuk', '2018-01-15', null),
  ('UA40', 4, 'Volodymyr Vanchasovych', null, null),
  ('UA41', 4, 'Ivan Shepshelei', '2018-03-19', null),
  ('UA43', 4, 'Dmytro Hryhorchuk', '2018-04-10', null),
  ('UA45', 4, 'Oleksii Fedyk', '2018-06-16', null),
  ('UA46', 4, 'Maksym Fedak', '2018-07-09', null),
  ('UA47', 4, 'Iurii Samaniuk', '2018-07-23', null),
  ('UA49', 4, 'Demian Linnyk', '2018-08-27', null),
  ('UA51', 4, 'Yevhenii Balan', '2018-09-17', null),
  ('UA52', 4, 'Kirill Laschenko', '2018-09-17', '2018-10-26'),
  ('UA56', 4, 'Andrii Kuzmin', '2018-10-02', null),
  ('UA57', 4, 'Marian Vavrynchuk', '2018-10-08', null),
  ('UA61', 3, 'Mykhailo Kobernyk', '2019-01-14', null),
  ('UA62', 4, 'Dimitris Hadjiconstantinou', '2019-01-21', null),
  ('UA63', 3, 'Daria Rudenko', '2019-02-11', null),
  ('NOF', null, 'Free - Bergen', null, null),
  ('NOS', null, 'Storage - Bergen', null, null),
  ('NOO', null, 'Office - Bergen', null, null),
  ('UA', null, 'Lviv Office', null, null),
  ('MT1', null, 'Espen Rød', null, null),
  ('UA58', null, 'Vitaliy Makarets', null, null),
  ('UA59', null, 'Yaryna Barninets', null, null),
  ('UA60', null, 'Volodymyr Bodak', null, null);


  INSERT INTO equipments (currency, price, model, buy_date, receipt_id, description, note) VALUES
  ('NOK', 3196, null, '2014-01-23', '201459-1', 'P8 DT Pen-G3220/12G/1T/GT62', null),
  ('NOK', 3196, null, '2014-01-23', '201459-2', 'P8 DT Pen-G3220/12G/1T/GT62', null),
  ('NOK', 6517, '2013', '2014-02-23', '2014247', 'Asus N56JR 15,6" i7/8GB/750GB HDD/SSD', 'Ødelagt skjerm'),
  ('NOK', 5192, '2013', '2014-11-11', '2014473', 'Komplett Office i7-4770S/8GB/120GB', null),
  ('NOK', 0, '2014', '2014-12-01', '2014X', 'Macbook Pro i5 8GB', 'Kjøpt i desember på ebay iflg. Loken'),
  ('NOK', 5432, '2014', '2015-04-16', '2015160-1', 'Mac mini MGEN2D', 'Lviv'),
  ('NOK', 5432, '2014', '2015-04-16', '2015160-2', 'Mac mini MGEN2D', 'Lviv'),
  ('NOK', 5432, '2014', '2015-04-16', '2015503', 'Mac mini MGEN2DH/A', 'Lviv'),
  ('NOK', 6399, '2014', '2015-04-23', '2015222', 'Asus UX305FA-FC004H 13.3" laptop', 'Andreas?'),
  ('NOK', 11992, '2014', '2015-06-29', '2015461', 'Macbook Pro 15" MGXA2HA', 'knust skjerm, brukes som stasjonær'),
  ('NOK', 6072, '2014', '2015-09-01', '2015449-1', 'Iphone 6 64GB Space Gray', null),
  ('NOK', 3112, '2013', '2015-09-01', '2015449-2', 'Iphone 5C 8GB Blue', null),
  ('NOK', 4444, null, '2015-09-01', '2015868-1', 'LG 55"LED/FHD/50Hz/T2CS2', null),
  ('NOK', 4444, null, '2015-09-01', '2015868-2', 'LG 55"LED/FHD/50Hz/T2CS2', 'Utviklerrommet'),
  ('NOK', 4444, null, '2015-09-01', '2015868-3', 'LG 55"LED/FHD/50Hz/T2CS2', 'Utviklerrommet'),
  ('NOK', 7236, null, '2015-12-16', '2015X', 'Lenovo Y50-70 15.6"', 'kjøpt i 2015, refusjon i 2018'),
  ('NOK', 5592, '2016', '2016-06-10', '2016394-1', 'Samsung Galaxy S7 32GB White', null),
  ('NOK', 3992, '2014', '2016-06-10', '2016394-2', 'Iphone 6 White 16', null),
  ('NOK', 3992, '2014', '2016-06-10', '2016394-3', 'Ipad Air 2 64GB Wifi Grey', null),
  ('NOK', 12791, '2015', '2016-06-21', '2016AP121', 'Macbook Pro 13,3" MF840HA', null),
  ('NOK', 6152, '2014', '2016-07-11', '2016BA234-1', 'Mac mini MGEN2D', 'Lviv'),
  ('NOK', 6152, '2014', '2016-07-11', '2016BA234-2', 'Mac mini MGEN2D', 'Lviv'),
  ('NOK', 3592, '2014', '2016-07-11', '2016BA234-3', 'Ipad Air 2 16GB Silver', 'Bergen eller Lviv?'),
  ('NOK', 6792, '2015', '2016-07-16', '20162017-221', 'Iphone 6S 64GB Silver', null),
  ('NOK', 3192, '2016', '2016-08-31', '2016AP84', 'Bose QC 35 Trådløs Hodetelefon', 'Kjøpt i 2016, Sundal fått refusjon i 2018'),
  ('NOK', 7962, '2015', '2016-09-12', '2016X', 'Macbook Air i5', null),
  ('NOK', 12982, '2016', '2016-10-24', '20162018-X2', 'MSI GE72VR 6RF Apache Pro', null),
  ('NOK', 6552, '2016', '2016-12-20', '2016BA245', 'iPhone 7 128GB Black', null),
  ('NOK', 11192, null, '2017-01-20', '2017BA197', 'Asus UX501VW-FI020T 15,6" laptop', 'returnert. Bråkte. 30.05.2017'),
  ('NOK', 9989, '2015', '2017-03-06', '2017AP34', 'Macbook Pro MF839H/A 13" S/N:C025R6NJFVH3', null),
  ('NOK', 5832, null, '2017-03-09', '2017AP40-2', 'Lenovo ThinkCentre S510', 'Bergen'),
  ('NOK', 5832, null, '2017-03-09', '2017AP40-1', 'Lenovo ThinkCentre S510', null),
  ('NOK', 9975, '2015', '2017-04-27', '2017AP92', 'Macbook Pro 13" MF839H/A S/N: C02T33B6FVH3', null),
  ('NOK', 11314, '2016', '2017-05-30', '2017X', 'Macbook Pro 13", i5, no touch bar, S/N: C02T96JNGY25', null),
  ('NOK', 8939, '2016', '2017-06-28', '2017ER43', 'Iphone 7 128GB Jet Black', null),
  ('NOK', 6072, '2017', '2017-06-30', '2017AP240-2', 'Samsung Galaxy S8 Orchid Grey', null),
  ('NOK', 10470, null, '2017-07-02', '2017BA99-1', 'Custom PC: i7, 16GB, 500GB SSD, GTX1050Ti', 'brukes til videoredigering'),
  ('NOK', 10470, null, '2017-07-02', '2017BA99-3', 'Custom PC: i7, 16GB, 500GB SSD, GTX1050Ti', null),
  ('NOK', 10470, null, '2017-07-02', '2017BA99-2', 'Custom PC: i7, 16GB, 500GB SSD, GTX1050Ti', null),
  ('NOK', 6499, '2017', '2017-07-13', '2017BA177', 'Komplett Silent Office i3-7100/8GB/128GB', null),
  ('NOK', 12232, '2017', '2017-10-16', '2017AP322', 'Microsoft Surface Pro 12,3', null),
  ('NOK', 2712, '2017', '2017-11-13', '2017AP331', 'Ipad 9,7" 32GB Wifi Grå', 'Bergen?'),
  ('NOK', 10631, '2017', '2017-11-20', '2017ER98', 'Macbook Pro 13" MPXR2HA', null),
  ('NOK', 3506, null, '2017-12-06', '2017AP375', 'LG 27UD58-B 27inch Ultra HD 4k monitor', null),
  ('NOK', 6398, null, '2018-01-08', '2018ER10-2', 'HP i5-7400/8/256/GTX1050-2/AC', 'Bergen'),
  ('NOK', 6398, null, '2018-01-08', '2018ER10-1', 'HP i5-7400/8/256/GTX1050-2/AC', 'Bergen'),
  ('NOK', 2700, '2017', '2018-01-25', '2018AP33-1', 'Ipad 9,7" 32GB Wifi Grå', 'Lviv?'),
  ('NOK', 2700, '2017', '2018-01-25', '2018AP33-2', 'Ipad 9,7" 32GB Wifi Grå', 'Bergen?'),
  ('NOK', 5450, '2017', '2018-01-25', '2018AP33-4', 'Samsung Galaxy S8 64GB Sort', 'overlatt til Nik når han sluttet, 11.12.2018'),
  ('NOK', 15050, '2015', '2018-01-25', '2018AP33-3', 'Macbook Pro 15" MJLQ2H/A, C02V8459G8WN', null),
  ('NOK', 11192, null, '2018-01-30', '2018AP49', '2 x Dell 27" Led UP2716D', 'står ledig på plassen til Nik'),
  ('NOK', 22391, '2017', '2018-03-05', '2018ER32', 'Macbook Pro 15" MPTT2HA', null),
  ('NOK', 8111, '2017', '2018-03-20', '2018AP115', 'Macbook Air', null),
  ('NOK', 14462, '2015', '2018-04-18', '2018ER40', 'Macbook Pro 15" MJLQ2H/A C02VX2Y2G8WN', null),
  ('NOK', 12343, null, '2018-05-25', '2018AP308', 'HP Z2 Mini WorkStation', null),
  ('NOK', 17752, '2017', '2018-06-01', '2018AP324', 'Macbook Pro 13" MPXV2H/A S/N: C02WPOLDHV2Q', null),
  ('NOK', 9991, '2017', '2018-09-17', '2018ER81', 'Macbook Air MQD42H/A', null),
  ('NOK', 19992, '2018', '2018-10-05', '2018ER95', 'Macbook Pro 15" MR962H/A', null),
  ('UAH', 18030, null, '2017-09-30', '2017AP282', null, 'Mohikn mnwkn, kaabn'),
  ('UAH', 11366, '2015', '2017-10-25', '2017212', 'Custom PC i3-6098P/8GB/120GB', null),
  ('UAH', 31299, '2017', '2017-11-02', '2017225', 'Macbook Air MQD32UA/A', null),
  ('UAH', 26234, '2017', '2017-12-25', '2017ER129-2', 'Macbook Air 13" MQD32', null),
  ('UAH', 26234, '2017', '2017-12-25', '2017ER129-1', 'Macbook Air 13" MQD32', null),
  ('UAH', 26654, '2017', '2018-02-05', '2018ER3-2', 'Macbook Air MQD32', null),
  ('UAH', 26654, '2017', '2018-02-05', '2018ER3-1', 'Macbook Air MQD32', null),
  ('UAH', 54716, '2015', '2018-02-06', '2018AP66-4', 'Macbook Pro 15" MJLQ2', null),
  ('UAH', 54716, '2015', '2018-02-06', '2018AP66-2', 'Macbook Pro 15" MJLQ2', null),
  ('UAH', 54716, '2015', '2018-02-06', '2018AP66-1', 'Macbook Pro 15" MJLQ2', null),
  ('UAH', 54716, '2015', '2018-02-06', '2018AP66-3', 'Macbook Pro 15" MJLQ2', null),
  ('UAH', 59587, '2017', '2018-03-26', '2018AP111-1', 'Macbook Pro 15" MPTU2', null),
  ('UAH', 59587, '2017', '2018-03-26', '2018AP111-2', 'Macbook Pro 15" MPTU2', null),
  ('UAH', 59587, '2017', '2018-03-26', '2018AP111-3', 'Macbook Pro 15" MPTU2', null),
  ('UAH', 59587, '2017', '2018-03-26', '2018AP111-4', 'Macbook Pro 15" MPTU2', null),
  ('UAH', 59587, '2017', '2018-03-26', '2018AP111-5', 'Macbook Pro 15" MPTU2', null),
  ('UAH', 17151, null, '2018-10-11', '2018269-1', 'Custom PC Pentium G5400/8GB/GT710/120GB', null),
  ('UAH', 17151, null, '2018-10-11', '2018269-2', 'Custom PC Pentium G5400/8GB/GT710/120GB', null),
  ('UAH', 17151, null, '2018-10-11', '2018269-3', 'Custom PC Pentium G5400/16GB/GT710/120GB', null),
  ('UAH', 39101, '2018', '2018-11-29', '2018ER114-16', 'Asus UX430UN-GV043T', null),
  ('UAH', 18216, null, '2018-11-22', '2018ER114-13', 'PowerWalker VFI 2000 RT UPS', null),
  ('UAH', 42209, '2018', '2018-11-30', '2018ER114-15', 'Macbook Air MRE82 SFVFXKCPXJK77', null);


  INSERT INTO transactions (equipment_id, employee_id, transfer_date) VALUES
  (32, 4, '2017-03-09'),
  (53, 4, '2018-03-20'),
  (4, 5, '2014-11-11'),
  (25, 5, '2016-08-31'),
  (30, 5, '2017-03-06'),
  (44, 5, '2017-12-06'),
  (41, 5, '2019-01-01'),
  (57, 7, '2018-09-17'),
  (37, 7, '2019-01-16'),
  (20, 8, '2016-06-21'),
  (27, 8, '2016-10-24'),
  (36, 8, '2017-06-30'),
  (37, 8, '2017-07-02'),
  (3, 9, '2014-02-23'),
  (39, 9, '2017-07-02'),
  (30, 9, '2019-01-14'),
  (5, 10, '2014-12-01'),
  (28, 10, '2016-12-20'),
  (55, 10, '2018-05-25'),
  (33, 11, '2017-04-27'),
  (35, 11, '2017-06-28'),
  (26, 12, '2016-09-12'),
  (46, 12, '2018-01-08'),
  (10, 13, '2015-06-29'),
  (24, 13, '2016-07-16'),
  (41, 13, '2017-10-16'),
  (56, 13, '2018-06-01'),
  (37, 13, '2019-01-01'),
  (16, 14, '2015-12-16'),
  (38, 14, '2017-07-02'),
  (54, 14, '2018-04-18'),
  (34, 15, '2017-06-01'),
  (40, 18, '2017-07-13'),
  (50, 18, '2019-01-16'),
  (43, 19, '2017-11-20'),
  (50, 21, '2018-03-05'),
  (52, 21, '2018-12-17'),
  (50, 22, '2018-01-25'),
  (49, 22, '2018-01-25'),
  (51, 22, '2018-01-30'),
  (52, 22, '2018-03-05'),
  (58, 22, '2018-10-05'),
  (50, 25, '2018-12-17'),
  (29, 3, '2017-05-30'),
  (49, 3, '2018-12-10'),
  (3, 3, '2019-01-16'),
  (16, 88, '2018-07-01'),
  (51, 84, '2018-12-11'),
  (14, 86, '2018-08-01'),
  (15, 86, '2018-08-01'),
  (13, 85, '2018-08-01'),
  (79, 87, '2018-11-22'),
  (75, 56, '2018-10-11'),
  (76, 56, '2018-10-11'),
  (77, 56, '2018-10-11'),
  (68, 30, '2018-02-06'),
  (70, 31, '2018-03-26'),
  (71, 32, '2018-03-26'),
  (69, 33, '2018-02-06'),
  (62, 36, '2017-12-25'),
  (63, 38, '2017-12-25'),
  (72, 39, '2018-07-28'),
  (61, 61, '2017-11-02'),
  (72, 40, '2018-03-26'),
  (73, 42, '2018-03-26'),
  (66, 44, '2018-02-06'),
  (70, 44, '2018-09-28'),
  (65, 46, '2018-02-05'),
  (66, 27, '2018-09-17'),
  (67, 52, '2018-08-17'),
  (78, 89, '2018-11-29'),
  (74, 54, '2018-03-26'),
  (80, 28, '2018-11-30'),
  (64, 29, '2018-02-05'),
  (67, 55, '2018-02-06'),
  (50, 27, '2019-01-23'),
  (54, 27, '2019-01-23'),
  (65, 41, '2019-01-24'),
  (50, 53, '2019-01-24'),
  (54, 46, '2019-01-24');

