
from curses import echo, meta
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()
engine = create_engine("postgresql:///lyrics", echo=True)
session = Session(engine)


class Artists(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    songs = relationship("Songs", back_populates = "artist")
    
    
class Songs(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable = False)
    lyrics = Column(String)
    artist = relationship("Artists", back_populates = "songs")


def add_artist(name):
    artist = Artists(name=name)
    session.add(artist)
    session.commit()
    session.refresh(artist)
    return artist

def add_song(name, lyrics, artist):
    song = Songs(name=name, lyrics=lyrics, artist=artist)
    session.add(song)
    session.commit()

def create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
