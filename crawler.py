import argparse
import logging

from bs4 import BeautifulSoup 
import requests

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action = "store_true")
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

def get_artists(artists):
    resp = requests.get(artists)
    soup = BeautifulSoup(resp.content, "lxml")
    track_list = soup.find("table", attrs = {"class" : "tracklist"})
    track_link = track_list.find_all('a')
    for link in track_link:
        if link.find('img') not in link:
            logger.info(link.text)

def get_artists_songs(artists_songs):
    resp = requests.get(artists_songs)
    soup = BeautifulSoup(resp.content, "lxml")
    song_lists = soup.find("table", attrs = {"class" : "tracklist"})
    song_list = song_lists.find_all('a')
    for list in song_list:
        logger.info(list.text)

def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    get_artists('https://www.songlyrics.com/top-artists-lyrics.html')
    get_artists_songs("http://www.songlyrics.com/katy-perry-lyrics/")
    
if __name__=="__main__":
    main()