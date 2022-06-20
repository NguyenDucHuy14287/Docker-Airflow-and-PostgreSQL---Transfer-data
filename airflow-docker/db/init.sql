CREATE TABLE transactions (
   id SERIAL PRIMARY KEY,
   creation_date varchar NOT NULL,
   sale_value bigint NOT NULL
);

INSERT INTO transactions (id, creation_date, sale_value)
VALUES
    (1, '2022-06-11', 1000),
    (2, '2022-06-12', 2000),
    (3, '2022-06-13', 3000);