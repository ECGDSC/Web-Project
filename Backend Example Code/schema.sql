DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO users (name, email) VALUES ("Arata", "arata@earlham.edu");
INSERT INTO users (name, email) VALUES ("Sharon", "sharon@earlham.edu");
INSERT INTO users (name, email) VALUES ("Tien", "tien@earlham.edu");
INSERT INTO users (name, email) VALUES ("Musa", "musa@earlham.edu");
INSERT INTO users (name, email) VALUES ("Parsa", "parsa@earlham.edu");
INSERT INTO users (name, email) VALUES ("Anahit", "anahit@earlham.edu");
INSERT INTO users (name, email) VALUES ("Shun", "shun@earlham.edu");
