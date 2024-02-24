# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Yone/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 19704307  # integer value, dont use ""
    API_HASH = "031ab037968003ac20ec180d9ec3e07b"    
    TOKEN = "6254865362:AAHq3xj36h82o34CRKX5t5hDFV4lLD-TNmc"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 945137470  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "saint_foire"
    SUPPORT_CHAT = "zeekihq"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001180007354
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001237968047
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOGS = (
        -1001732618654
    )  # Prints information Error

    # RECOMMENDED
    DB_URI = "postgres://kwzssizt:QQVjmnJsftOrq2V2FKkrScuGa__K8QQq@lallah.db.elephantsql.com/kwzssizt"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False    
    
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
