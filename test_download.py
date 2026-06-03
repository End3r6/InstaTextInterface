from pytubefix import YouTube, Search
from pytubefix.cli import on_progress

def get_song(query):
    results = Search(query)

    url = results.all[0].watch_url
    print(url)

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    path = ys.download(output_path="./downloads/")

    return path

get_song("Numb By Linkin Park")

