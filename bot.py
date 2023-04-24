from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "1834175795:AAHMyQudBP_f4JVxbIwXSMD9u2OJ5hF8FLA")

API_ID = int(os.environ.get("API_ID","3393749"))

API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "pdisk.pro",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
