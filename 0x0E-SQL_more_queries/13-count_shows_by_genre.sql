-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- The database name will be passed as an argument of the mysql command.
SELECT tg.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg
ON tsg.genre_id = tg.id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC;
