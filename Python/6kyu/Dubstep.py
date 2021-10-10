import re
def song_decoder(song):
    x = song.replace("WUB", " ").strip()
    return re.sub(' +', ' ', x)
