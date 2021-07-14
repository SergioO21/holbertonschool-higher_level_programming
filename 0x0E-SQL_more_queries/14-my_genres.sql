-- Lists all genres of the show Dexter.
-- The database name will be passed as an argument of the mysql command.
SELECT tg.name
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
