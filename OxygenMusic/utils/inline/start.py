import config
from OxygenMusic import app

from .keyboard import build_inline_keyboard


def start_panel(_):
    return build_inline_keyboard(
        [
            (
                (_["S_B_1"], f"https://t.me/{app.username}?startgroup=true", True),
                (_["S_B_2"], config.SUPPORT_GROUP, True),
            ),
            ((_["S_B_10"], "https://t.me/oxeign", True),),
            ((_["S_B_7"], "https://t.me/TeamSirion", True),),
        ]
    )


def private_panel(_):
    return build_inline_keyboard(
        [
            ((_["S_B_3"], f"https://t.me/{app.username}?startgroup=true", True),),
            (
                (_["S_B_4"], "settings_back_helper"),
                (_["S_B_2"], config.SUPPORT_GROUP, True),
            ),
            (
                (_["S_B_6"], config.SUPPORT_CHANNEL, True),
                (_["S_B_5"], str(config.OWNER_ID), "user"),
            ),
            ((_["S_B_10"], "https://t.me/oxeign", True),),
            ((_["S_B_7"], "https://t.me/TeamSirion", True),),
        ]
    )
