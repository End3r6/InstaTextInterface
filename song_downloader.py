from command_system import Command, CommandContext
from base_bot_app import BaseBotApp


class SongDownloader(BaseBotApp):
    name = "Song Downloader"
    description = "The app to download songs"
    def execute(self, args, options):
        return "Downloading song!!"

    def get_song(self, title, artist):
        pass

