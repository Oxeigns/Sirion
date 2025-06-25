from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import Iterable, List, Tuple, Union

Button = Union[
    Tuple[str, str],  # text, callback_data
    Tuple[str, str, bool],  # text, data, is_url
    Tuple[str, str, str],  # text, data, type: 'url', 'user', 'callback'
]


def build_inline_keyboard(rows: Iterable[Iterable[Button]]) -> InlineKeyboardMarkup:
    """Return InlineKeyboardMarkup from rows of button tuples.

    Supported tuple formats:
    - (text, callback_data)
    - (text, data, True)  -> treat data as URL
    - (text, data, "url"|"callback"|"user") to explicitly set type
    """
    keyboard: List[List[InlineKeyboardButton]] = []
    for row in rows:
        btn_row: List[InlineKeyboardButton] = []
        for item in row:
            if len(item) == 2:
                text, data = item
                btn_row.append(InlineKeyboardButton(text=text, callback_data=data))
            elif len(item) == 3 and isinstance(item[2], bool):
                text, data, is_url = item
                if is_url:
                    btn_row.append(InlineKeyboardButton(text=text, url=data))
                else:
                    btn_row.append(InlineKeyboardButton(text=text, callback_data=data))
            else:
                text, data, kind = item
                if kind == "url":
                    btn_row.append(InlineKeyboardButton(text=text, url=data))
                elif kind == "user":
                    btn_row.append(InlineKeyboardButton(text=text, user_id=int(data)))
                else:
                    btn_row.append(InlineKeyboardButton(text=text, callback_data=data))
        keyboard.append(btn_row)
    return InlineKeyboardMarkup(keyboard)
