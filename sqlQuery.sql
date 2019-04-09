DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS equipments CASCADE;
DROP TABLE IF EXISTS departments CASCADE;
DROP TABLE IF EXISTS receipts CASCADE;

CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    country VARCHAR(128) NOT NULL,
    unit VARCHAR(256) NOT NULL
);

CREATE TABLE receipts (
    id VARCHAR(64) PRIMARY KEY,
    supplement VARCHAR(256) NOT NULL,
    year INTEGER NOT NULL
);

CREATE TABLE employees (
    id VARCHAR(64) PRIMARY KEY,
    department_id INTEGER,
    name VARCHAR(256) NOT NULL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments (id)
);

CREATE TABLE equipments (
    id SERIAL PRIMARY KEY,
    currency CHAR(3),
    price INTEGER NOT NULL,
    model VARCHAR(128),
    buy_date DATE,
    receipt_id VARCHAR(64),
    description VARCHAR(256),
    note VARCHAR(256),
    FOREIGN KEY (receipt_id) REFERENCES receipts (id)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    equipment_id INTEGER,
    employee_id VARCHAR(64),
    transfer_date DATE NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipments (id),
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);