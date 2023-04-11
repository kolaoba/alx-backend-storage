-- Create a table users with the following attributes:
-- id: INT, not null, auto increment, primary key
-- email: VARCHAR(255), not null
-- name: VARCHAR(255)
CREATE TABLE IF NOT EXISTS holberton.users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);