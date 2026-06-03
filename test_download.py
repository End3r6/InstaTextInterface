from pytubefix import YouTube, Search
from pytubefix.cli import on_progress
from swiftshadow.classes import ProxyInterface
from swiftshadow import QuickProxy


def get_song(query):
    # proxy_https = ProxyInterface(countries=["US"], protocol="https").get().as_string()
    proxy_https = QuickProxy(countries=["US"], protocol="https")
    print(type(QuickProxy(countries=["US"], protocol="https")))
    # proxy_http = ProxyInterface(protocol="http").get().as_string()
    proxy = {
        "https": proxy_https,
        # "http": proxy_http
    }

    # results = Search(query)
    # url = results.all[0].watch_url
    # print(url)

    # yt = YouTube(url, proxies=proxy, on_progress_callback=on_progress)
    # print(yt.title)

    # ys = yt.streams.get_audio_only()
    # path = ys.download(output_path="./downloads/")

    # return path

get_song("Numb By Linkin Park")

