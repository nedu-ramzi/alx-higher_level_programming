-- creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows

CREATE TABLE IF NOT EXISTS second_table
(id INT, name VARCHAR(256), score INT)
VALUES(1, name = "John", score = 10),
(2, name = "Alex", score = 3),
(3, name = "Bob", score = 14),
(4, name = "George", score = 8);
