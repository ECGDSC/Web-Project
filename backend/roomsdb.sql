DROP TABLE IF EXISTS rooms;

CREATE TABLE rooms (
    id INTEGER PRIMARY KEY,
    status INTEGER NOT NULL
);

INSERT INTO rooms(id, status) VALUES (100, 0);
INSERT INTO rooms(id, status) VALUES (101, 0);
INSERT INTO rooms(id, status) VALUES (103, 0);
INSERT INTO rooms(id, status) VALUES (104, 1);
INSERT INTO rooms(id, status) VALUES (105, 1);
INSERT INTO rooms(id, status) VALUES (106, 0);
INSERT INTO rooms(id, status) VALUES (108, 0);
INSERT INTO rooms(id, status) VALUES (110, 1);
INSERT INTO rooms(id, status) VALUES (111, 0);
INSERT INTO rooms(id, status) VALUES (112, 0);
INSERT INTO rooms(id, status) VALUES (114, 1);
INSERT INTO rooms(id, status) VALUES (300, 1);
INSERT INTO rooms(id, status) VALUES (302, 0);
INSERT INTO rooms(id, status) VALUES (303, 0);
INSERT INTO rooms(id, status) VALUES (304, 1);
INSERT INTO rooms(id, status) VALUES (308, 1);
INSERT INTO rooms(id, status) VALUES (310, 1);
INSERT INTO rooms(id, status) VALUES (312, 1);
INSERT INTO rooms(id, status) VALUES (314, 0);
INSERT INTO rooms(id, status) VALUES (315, 0);
INSERT INTO rooms(id, status) VALUES (316, 0);
INSERT INTO rooms(id, status) VALUES (317, 0);
INSERT INTO rooms(id, status) VALUES (318, 1);

-- INSERT INTO rooms(id, status) VALUES (211, 0);
-- INSERT INTO rooms(id, status) VALUES (212, 0);
-- INSERT INTO rooms(id, status) VALUES (213, 1);
