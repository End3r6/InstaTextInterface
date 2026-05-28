import yt_dlp
from base_bot_app import BaseBotApp
from email_helper import email_file


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

            email_file(
                file_path,
                subject=f"Song Download: {query}",
                body=f'Here is the file for "{query}".'
            )

            return f'Downloaded and emailed: "{query}"'

        except Exception as e:
            return f"Failed to download/email song: {e}"

    def get_song(self, query):
        ydl_opts = {
            "format": "ba[ext=m4a]/ba[ext=webm]/bestaudio/best",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "noplaylist": True,
            "default_search": "ytsearch1",
            "cookiefile": "cookies.txt",
            "listformats": True,
            "ignoreerrors": False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=True)


            if "entries" in info:
                info = info["entries"][0]

            return ydl.prepare_filename(info)
    