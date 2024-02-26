DROP TABLE IF EXISTS CST_rooms;

CREATE TABLE CST_rooms (
          rooms_num INTEGER PRIMARY KEY ,
          status BOOLEAN NOT NULL,
          cap INTEGER NOT NULL,
          num_of_whiteboards INTEGER ,
          hours INTEGER  
);

INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (300, 0, 30, 4, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (301, 0, 20, 4, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (302, 0, 3, 2, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (303, 0, 20, 4, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (304, 0, 4, 2, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (305, 0, 2, 4, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (308, 0, 6, 2, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (310, 0, 2, 1, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (312, 0, 3, 1, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (314, 0, 20, 2, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (315, 0, 30, 1, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (316, 0, 10, 1, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (318, 0, 20, 1, 0);
INSERT INTO CST_rooms (rooms_num, status, cap, num_of_whiteboards, hours) VALUES (317, 0, 20, 1, 0);









