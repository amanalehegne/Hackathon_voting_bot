
from os import getenv
from dotenv import load_dotenv

env_dir = ".env"

load_dotenv(env_dir)

telegram_token = getenv("BOT_TOKEN")
mongodb_connection_string = getenv("MONGO_DB_CONNECTION_STRING")
admin_ids = [int(i) for i in getenv("ADMIN_IDS").split(",") if getenv("ADMIN_IDS")]