SELECT name_album, release_album FROM albums
WHERE release_album BETWEEN '2018-01-01' AND '2018-12-31';

SELECT track, track_time FROM track_list
ORDER BY track_time DESC;

SELECT track FROM track_list
WHERE track_time >= '3.50';

SELECT collection_name FROM collections
WHERE release_date BETWEEN '2018-01-01' AND '2020-12-31';

SELECT nickname FROM artist_list
WHERE nickname NOT LIKE '% %';

SELECT track FROM track_list
WHERE track LIKE '%my%' OR '%Мой%';
