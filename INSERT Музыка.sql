--Добавим исполнителей
INSERT INTO artist_list(id,nickname)
VALUES ('1','Nirvana'),
	('2','Lana Del Rey'),
	('3','Rihanna'),
	('4','Mireille Mathieu'),
	('5','Maneckin'),
	('6','Asti'),
	('7','Zemfira'),
	('8','Stromae');

--Жанры
INSERT INTO genre_list(id,genre_name)
VALUES ('1','Поп'),
	('2','Рок'),
	('3','R&B'),
	('4','Русский рок'),
	('5','Шансон');
	
--Альбомы
INSERT INTO albums(id,name_album,release_album)
VALUES ('1','земфира','1999-09-23'),
	('2','NFR!','2020-03-09'),
	('3','Anti','2021-11-01'),
	('4','Vivre','1986-04-12'),
	('5','Zitti','2020-05-16'),
	('6','7','2021-11-18'),
	('7','Cheese','2009-02-27'),
	('8','Nevermind','2011-01-21');
	
--Треки
INSERT INTO track_list(id,track,track_time)
VALUES ('1','torna a casa','3.40'),
	('2','Polly','3.10'),
	('3','Love song','4.13'),
	('4','California','5.11'),
	('5','-140','2.52'),
	('6','carmen','3.21'),
	('7','alors on danse','4.01'),
	('8','Lolita','2.34'),
	('9','in my feelings','3.09'),
	('10','ок','2.56'),
	('11','Bravo','4.12'),
	('12','самолет','4.44'),
	('13','Жди меня','3.52'),
	('14','lenfer','3.22'),
	('15','Мой','2.11');
	
--Коллекции
INSERT INTO collections(collection_name,release_date)
VALUES ('Cool','2020-01-21'),
	('coolection_big','2022-03-12'),
	('For mood','2019-10-31'),
	('Happy','2010-12-12'),
	('Sport','2009-02-09'),
	('Dance','2018-07-08'),
	('Dark athmo','2023-08-19'),
	('New','2021-12-30');