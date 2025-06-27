"""Initialization helpers for OxygenMusic."""
from .core.dir import dirr
from .core.git import git
from .misc import dbb, heroku
from .core.bot import Aviax
from .core.userbot import Userbot
from .platforms import AppleAPI, CarbonAPI, RessoAPI, SoundAPI, SpotifyAPI, YouTubeAPI
from .platforms.Telegram import TeleAPI


def bootstrap():
    """Setup project directories and return initialized clients."""
    dirr()
    git()
    dbb()
    heroku()

    bot = Aviax()
    user = Userbot()

    apple = AppleAPI()
    carbon = CarbonAPI()
    sound = SoundAPI()
    spotify = SpotifyAPI()
    resso = RessoAPI()
    youtube = YouTubeAPI()
    telegram = TeleAPI(bot)

    return bot, user, apple, carbon, sound, spotify, resso, youtube, telegram
