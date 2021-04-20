CREATE TABLE visitors (id SERIAL PRIMARY KEY, time TIMESTAMP);
CREATE TABLE statuses (id SERIAL PRIMARY KEY, value INTEGER, description TEXT);
CREATE TABLE wages (id SERIAL PRIMARY KEY, description TEXT, hour_wage INTEGER);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT, role INTEGER, wage_id INTEGER REFERENCES wages);
CREATE TABLE categories (id SERIAL PRIMARY KEY, value INTEGER, description TEXT);
CREATE TABLE chores (id SERIAL PRIMARY KEY, description TEXT, responsible_id INTEGER REFERENCES users, minutes INTEGER, status_id INTEGER REFERENCES statuses, category_id INTEGER REFERENCES categories, salary_amount INTEGER);
