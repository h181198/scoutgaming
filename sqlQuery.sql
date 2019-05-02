DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS equipments CASCADE;
DROP TABLE IF EXISTS departments CASCADE;
DROP TABLE IF EXISTS receipts CASCADE;

CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    country VARCHAR(128) NOT NULL,
    unit VARCHAR(128) NOT NULL
);

CREATE TABLE receipts (
    id SERIAL PRIMARY KEY,
    comb_id VARCHAR(128),
    supplement VARCHAR(128),
    year INTEGER NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_number VARCHAR(128),
    department_id INTEGER,
    name VARCHAR(128) NOT NULL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments (id)
);

CREATE TABLE equipments (
    id SERIAL PRIMARY KEY,
    currency VARCHAR(128),
    price INTEGER,
    model VARCHAR(128),
    buy_date DATE,
    receipt_id INTEGER,
    description VARCHAR(128),
    note VARCHAR(128),
    FOREIGN KEY (receipt_id) REFERENCES receipts (id)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    equipment_id INTEGER,
    employee_id INTEGER,
    transfer_date DATE NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipments (id),
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);

INSERT INTO employees (employee_number, department_id, name, start_date, end_date) VALUES
  ('N', NULL, 'None', NULL ,NULL ),
  ('D', NULL, 'DELETED', NULL, NULL),
  ('S', NULL, 'SOLD', NULL, NULL),
  ('G', NULL, 'GONE', NULL, NULL);

INSERT INTO receipts (comb_id, supplement, year) VALUES
  ('None','',0000);

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  username VARCHAR (32),
  password VARCHAR (512)

);

INSERT INTO users(username, password) VALUE
  ('Stian', 'e1f057cd9938e3d993688d99cb3bd507fa83c4651aa606a5f4327b763bfd6335');