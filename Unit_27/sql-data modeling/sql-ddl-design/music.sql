-- from the terminal run:
-- psql < music.sql

DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

\c music

-- CREATE TABLE songs
-- (
--   id SERIAL PRIMARY KEY,
--   title TEXT NOT NULL,
--   duration_in_seconds INTEGER NOT NULL,
--   release_date DATE NOT NULL,
--   artists TEXT[] NOT NULL,
--   album TEXT NOT NULL,
--   producers TEXT[] NOT NULL
-- );

-- INSERT INTO songs
--   (title, duration_in_seconds, release_date, artists, album, producers)
-- VALUES
--   ('MMMBop', 238, '04-15-1997', '{"Hanson"}', 'Middle of Nowhere', '{"Dust Brothers", "Stephen Lironi"}'),
--   ('Bohemian Rhapsody', 355, '10-31-1975', '{"Queen"}', 'A Night at the Opera', '{"Roy Thomas Baker"}'),
--   ('One Sweet Day', 282, '11-14-1995', '{"Mariah Cary", "Boyz II Men"}', 'Daydream', '{"Walter Afanasieff"}'),
--   ('Shallow', 216, '09-27-2018', '{"Lady Gaga", "Bradley Cooper"}', 'A Star Is Born', '{"Benjamin Rice"}'),
--   ('How You Remind Me', 223, '08-21-2001', '{"Nickelback"}', 'Silver Side Up', '{"Rick Parashar"}'),
--   ('New York State of Mind', 276, '10-20-2009', '{"Jay Z", "Alicia Keys"}', 'The Blueprint 3', '{"Al Shux"}'),
--   ('Dark Horse', 215, '12-17-2013', '{"Katy Perry", "Juicy J"}', 'Prism', '{"Max Martin", "Cirkut"}'),
--   ('Moves Like Jagger', 201, '06-21-2011', '{"Maroon 5", "Christina Aguilera"}', 'Hands All Over', '{"Shellback", "Benny Blanco"}'),
--   ('Complicated', 244, '05-14-2002', '{"Avril Lavigne"}', 'Let Go', '{"The Matrix"}'),
--   ('Say My Name', 240, '11-07-1999', '{"Destiny''s Child"}', 'The Writing''s on the Wall', '{"Darkchild"}');

CREATE TABLE producers (
  id SERIAL PRIMARY Key,
  producer TEXT [] NOT NULL
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  release_date DATE NOT NULL,
  producer_id INTEGER REFERENCES producers
);

CREATE TABLE songs (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  length_in_sec INTEGER NOT NULL,
  album_id INTEGER REFERENCES albums
);

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  artist_name TEXT NOT NULL,
  song_id INTEGER REFERENCES songs,
  album_id INTEGER REFERENCES albums
);

INSERT INTO producers (producer)
VALUES 
('{"Dust Brothers", "Stephen Lironi"}'),
('{"Roy Thomas Baker"}'),
('{"Walter Afanasieff"}'),
('{"Benjamin Rice"}'),
('{"Rick Parashar"}'),
('{"Al Shux"}'),
('{"Max Martin", "Cirkut"}'),
('{"Shellback", "Benny Blanco"}'),
('{"The Matrix"}'),
('{"Darkchild"}');

INSERT INTO albums (name, release_date, producer_id)
VALUES
('Middle of Nowhere', '04-15-1997', 1),
('A Night at the Opera', '10-31-1975', 2),
('Daydream', '11-14-1995', 3),
('A Star Is Born', '09-27-2018', 4),
('Silver Side Up', '08-2-2001', 5),
('The Blueprint 3', '10-20-2009', 6),
('Prism', '12-17-2013', 7),
('Hands All Over', '06-21-2011', 8),
('Let Go', '05-14-2002', 9),
('The Writing"s on the Wall', '11-07-1999', 10);

INSERT INTO songs (title, length_in_sec, album_id)
VALUES
('MMMBop', 238, 1),
('Bohemian Rhapsody', 355, 2),
('One Sweet Day', 282, 3),
('Shallow', 216, 4),
('How You Remind Me', 223, 5),
('New York State of Mind', 276, 6),
('Dark Horse', 215, 7),
('Moves Like Jagger', 201, 8),
('Complicated', 244, 9),
('Say My Name', 240, 10);

INSERT INTO artists (artist_name, song_id, album_id)
VALUES
('{"Hanson"}', 1, 1),
('{"Queen"}', 2, 2),
('{"Mariah Cary", "Boyz II Men"}', 3,3),
('{"Lady Gaga", "Bradley Cooper"}', 4, 4),
('{"Nickelback"}', 5, 5),
('{"Alicia Keys"}', 6, 6),
('{"Katy Perry", "Juicy J"}', 7, 7),
('{"Maroon 5", "Christina Aguilera"}', 8, 8),
('{"Avril Lavigne"}', 9, 9),
('{"Destiny"s Child"}', 10, 10);