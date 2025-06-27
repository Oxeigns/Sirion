"""Initialize commonly used objects for the OxygenMusic package."""

from .logging import LOGGER
from OxygenMusic.core.bot import Aviax
from OxygenMusic.core.userbot import Userbot
from OxygenMusic.core.dir import dirr
from OxygenMusic.core.git import git
from OxygenMusic.misc import dbb, heroku

app = Aviax()
userbot = Userbot()

from .platforms import (
    AppleAPI,
    CarbonAPI,
    RessoAPI,
    SoundAPI,
    SpotifyAPI,
    TeleAPI,
    YouTubeAPI,
)

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

dirr()
git()
dbb()
heroku()
