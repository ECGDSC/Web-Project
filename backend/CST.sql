DROP TABLE IF EXISTS users;

CREATE CST_rooms (
          rooms_num INTEGER PRIMARY KEY ,
          status TEXT NOT NULL,
          cap TEXT NOT NULL,
          num_of_whiteboards INTEGER PRIMARY KEY,
          hours INTEGER PRIMARY KEY 
);