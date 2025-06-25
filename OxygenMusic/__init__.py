from OxygenMusic.core.bot import Aviax
from OxygenMusic.core.dir import dirr
from OxygenMusic.core.git import git
from OxygenMusic.core.userbot import Userbot
from OxygenMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
