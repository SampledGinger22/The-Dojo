INSERT INTO dojos (name, created_at, updated_at)
VALUES ("The Dojo", now(), now());
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("Kung Pow Dojo", now(), now());
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("Ten Rings Dojo", now(), now());

DELETE FROM dojos
WHERE id < 4;

INSERT INTO dojos (name, created_at, updated_at)
VALUES ("The Dojo", now(), now());
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("Kung Pow Dojo", now(), now());
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("Ten Rings Dojo", now(), now());

-- Manually adjusted ID for each dojo prior to next step

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Stevie", "Jones", 25, now(), now(), 1);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Johnny", "Knoxville", 75, now(), now(), 1);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Stewie", "Griffin", 2, now(), now(), 1);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Yoana", "Franco", 25, now(), now(), 2);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Nick", "Smith", 31, now(), now(), 2);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Mason", "Britsch", 27, now(), now(), 2);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Jesus", "Christ", 70000, now(), now(), 3);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Darth", "Vader", 151, now(), now(), 3);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Baby", "Yoda", 125, now(), now(), 3);

SELECT * FROM ninjas
WHERE dojo_id = 1;

SELECT * from ninjas
WHERE dojo_id = (SELECT MAX(dojo_id) from ninjas);

SELECT * from ninjas
WHERE id = (SELECT MAX(id) from ninjas);

