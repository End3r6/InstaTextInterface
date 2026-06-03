from base_bot_app import BaseBotApp
from email_helper import email_file
from pytubefix import YouTube, Search
from pytubefix.cli import on_progress
from swiftshadow.classes import ProxyInterface
import os

class SongDownloader(BaseBotApp):
    name = "Song Downloader"
    description = "Finds and downloads songs"

    def register_commands(self):
        self.add_command(
            "find",
            self.find_song,
            'Find a song. Example: find "Numb" --artist "Linkin Park"'
        )

    def find_song(self, args, options):
        title = " ".join(args)
        artist = options.get("artist")

        if not title:
            return 'Usage: find "song title" --artist "artist name"'

        query = title
        if artist:
            query += f" {artist}"

        try:
            file_path = self.get_song(query)

            print("Song Found!")

            print("Beginning Email...")
            email_file(
                file_path,
                subject=f"Song Download: {query}",
                body=f'Here is the file for "{query}".'
            )

            print("Email Sent!")

            print("Deleting File...")
            os.remove(file_path)  # Delete the file after emailing
            print("File Deleted!")

            return f'Downloaded and emailed: "{query}"'

        except Exception as e:
            return f"Failed to download/email song: {e}"

    def get_song(self, query):
        proxy_https = ProxyInterface(protocol="https").get().as_string()
        proxy_http = ProxyInterface(protocol="http").get().as_string()

        proxy = {
            "http": proxy_https,
            "https": proxy_http
        }

        results = Search(query)

        url = results.all[0].watch_url
        print(url)

        yt = YouTube(url, proxies=proxy, on_progress_callback=on_progress)
        print(yt.title)

        ys = yt.streams.get_audio_only()
        path = ys.download(output_path="./downloads/")

        return path

