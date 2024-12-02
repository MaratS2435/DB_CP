INSERT INTO hotels (hotel_id, place, manager) VALUES
(1, 'New York', NULL),
(2, 'Rome', NULL),
(3, 'Casablanca', NULL),
(4, 'Osaka', NULL);

INSERT INTO users (user_id, password, name, age, status, role, hotel_id, affilation_id) VALUES
(1, '$2b$12$P9fmGuHnm26Uv2LlBzQP3.vRACAAhNHPlqU5cZKD2M/PX/Z77leYa', 'Winston Scott', 55, 'alive', 'manager', 1, NULL),
(2, '$2b$12$/NXvswD4WqTNw4Vbkcn5T.DW3nHFNxvXBa/6XZcwWbzOPnyMtnGLW', 'Julius', 30, 'alive', 'manager', 2, NULL),
(3, '$2b$12$gjYdEFrjZASoHUHqysewveOvCGVXJBRS9PsRevT8H0mhF1GJ1L1tO', 'Sofia Al-Azwar', 35, 'alive', 'manager', 3, NULL),
(4, '$2b$12$nv.LXtrd2vDPhdCAGTjNeezxpgI0ocU5oenFqtYCKn/purgwzuG.e', 'Koji Shimazu', 50, 'alive', 'manager', 4, NULL),
(5, '$2b$12$G4CI9Y12sXm63RtlSHAJC.CbSEgZnycSO94qusLRY9.b.oltJ9zBa', 'The Director', 55, 'alive', NULL, 1, NULL),
(6, '$2b$12$WKp61/McF4QHLmIH9NzewOzykgMAKz/pp/oEPt.lO6/EWhbJxvSau', 'Gianna DAntonio', 55, 'alive', NULL, 2, NULL),
(7, '$2b$12$G1LVW0sMIUG1Iob1fM8R4uSdeq88iDS7K5FjZZaKc0ZOZFBnYRmXm', 'The Bowery King', 50, 'alive', NULL, 1, NULL),
(8, '$2b$12$bIwCSVgOFFVGg4orGNpA6.pI1RRcL4WJxX4wkVpQwnaf2AhUvhfQa', 'John Wick', 40, 'alive', 'killer', 1, NULL),
(9, '$2b$12$p/74/4mY.Fv.OgjWz/Z34OhKJcEL2m2B6PpiYndSw41X4fICBbtfO', 'Caine', 40, 'retired', 'killer', 1, NULL),
(10, '$2b$12$R60TrrmzPZu0VBhXoZg1yOd8ESjkrrrUp0wnDuQy4hA/Gn8BISiB.', 'Ares', 30, 'alive', 'killer', 2, NULL),
(11, '$2b$12$EmG4ISlmQiAOhSXzbx9nseVdQeE4Mdea.pb0CkCvbJMqcXsAJsDOq', 'Earl', 32, 'alive', 'killer', 1, NULL);

UPDATE hotels SET manager = 1 WHERE hotel_id = 1;
UPDATE hotels SET manager = 2 WHERE hotel_id = 2;
UPDATE hotels SET manager = 3 WHERE hotel_id = 3;
UPDATE hotels SET manager = 4 WHERE hotel_id = 4;

INSERT INTO affilations (affilation_id, name, head_id) VALUES
(1, 'Ruska Roma', 5),
(2, 'Camorra', 6),
(3, 'The Soup Kitchen', 7);

UPDATE users SET affilation_id = 1 WHERE user_id = 5;
UPDATE users SET affilation_id = 1 WHERE user_id = 8;
UPDATE users SET affilation_id = 2 WHERE user_id = 6;
UPDATE users SET affilation_id = 2 WHERE user_id = 10;
UPDATE users SET affilation_id = 3 WHERE user_id = 7;
UPDATE users SET affilation_id = 3 WHERE user_id = 11;

INSERT INTO rules (rule_id, description) VALUES
(1, 'Отель Continental - это убежище для всех людей, находящихся на его территории.'),
(2, 'Каждый человек, находящийся на территории отеля, должен оплатить свое присутствие, чтобы иметь право на получение убежища'),
(3, 'Клятва на крови, однажды принесенная с помощью Маркера, должна быть соблюдена.'),
(4, 'Помощь или содействие отлучённым запрещается.');
