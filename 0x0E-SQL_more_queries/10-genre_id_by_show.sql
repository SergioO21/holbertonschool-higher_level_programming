-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- The database name will be passed as an argument of the mysql command.
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
