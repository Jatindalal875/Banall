from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", "12834603")
    API_HASH = config("API_HASH", "84a5daf7ac334a70b3fbd180616a76c6")
    BOT_TOKEN = config("BOT_TOKEN", "6233213793:AAHKqb9O6Lq_YRKSEWXXOk28sQQ9Cr5XtVc")
    SUDO = list(map(int, getenv("SUDO", "5615344987 6699370215 5620092357").split()))
