CREATE TABLE IF NOT EXISTS artist_list(
	ID SERIAL PRIMARY KEY,
	nickname VARCHAR(60) NOT NULL);

CREATE TABLE IF NOT EXISTS genre_list(
	ID SERIAL PRIMARY KEY,
	genre_name VARCHAR(80) NOT NULL);

CREATE TABLE IF NOT EXISTS albums(
	ID SERIAL PRIMARY KEY,
	name_album VARCHAR(60) NOT NULL,
	release_album DATE);

CREATE TABLE IF NOT EXISTS collections(
	ID SERIAL PRIMARY KEY,
	collection_name VARCHAR(80) NOT NULL,
	release_date DATE);

CREATE TABLE IF NOT EXISTS artist_in_genre(
	ID SERIAL PRIMARY KEY,
	artist_id INTEGER NOT NULL REFERENCES artist_list(id),
	genre_id INTEGER NOT NULL REFERENCES genre_list(id));
	
CREATE TABLE IF NOT EXISTS track_list(
	ID SERIAL PRIMARY KEY,
	album_id INTEGER REFERENCES albums(id),
	track VARCHAR(80) NOT NULL,
	track_time VARCHAR(80) NOT NULL);
	
CREATE TABLE IF NOT EXISTS collection_track(
	ID SERIAL PRIMARY KEY,
	collection_id INTEGER NOT NULL REFERENCES collections(id),
	track_id INTEGER NOT NULL REFERENCES track_list(id));

CREATE TABLE IF NOT EXISTS artist_albums(
	ID SERIAL PRIMARY KEY,
	artist_id INTEGER NOT NULL REFERENCES artist_list(id),
	album_id INTEGER NOT NULL REFERENCES albums(id));
	
