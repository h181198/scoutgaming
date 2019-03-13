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
    department_id INTEGER NOT NULL,
    name VARCHAR(256) NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments (id)
);

CREATE TABLE equipments (
    id SERIAL PRIMARY KEY,
    price INTEGER NOT NULL,
    model VARCHAR(128),
    buy_date TIMESTAMP,
    receipt_id VARCHAR(64),
    description VARCHAR(256),
    note VARCHAR(256),
    FOREIGN KEY (receipt_id) REFERENCES receipts (id)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    equipment_id INTEGER NOT NULL,
    employee_id VARCHAR(64) NOT NULL,
    transfer_date TIMESTAMP NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipments (id),
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);