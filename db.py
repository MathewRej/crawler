import psycopg2

def get_connection(dbname = "lyrics"):
    return psycopg2.connect(f"dbname = {dbname}")

def add_artist(artist_name):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("insert into artists(name) values(%s)", (artist_name,))
        curs.execute("select id from artists order by id DESC")
        id = curs.fetchone()[0]
        conn.commit() 
        conn.close()
        return id


def add_song(song_name, artist_id, lyrics):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("insert into songs(name, artist_id, lyrics) values(%s,%s, %s)", (song_name, artist_id, lyrics))
    conn.commit()
    conn.close()