DROP TABLE IF EXISTS rooms;

CREATE TABLE rooms (
    id INTEGER PRIMARY KEY,
    status INTEGER NOT NULL
);

INSERT INTO rooms(id, status) VALUES (211, 1);
INSERT INTO rooms(id, status) VALUES (212, 0);
INSERT INTO rooms(id, status) VALUES (213, 1);

