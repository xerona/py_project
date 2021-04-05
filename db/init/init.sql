CREATE TABLE player ( id serial PRIMARY KEY, first_name VARCHAR(100) NOT NULL, last_name VARCHAR(100) NOT NULL );

INSERT INTO player (first_name, last_name) VALUES ('lebron', 'james');
INSERT INTO player (first_name, last_name)  VALUES ('stephen', 'curry');
INSERT INTO player (first_name, last_name)  VALUES ('kevin', 'durant');
INSERT INTO player (first_name, last_name)  VALUES ('james', 'harden');
INSERT INTO player (first_name, last_name)  VALUES ('michael', 'jordan');


CREATE TABLE user_account ( id serial PRIMARY KEY, email VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL );
INSERT INTO user_account (email, password) VALUES ('foo@gmail.com', 'foo_pw');
