# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1048578285:AAGmjcdQEAJQy9Q1TQA4VVuh4FDNhBdQino"
    OWNER_ID = "949789842"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "dickhunter18"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = None  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = "ANYTHING"
    URL = None

    # OPTIONAL
    SUDO_USERS = [949789842]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [949789842]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [949789842]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 8443
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADzAADECECEDbFGF9_b4P-FgQ'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    STRICT_GMUTE = True
    LOGGER = False
