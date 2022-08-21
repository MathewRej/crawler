drop table if exists songs;
drop table if exists artists;


create table artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30)
);

create table songs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(80),
    artist_id INTEGER references artists(id),
    lyrics TEXT
);