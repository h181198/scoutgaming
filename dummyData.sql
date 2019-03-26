  INSERT INTO departments (country, unit) VALUES
  ('Norway', 'Oslo'),
  ('Norway', 'Bergen'),
  ('Danmark', 'Aalborg'),
  ('England', 'Wales');

  INSERT INTO receipts VALUES
  (12018, 1, 2018),
  (22018, 2, 2018),
  (22019, 2, 2019);

  INSERT INTO employees VALUES
  ('1', 1, 'Ingrid', '2018-01-22', null),
  ('2', 1, 'Ida', '2018-02-01', null),
  ('3', 2, 'Helene', '2018-03-21', null),
  ('4', 3, 'Nora', '2018-04-23', null);

  INSERT INTO equipments (price, model, buy_date, receipt_id, description, note) VALUES
  (2000, '2019', '2019-03-13', 22019, 'GamingPc Windows10', 'Ha i felles areal'),
  (2000, '2019', '2019-03-13', 22019, 'GamingPc Windows10', 'Ha i felles areal'),
  (2000, '2019', '2019-03-13', 22019, 'GamingPc Windows10', 'Ha i felles areal'),
  (2000, '2019', '2019-03-13', 22018, 'Flatskjerm', 'Ha i felles areal');

  INSERT INTO transactions (equipment_id, employee_id, transfer_date) VALUES
  (1, '1', '2018-01-22'),
  (1, '1', '2018-01-22'),
  (2, '2', '2018-01-22'),
  (3, '3', '2018-01-22'),
  (4, '4', '2018-01-22');
