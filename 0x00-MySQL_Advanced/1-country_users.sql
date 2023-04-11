-- Create a table users with the following attributes:
-- id: INT, not null, auto increment, primary key
-- email: VARCHAR(255), not null
-- name: VARCHAR(255)
-- country: enumeration of the following values: 'US', 'CO', 'TN', never null
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);