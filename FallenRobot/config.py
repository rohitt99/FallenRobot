class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25830228
    API_HASH = "a23a5133bddbdab87df3df06ccf63a89"

    CASH_API_KEY = "ODEUSYY8R0JUK2DU"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002241127611)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://rohit6205881743:rohit6205881743@cluster0.soqtewz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/8c68edda7a29ef01a92b8.jpg"

    SUPPORT_CHAT = "-1001977784654"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7076111479:AAFRuKfDEHWnhhvkj3QvEF4clIawDJQVdLc"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "AYJ7PU3K31JB"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6722550550  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [6722550550]  # User id of sudo users
    DEV_USERS = [6722550550]  # User id of dev users
    DEMONS = [-1001977784654]  # User id of support users
    TIGERS = [6722550550]  # User id of tiger users
    WOLVES = [6722550550]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
