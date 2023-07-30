-- table ID cant be null
CREATE TABLE IF NOT exists id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);