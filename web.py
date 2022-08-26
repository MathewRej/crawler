from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask("lyrics")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lyrics'
db = SQLAlchemy(app)

class Artists(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    songs = db.relationship("Songs", back_populates = "artist")

    def __repr__(self):
        return f"Artists('{self.name}')"

class Songs(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable = False)
    lyrics = db.Column(db.String)
    artist = db.relationship("Artists", back_populates = "songs")

    def __repr__(self):
        return f"Songs('{self.name}')"

@app.route("/")
def index():
    artists = Artists.query.all()
    # formatted = []
    # for artist in artists:
    #     target = url_for("artist", artist_id = artist.id)
    #     link = f'<a href = "{target}">{artist.name}</a>'
    #     formatted.append(f"<li>{link}</li>")
    #     artists = "".join(formatted)
    #     print(artists)
    return render_template('artists.html', artists = artists)

@app.route("/artist/<int:artist_id>")
def artist(artist_id):
    songs = Songs.query.filter_by(artist_id = artist_id).all()
    artist = Artists.query.get(artist_id)
    # formatted = []
    # for i in songs:
    #     target = url_for("song", song_id = i.id)
    #     link = f'<a href = "{target}">{i.name}</a>'
    #     formatted.append(f"<li>{link}</li>")
    #     songs = "".join(formatted)
    # return "<ul>" + "".join(formatted) + "</ul>"
    return render_template('songs.html',artist = artist.name, songs = songs)

@app.route("/song/<int:song_id>")
def song(song_id):
    song = Songs.query.filter_by(id = song_id).first()
    songs = Songs.query.filter_by(artist_id = song.artist_id).all()
    lyrics = song.lyrics.replace("\n","<br>")
    return render_template('lyrics.html', songs=songs,song_name = song.name,artist_name = song.artist.name,lyrics=lyrics)  