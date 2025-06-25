from OxygenMusic.core.bot import Aviax
from OxygenMusic.core.dir import dirr
from OxygenMusic.core.git import git
from OxygenMusic.core.userbot import Userbot
from OxygenMusic.misc import dbb, heroku

from .logging import LOGGER as LOGGER
from .platforms import (AppleAPI, CarbonAPI, RessoAPI, SoundAPI, SpotifyAPI,
                        TeleAPI, YouTubeAPI)

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
