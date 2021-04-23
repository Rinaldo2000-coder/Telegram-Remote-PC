import webbrowser as web
from whatkit import playonyt

def YTvideo(song):
    song = (song.lower()).replace("play","")
    link = playonyt(song)
    web.open(link, new=0, autoraise=True)
if __name__ == '__main__':
    YTvideo("play sweet but psycho lyrics")
