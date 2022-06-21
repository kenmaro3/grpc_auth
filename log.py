import logging
import uuid
import os

from datetime import datetime, timezone, timedelta
from logging.handlers import TimedRotatingFileHandler


if not os.path.exists("logs"):
    os.mkdir("logs")

handlers = [logging.StreamHandler()]

JST = timezone(timedelta(hours=+9), "JST")
now = datetime.now(JST)

time_handler = TimedRotatingFileHandler(
    "logs/d.log", when="midnight", interval=1
)
time_handler.suffix = "%Y-%m-%d"
handlers.append(time_handler)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] [%(levelname)s] %(module)s:: %(message)s",
    datefmt=f"{now:%Y-%m-%d %H:%M:%S}",
    handlers=handlers,
)

logging.getLogger("werkzeug").setLevel(logging.ERROR)


def get_time():
    return round(datetime.utcnow().timestamp() * 1000)


def get_uid():
    return uuid.uuid1().hex


