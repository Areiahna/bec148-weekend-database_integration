CREATE DATABASE library;
USE library;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    availability BOOLEAN DEFAULT 1
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO users (name,email)
VALUES("Batman","batty_boy@gmail.com"),
("Robin","sidekick@yahoo.com"),
("Black Panther","King-TChalla@cboseman.com"),
("Peter Parker","spidey@multiverse.com");

SELECT * FROM users;

INSERT INTO books(title)
VALUES("Holes"),
("Me Before You"),
("No David"),
("Princess and the Frog");

select * FROM books;

INSERT INTO borrowed_books(user_id,book_id)
VALUES (1,2),
(3,4);

select * FROM borrowed_books;

SET SQL_SAFE_UPDATES = 0; 

UPDATE books 
SET availability = 2
WHERE id = 2;

UPDATE books 
SET availability = 2
WHERE id = 4;

SET SQL_SAFE_UPDATES = 1; 


