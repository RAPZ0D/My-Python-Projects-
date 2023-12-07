Create Database makeuplab;
use makeuplab;

CREATE TABLE Track (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    track_name TEXT,
    track_artist TEXT,
    track_popularity INT,
    track_album_id TEXT,
    danceability FLOAT,
    energy FLOAT,
    `key` INT,
    loudness FLOAT,
    mode INT,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    duration_ms INT
);

CREATE TABLE Album (
    album_id  INT AUTO_INCREMENT PRIMARY KEY,
    album_name TEXT,
    album_release_date TEXT
);

CREATE TABLE Playlist (
    playlist_id TEXT, -- INT auto_increment Primary Key,
    playlist_name TEXT,
    playlist_genre TEXT,
    playlist_subgenre TEXT
);

CREATE TABLE Track_Album (
    track_id INT,
    album_id INT,
	 FOREIGN KEY (track_id) REFERENCES Track(track_id),
    foreign key (album_id) References Album(album_id)
);


CREATE TABLE Track_Playlist (
    track_id INT,
    playlist_id INT,
     foreign key (track_id) References Track(track_id),
     foreign key (playlist_id) References Playlist(playlist_id)
);

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    playlist_genre TEXT
);

CREATE TABLE Track_Genre (
    track_id INT,
    genre_id INT auto_increment PRIMARY KEY,
    Foreign key (track_id) References Track(track_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);


select * from Track; 
