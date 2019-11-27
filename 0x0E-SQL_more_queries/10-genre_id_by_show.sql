-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
select tv_shows.title, tv_show_genres.genre_id from tv_shows join tv_show_genres
on tv_show_genres.show_id = tv_shows.id order by 1, 2;
