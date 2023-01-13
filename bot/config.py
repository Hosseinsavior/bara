# (c) @AbirHasan2005


class Config(object):
    # You can keep this default
    SESSION_NAME = ("SESSION_NAME", "AHCompressorBot")
    # Put MongoDB URL
    DATABASE_URL = ("DATABASE_URL", "mongodb+srv://Hossein:XQipaxb5U84xrjMo@cluster0.hsdw6lz.mongodb.net/?retryWrites=true&w=majority")
    # get a token from @BotFather
    TG_BOT_TOKEN = ("TG_BOT_TOKEN", "5745311176:AAGZJqwVmOSEf_f-uJkKVFmc6pcjeE0LmYk")
    # The Telegram API things
    APP_ID = int(("APP_ID", "14699743"))
    API_HASH = ("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")
    LOG_CHANNEL = ("LOG_CHANNEL")
    UPDATES_CHANNEL = ("UPDATES_CHANNEL", None) # Without `@` LOL
     # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_USERS = ("AUTH_USERS", 5059280908
    )
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = ("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = ("BOT_USERNAME", "Savimusiceditbot")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = ("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = ("FINISHED_PROGRESS_STR", "▓")
    UN_FINISHED_PROGRESS_STR = ("UN_FINISHED_PROGRESS_STR", "░")
    LOG_FILE_ZZGEVC = ("LOG_FILE_ZZGEVC", "Log.txt")
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = ("SHOULD_USE_BUTTONS", False)
