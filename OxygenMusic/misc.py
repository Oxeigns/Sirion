import socket
import time

from pyrogram import filters

import config
from .logging import LOGGER

# In-memory database placeholder. This dictionary will be
# initialised by ``dbb()`` during bootstrap, but needs to be
# present at import time so that other modules can safely
# import ``db`` from here without hitting ``ImportError``.
db = {}

# ``SUDOERS`` now stores user IDs in a simple set while ``SUDOERS_FILTER``
# references a Pyrogram filter built from that set.  Mutating ``SUDOERS``
# will automatically affect the filter.
SUDOERS = set()
SUDOERS_FILTER = filters.user(list(SUDOERS))

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "master",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info("Local Database Initialized.")


async def sudo():
    from OxygenMusic.core.mongo import mongodb

    global SUDOERS_FILTER, SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    SUDOERS_FILTER = filters.user(list(SUDOERS))
    LOGGER(__name__).info("Sudoers Loaded.")


def heroku():
    global HAPP
    if is_heroku():
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                import heroku3

                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info("Heroku App Configured")
            except BaseException:
                LOGGER(__name__).warning(
                    "Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )


# Initialize in-memory database as soon as this module is imported.
dbb()

