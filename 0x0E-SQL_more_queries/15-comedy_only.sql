-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- The database name will be passed as an argument of the mysql command.
SELECT ts.title
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
JOIN tv_genres AS tg
ON tg.id = tsg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
