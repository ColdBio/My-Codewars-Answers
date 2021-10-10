import re
def song_decoder(song):
    x = song.replace("WUB", " ").strip()
    print(re.sub(' +', ' ', x))
    return re.sub(' +', ' ', x)
