from flask import Flask, request, Response
import os

app = Flask(__name__)

MY_PHONE = os.getenv("MY_PHONE")

@app.route("/", methods=["GET"])
def home():
    return "Instagram helper server is running."

@app.route("/sms", methods=["POST"])
def sms():
    from_number = request.form.get("From")
    body = request.form.get("Body", "").strip().lower()

    if MY_PHONE and from_number != MY_PHONE:
        reply = "Unauthorized."
    elif body == "ping":
        reply = "pong"
    elif body == "ig":
        reply = "Instagram helper connected."
    elif body == "pic":
        xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>
        <Body>Here is the test picture.</Body>
        <Media>https://instatextinterface.onrender.com/static/ig.jpeg</Media>
    </Message>
</Response>"""

        return Response(xml, mimetype="text/xml")
    else:
        reply = "Commands: ping, ig"

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{reply}</Message>
</Response>"""

    return Response(xml, mimetype="text/xml")


#  +12029155212