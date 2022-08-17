import argparse
import logging
import os
from socket import SO_LINGER

from bs4 import BeautifulSoup 
import requests

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action = "store_true")
    parser.add_argument("-download", help = "creates a directory for lyrics", action = "store")
    return parser.parse_args()

def configure_logging(level = logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

def get_artists(base):
    artists = {}
    resp = requests.get(base)
    soup = BeautifulSoup(resp.content, "lxml")
    track_lists = soup.find("table", attrs = {"class" : "tracklist"})
    track_link = track_lists.find_all('h3')
    for link in track_link[:5]:
        artists[link.text] = link.a['href']
    return artists
    
def get_artist_songs(artists):
    songs = {}
    resp = requests.get(artists)
    soup = BeautifulSoup(resp.content, "lxml")
    song_list = soup.find("table", attrs = {"class" : "tracklist"})
    songs_links = song_list.find_all('a')
    for song in songs_links[:3]:
        songs[song.text] = song['href']

    return songs

def get_artists_song_lyrics(song_lyrics):
    resp = requests.get(song_lyrics)
    soup = BeautifulSoup(resp.content, "lxml")
    lyrics = soup.find('p', attrs = {"id" : "songLyricsDiv"})
    return lyrics.text

def crawl(download_dir):
    for artist_name, artist_link in get_artists('http://www.songlyrics.com/top-artists-lyrics.html').items():
        logger.debug("Artist : %s", artist_name)
        artist_dir = os.path.join(download_dir, artist_name)
        os.makedirs(artist_dir, exist_ok = True)
        for song, song_link in get_artist_songs(artist_link).items():
            song_name = song.replace("/", " ")
            file = open(f"{artist_dir}/{song_name}.txt", "w")
            file.write(get_artists_song_lyrics(song_link))
            file.close()

def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    crawl("artists")

if __name__=="__main__":
    main()