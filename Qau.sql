CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(25) NOT NULL,
    description TEXT,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    description TEXT,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);