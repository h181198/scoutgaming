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