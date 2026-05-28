from flask import Flask, request, Response
from command_system import CommandContext, parse_message
import os
from enum import Enum
from song_downloader import SongDownloader


class BotState(Enum):
    NEUTRAL = 1
    USING_APP = 2

app = Flask(__name__)

MY_PHONE = os.getenv("MY_PHONE")

bot_state = BotState.NEUTRAL

app_map = {
    "song_downloader" : SongDownloader
    }

app_instance = None

cookies = os.getenv("YOUTUBE_COOKIES")

if cookies:
    with open("cookies.txt", "w", encoding="utf-8") as f:
        f.write(cookies)

def sms_reply(text):
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{text}</Message>
</Response>"""
    return Response(xml, mimetype="text/xml")

@app.route("/", methods=["GET"])
def home():
    return "Instagram helper server is running."

@app.route("/low_balance", methods=["POST"])
def low_balance():
    return sms_reply("You have gone below the 5$ balance, adding more MONEYSSSSSS")

@app.route("/sms", methods=["POST"])
def sms():
    global bot_state
    global app_instance

    from_number = request.form.get("From")
    if MY_PHONE and from_number != MY_PHONE:
        return sms_reply("Unauthorized.")

    body = request.form.get("Body", "").strip().lower()

    args, options = parse_message(body)

    if bot_state == BotState.NEUTRAL:
        if len(args) >= 2 and args[0] == "use":
            app_name = args[1]

            app_instance = app_map[app_name]()
            bot_state = BotState.USING_APP
            return sms_reply(f"Using {app_name}. Type help for commands.")

        return sms_reply("Neutral mode. Type: use song_downloader")
    
    if bot_state == BotState.USING_APP:

        if args[0] == "quit":
            bot_state = BotState.NEUTRAL
            app_instance = None
            return sms_reply(f"Quitting app: {app_instance.name}")

        app_execute_results = app_instance.execute(args, options)

        return sms_reply(app_execute_results)




